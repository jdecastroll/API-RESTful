import json 
import os

from todos import decimalencoder

import boto3
dynamodb = boto3.resource('dynamodb')
apitranslate = boto3.client('translate')

def translate(event, context):

    tabla = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    result = tabla.get_item(
        Key={
            'id': event['pathParameters']['id']
        }
    ) 

    language_dest = event['pathParameters']['lang']
    init_issue = result ['Item']['text']

    translate_issue = apitranslate.translate_text(Text=init_issue,SourceLanguageCode='auto', TargetLanguageCode=language_dest)

    result['Item']['text'] = translate_issue['TranslatedText']

    response = {
      "statusCode": 200,
      "body": json.dumps(result['Item'], cls=decimalencoder.DecimalEncoder)
    }

    return response
