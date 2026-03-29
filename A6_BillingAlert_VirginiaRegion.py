import boto3
from datetime import datetime, timedelta

def lambda_handler(event, context):
    # Billing metrics only available in us-east-1
    cloudwatch = boto3.client('cloudwatch', region_name='us-east-1')
    sns = boto3.client('sns')

    topic_arn = 'arn:aws:sns:us-east-1:944765969321:BillingAlertTopic_Virginia'

    end_time = datetime.utcnow()
    start_time = end_time - timedelta(days=1)

    response = cloudwatch.get_metric_statistics(
        Namespace='AWS/Billing',
        MetricName='EstimatedCharges',
        Dimensions=[{'Name': 'Currency', 'Value': 'USD'}],
        StartTime=start_time,
        EndTime=end_time,
        Period=86400,
        Statistics=['Maximum']
    )

    if not response['Datapoints']:
        message = "No billing data available yet."
        print(message)
    else:
        latest_charge = max(dp['Maximum'] for dp in response['Datapoints'])
        message = f"Current AWS Billing Amount: ${latest_charge}"
        print(message)

    # Send email via SNS
    sns.publish(
        TopicArn=topic_arn,
        Subject='AWS Billing Update',
        Message=message
    )

    print("Email sent successfully")

    return {
        'statusCode': 200,
        'body': message
    }