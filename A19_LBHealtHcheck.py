import boto3
import os

# Environment variables for flexibility
ELB_NAME = os.environ.get('ELB_NAME')
SNS_TOPIC_ARN = os.environ.get('SNS_TOPIC_ARN')

elb_client = boto3.client('elb')  # Use 'elbv2' for ALB/NLB v2
sns_client = boto3.client('sns')

def lambda_handler(event, context):
    try:
        # Fetch health of instances registered with the ELB
        response = elb_client.describe_instance_health(LoadBalancerName=ELB_NAME)
        instance_states = response['InstanceStates']

        unhealthy_instances = []
        for inst in instance_states:
            if inst['State'] != 'InService':
                unhealthy_instances.append({
                    'InstanceId': inst['InstanceId'],
                    'State': inst['State'],
                    'Reason': inst.get('Description', 'No description')
                })

        if unhealthy_instances:
            message = f"⚠️ Unhealthy instances detected in ELB '{ELB_NAME}':\n\n"
            for inst in unhealthy_instances:
                message += f"InstanceId: {inst['InstanceId']}, State: {inst['State']}, Reason: {inst['Reason']}\n"

            # Publish to SNS
            sns_client.publish(
                TopicArn=SNS_TOPIC_ARN,
                Subject=f"ELB Health Alert: {len(unhealthy_instances)} Unhealthy Instance(s)",
                Message=message
            )
            print("SNS notification sent for unhealthy instances.")
        else:
            print(f"All instances in ELB '{ELB_NAME}' are healthy.")

        return {
            'statusCode': 200,
            'body': 'Health check completed successfully'
        }

    except Exception as e:
        print(f"Error checking ELB health: {e}")
        raise e