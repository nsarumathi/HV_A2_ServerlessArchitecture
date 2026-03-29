import boto3
from datetime import datetime, timedelta, timezone

cloudwatch = boto3.client('cloudwatch')
sns = boto3.client('sns')

# 🔹 Replace with your values
SNS_TOPIC_ARN = 'arn:aws:sns:ap-south-2:944765969321:ELB-Error-Alerts'
LOAD_BALANCER = 'app/ALB-Demo/cbcbc5148aa4603e'

THRESHOLD = 1   # keep low for testing
PERIOD = 300

def lambda_handler(event, context):

    end_time = datetime.now(timezone.utc)
    start_time = end_time - timedelta(seconds=PERIOD)

    response = cloudwatch.get_metric_statistics(
        Namespace='AWS/ApplicationELB',
        MetricName='HTTPCode_ELB_5XX_Count',
        Dimensions=[
            {
                'Name': 'LoadBalancer',
                'Value': LOAD_BALANCER
            }
        ],
        StartTime=start_time,
        EndTime=end_time,
        Period=PERIOD,
        Statistics=['Sum']
    )

    datapoints = response.get('Datapoints', [])

    error_count = 0
    if datapoints:
        latest = sorted(datapoints, key=lambda x: x['Timestamp'])[-1]
        error_count = int(latest['Sum'])

    print("5xx Errors:", error_count)

    if error_count > THRESHOLD:
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="🚨 ALB 5xx Alert",
            Message=f"ALERT: 5xx errors = {error_count}"
        )