import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
connections_table = dynamodb.Table(os.environ['CONNECTIONS_TABLE'])
stats_table = dynamodb.Table(os.environ['STATS_TABLE'])

def lambda_handler(event, context):
    route_key = event.get('requestContext', {}).get('routeKey')
    connection_id = event.get('requestContext', {}).get('connectionId')

    if route_key == '$connect':
        # Store connection ID
        connections_table.put_item(Item={'connectionId': connection_id})
        
        # Increment visitor count (similar to our previous logic)
        stats_table.update_item(
            Key={'id': '1'},
            UpdateExpression='SET visitor_count = if_not_exists(visitor_count, :zero) + :inc',
            ExpressionAttributeValues={':inc': 1, ':zero': 0}
        )
        return {'statusCode': 200, 'body': 'Connected'}

    elif route_key == '$disconnect':
        # Remove connection ID
        connections_table.delete_item(Key={'connectionId': connection_id})
        return {'statusCode': 200, 'body': 'Disconnected'}

    return {'statusCode': 400, 'body': 'Unknown route'}
