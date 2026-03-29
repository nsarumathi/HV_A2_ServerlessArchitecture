import json
import boto3

comprehend = boto3.client('comprehend', region_name='ap-south-1')

def lambda_handler(event, context):
    try:
        # 1. Extract review text from event
        review_text = event.get('review', '')

        if not review_text:
            return {
                'statusCode': 400,
                'body': json.dumps('No review text provided')
            }

        # 2. Call Amazon Comprehend
        response = comprehend.detect_sentiment(
            Text=review_text,
            LanguageCode='en'
        )

        sentiment = response['Sentiment']
        scores = response['SentimentScore']

        # 3. Log result (CloudWatch)
        print(f"Review: {review_text}")
        print(f"Sentiment: {sentiment}")
        print(f"Scores: {scores}")

        # 4. Return response
        return {
            'statusCode': 200,
            'body': json.dumps({
                'review': review_text,
                'sentiment': sentiment,
                'scores': scores
            })
        }

    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(str(e))
        }