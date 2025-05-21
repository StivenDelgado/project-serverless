import json
import datetime
import handler

def test_hello_stiven():
    response = handler.hello_stiven({}, {})
    assert response['statusCode'] == 200
    
    parsed_body = json.loads(response['body'])
    assert parsed_body['message'].startswith("Hola Stiven ")
    
    date_string = parsed_body['message'].replace("Hola Stiven ", "")
    try:
        datetime.datetime.strptime(date_string, '%Y-%m-%d')
    except ValueError:
        assert False, f"Date string '{date_string}' is not in YYYY-MM-DD format"
