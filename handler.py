import json
import datetime


def hello(event, context):
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

def hello_stiven(event, context):
    current_date = datetime.date.today().strftime("%Y-%m-%d")
    message = f"Hola Stiven {current_date}"
    body = {
        "message": message
    }
    response = {"statusCode": 200, "body": json.dumps(body)}
    return response

def saludo(event, context):
    body = {
        "message": "Hola mundo"
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
