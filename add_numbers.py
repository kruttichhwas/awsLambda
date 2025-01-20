import json

def lambda_handler(event, context):
    """
    An AWS Lambda function that adds two numbers passed in the event,
    and returns the sum in the response.

    Expected event format:
    {
      "num1": 10,
      "num2": 20
    }

    Returns:
    {
      "statusCode": 200,
      "body": "{\"result\": 30}"
    }
    """

    # Extract numbers from event
    num1 = event
