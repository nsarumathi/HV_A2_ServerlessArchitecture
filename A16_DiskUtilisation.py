import boto3
from datetime import datetime, timedelta

sns = boto3.client('sns')
ec2 = boto3.client('ec2')
cloudwatch = boto3.client('cloudwatch')

SNS_TOPIC_ARN = "arn:aws:sns:ap-south-2:944765969321:EC2DiskAlerts"
DISK_THRESHOLD = 5  # percent

def lambda_handler(event, context):
    print("Starting EC2 disk space check...")
    
    # 1. List all EC2 instances
    instances = ec2.describe_instances()
    
    alerts = []
    
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            
            # 2. Get CloudWatch metric for disk utilization
            try:
                response = cloudwatch.get_metric_statistics(
                    Namespace='CWAgent',
                    MetricName='disk_used_percent',
                    Dimensions=[
                        {'Name': 'InstanceId', 'Value': instance_id},
                        # Assuming metric reports for root volume '/' 
                        {'Name': 'path', 'Value': '/'},
                        {'Name': 'filesystem', 'Value': 'root'}
                    ],
                    StartTime=datetime.utcnow() - timedelta(minutes=30),
                    EndTime=datetime.utcnow(),
                    Period=300,
                    Statistics=['Average']
                )
                
                datapoints = response['Datapoints']
                if datapoints:
                    utilization = datapoints[-1]['Average']
                    print(f"Instance {instance_id} Disk Usage: {utilization:.2f}%")
                    
                    if utilization > DISK_THRESHOLD:
                        alerts.append(f"Instance {instance_id} disk usage is {utilization:.2f}%")
                else:
                    print(f"No disk metrics found for instance {instance_id}")
                    
            except Exception as e:
                print(f"Error fetching metrics for {instance_id}: {e}")
    
    # 3. Send SNS alert if threshold exceeded
    if alerts:
        message = "🚨 EC2 Disk Space Alert:\n\n" + "\n".join(alerts)
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="EC2 Disk Space Utilization Alert",
            Message=message
        )
        print("SNS alert sent.")
    else:
        print("No instances exceeded disk threshold.")
    
    return {"statusCode": 200, "body": f"{len(alerts)} alerts sent."}