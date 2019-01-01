import os

def hello(event, context):
    return {
        "statusCode": 200,
        "body": "The answer is: " + os.environ["THE_ANSWER"]
    }