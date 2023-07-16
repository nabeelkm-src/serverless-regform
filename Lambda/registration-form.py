import json
import boto3

dyanamodb = boto3.resource('dyanamodb')
table = dyanamodb.Table('registration-table')

def lambda_handler(event, context):
    #Get request body
    print(event)
    
    #create new item in DynamoDB table
    response = table.put_item(
         Item={
             'email': event['email'],
             'name': event['name'],
             'phone': event['phone'],
             'password': event['password']
         }
    )
    
    # Return response
    return {
        'statusCode':200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Contro-Allow-Origin': '*'
        },
        'body': json.dump({'message': 'Registration successful'})
    }