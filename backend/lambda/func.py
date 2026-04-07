import json
import boto3
import os

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('TABLE_NAME', 'cloud-resume-stats')
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    # Atomic increment for visitor count
    response = table.update_item(
        Key={
            'id': '1'
        },
        UpdateExpression='SET visitor_count = if_not_exists(visitor_count, :zero) + :inc',
        ExpressionAttributeValues={
            ':inc': 1,
            ':zero': 0
        },
        ReturnValues='UPDATED_NEW'
    )
    
    visitor_count = response['Attributes']['visitor_count']
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Content-Type': 'application/json'
        },
        'body': json.dumps({'count': int(visitor_count)})
    }
