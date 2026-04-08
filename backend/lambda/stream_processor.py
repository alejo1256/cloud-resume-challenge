import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
apigateway = boto3.client('apigatewaymanagementapi', endpoint_url=os.environ['WEBSOCKET_API_URL'])
connections_table = dynamodb.Table(os.environ['CONNECTIONS_TABLE'])

def lambda_handler(event, context):
    for record in event['Records']:
        if record['eventName'] == 'MODIFY' or record['eventName'] == 'INSERT':
            # Get new visitor count from the stream record
            new_count = int(record['dynamodb']['NewImage']['visitor_count']['N'])
            
            # Get all active connection IDs
            active_connections = connections_table.scan(ProjectionExpression='connectionId')['Items']
            
            # Broadcast the new count to everyone
            for conn in active_connections:
                conn_id = conn['connectionId']
                try:
                    apigateway.post_to_connection(
                        ConnectionId=conn_id,
                        Data=json.dumps({'count': new_count})
                    )
                except apigateway.exceptions.GoneException:
                    # Clean up if the connection is gone but still in our DB
                    connections_table.delete_item(Key={'connectionId': conn_id})
                    
    return {'statusCode': 200}
