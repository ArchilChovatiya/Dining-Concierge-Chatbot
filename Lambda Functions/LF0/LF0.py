import json
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

client = boto3.client('lex-runtime')
def lambda_handler(event, context):
    
    response = client.post_text(
        botName='Diningone',
        botAlias='$LATEST',
        userId='userO',
        inputText=event['messages'][0]['unstructured']['text']
        )
    print(response)
    botResponse =  [{
        'type': 'unstructured',
        'unstructured': {
          'text': response["message"]
        }}]
    return {
        'statusCode': 200,
        'messages': botResponse
        }
