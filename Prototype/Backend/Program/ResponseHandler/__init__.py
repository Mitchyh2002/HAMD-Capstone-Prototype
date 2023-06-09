import json

def on_error(error_code, error_message):
    return {"Success": False,
            "StatusCode": error_code,
            "Message": error_message}

def on_success(data):
    return {
        "Success": True,
        "StatusCode": 200,
        "Values": data
    }