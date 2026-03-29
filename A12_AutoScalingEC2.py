import boto3
from datetime import datetime, timedelta

ec2 = boto3.client('ec2')
cloudwatch = boto3.client('cloudwatch')
sns = boto3.client('sns')

# 🔔 Replace with your actual SNS ARN
SNS_TOPIC_ARN = 'arn:aws:sns:ap-south-2:944765969321:EC2-Scaling-Alerts'

# CONFIG
INSTANCE_AMI = 'ami-09272d058ffc9bd9a'
INSTANCE_TYPE = 't3.micro'
KEY_NAME = 'demo'
SECURITY_GROUP = ['sg-059586966eb79f215']
SUBNET_ID = 'subnet-052bdb03da2046813'

HIGH_THRESHOLD = 5
LOW_THRESHOLD = 2


def get_network_load():
    end_time = datetime.utcnow()
    start_time = end_time - timedelta(minutes=5)

    response = cloudwatch.get_metric_statistics(
        Namespace='AWS/ApplicationELB',
        MetricName='RequestCount',
        Dimensions=[
            {'Name': 'LoadBalancer', 'Value': 'app/my-alb/982951f871cd1c3b'}
        ],
        StartTime=start_time,
        EndTime=end_time,
        Period=300,
        Statistics=['Sum']
    )

    datapoints = response['Datapoints']

    if not datapoints:
        return 0

    # ✅ Use Sum (NOT Average)
    return datapoints[0]['Sum']


def get_running_instances():
    response = ec2.describe_instances(
        Filters=[
            {'Name': 'instance-state-name', 'Values': ['running']}
        ]
    )

    instances = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instances.append(instance['InstanceId'])

    return instances


def launch_instance():
    response = ec2.run_instances(
        ImageId=INSTANCE_AMI,
        InstanceType=INSTANCE_TYPE,
        KeyName=KEY_NAME,
        SecurityGroupIds=SECURITY_GROUP,
        SubnetId=SUBNET_ID,
        MinCount=1,
        MaxCount=1
    )

    instance_id = response['Instances'][0]['InstanceId']
    return instance_id


def terminate_instance(instance_id):
    ec2.terminate_instances(InstanceIds=[instance_id])


def send_notification(message):
    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Message=message,
        Subject='EC2 Auto Scaling Notification'
    )


def lambda_handler(event, context):
    load = get_network_load()
    instances = get_running_instances()

    print(f"Current Load: {load}")
    print(f"Running Instances: {len(instances)}")

    if load > HIGH_THRESHOLD:
        instance_id = launch_instance()
        msg = f"High load detected ({load}). Launched instance: {instance_id}"
        send_notification(msg)

    elif load < LOW_THRESHOLD and len(instances) > 1:
        instance_id = instances[-1]
        terminate_instance(instance_id)
        msg = f"Low load detected ({load}). Terminated instance: {instance_id}"
        send_notification(msg)

    else:
        print("No scaling action required.")