import json
import base64
import boto3

s3_client = boto3.client("s3")

def lambda_handler(event, context):
    """
    An AWS Lambda function that takes a base64-encoded document (PDF or other file)
    from the event and uploads it to S3.

    Expected event format:
    {
      "bucket_name": "my-bucket",
      "file_name": "documents/sample.pdf",
      "file_content_base64": "<BASE64_ENCODED_DATA>"
    }

    Returns: 
    {
      "statusCode": 200,
      "body": "{\"message\": \"File uploaded successfully!\"}"
    } on success

    or an error message if something goes wrong.
    """

    try:
        # Read parameters from event
        bucket_name = event["bucket_name"]
        file_name = event["file_name"]
        file_content_base64 = event["file_content_base64"]

        # Decode the base64 file content
        file_content = base64.b64decode(file_content_base64)

        # Upload to S3
        s3_client.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=file_content
        )

        response = {
            "statusCode": 200,
            "body": json.dumps({"message": "File uploaded successfully!"})
        }
        return response

    except Exception as e:
        response = {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
        return response
