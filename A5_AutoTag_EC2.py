import boto3
from datetime import datetime

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    # 🔹 Extract instance ID from event
    instance_id = event['detail']['instance-id']

    # 🔹 Current date
    current_date = datetime.now().strftime('%Y-%m-%d')

    # 🔹 Add tags
    ec2.create_tags(
        Resources=[instance_id],
        Tags=[
            {'Key': 'CreatedOn', 'Value': current_date},
            {'Key': 'Environment', 'Value': 'Dev'}
        ]
    )

    print(f"Tagged instance {instance_id} with date {current_date}")

    return {
        'statusCode': 200,
        'body': f"Instance {instance_id} tagged successfully"
    }