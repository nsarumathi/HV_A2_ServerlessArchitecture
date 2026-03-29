import boto3
import json

sns = boto3.client('sns')


SNS_TOPIC_ARN = "arn:aws:sns:ap-south-2:944765969321:EC2StateChangeAlerts"

def lambda_handler(event, context):
    """
    Triggered by EC2 state change events from EventBridge
    """
    print("Received event:", json.dumps(event))
    
    # Extract EC2 instance ID and state from event
    detail = event.get('detail', {})
    instance_id = detail.get('instance-id')
    state = detail.get('state')
    
    if instance_id and state:
        # Build message
        message = f"EC2 Instance State Change:\n\nInstance ID: {instance_id}\nNew State: {state}"
        
        # Send SNS notification
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="EC2 Instance State Change Alert",
            Message=message
        )
        print(f"Notification sent for instance {instance_id} -> {state}")
    else:
        print("Event does not contain instance-id or state.")

    return {
        "statusCode": 200,
        "body": json.dumps({"instance_id": instance_id, "state": state})
    }