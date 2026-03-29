import boto3
from datetime import datetime, timedelta

def lambda_handler(event, context):
    cloudwatch = boto3.client('cloudwatch')
    sns = boto3.client('sns')

    topic_arn = 'arn:aws:sns:ap-south-2:944765969321:BillingAlertTopic'
    threshold = 5  # USD

    # Time range (last 1 day)
    end_time = datetime.utcnow()
    start_time = end_time - timedelta(days=1)

    response = cloudwatch.get_metric_statistics(
        Namespace='AWS/Billing',
        MetricName='EstimatedCharges',
        Dimensions=[
            {'Name': 'Currency', 'Value': 'USD'}
        ],
        StartTime=start_time,
        EndTime=end_time,
        Period=86400,
        Statistics=['Maximum']
    )

    if not response['Datapoints']:
        print("No billing data found")
        return

    latest_charge = max(dp['Maximum'] for dp in response['Datapoints'])

    print(f"Current AWS Charges: ${latest_charge}")

    if latest_charge > threshold:
        message = f"AWS billing alert! Current charges: ${latest_charge}"

        sns.publish(
            TopicArn=topic_arn,
            Subject='AWS Billing Alert',
            Message=message
        )

        print("Alert sent via SNS")
    else:
        print("Charges within limit")

    return {
        'statusCode': 200,
        'body': f"Checked billing: ${latest_charge}"
    }