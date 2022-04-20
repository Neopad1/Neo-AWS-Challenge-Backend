import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Neo_Resume')


def lambda_handler(event, context):
    response = table.get_item(Key={
        'no_visits': '0'
        
    })
    
    newView = response['Item']['newView']
    newView = newView + 1
    print(newView)
    
    response = table.put_item(Item={
        'no_visits':'0',
        'newView': newView
    })
    
    return "sucessful response code 200"
