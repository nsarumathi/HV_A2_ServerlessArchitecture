import boto3
import json

def lambda_handler(event, context):
    sns = boto3.client('sns')
    topic_arn = 'arn:aws:sns:ap-south-2:944765969321:DynamoDBAlertTopic'

    for record in event['Records']:
        event_name = record['eventName']  # INSERT, MODIFY, REMOVE

        if event_name == 'MODIFY':
            new_image = record['dynamodb'].get('NewImage', {})
            old_image = record['dynamodb'].get('OldImage', {})

            message = f"""
DynamoDB Item Updated!

Old Value:
{json.dumps(old_image, indent=2)}

New Value:
{json.dumps(new_image, indent=2)}
"""

            sns.publish(
                TopicArn=topic_arn,
                Subject='DynamoDB Update Alert',
                Message=message
            )

            print("Alert sent for update")

    return {
        'statusCode': 200,
        'body': 'Processed DynamoDB stream'
    }