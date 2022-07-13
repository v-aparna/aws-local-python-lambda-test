import json

def read_json_to_event(i):
    input_json = open(i)
    event = json.load(input_json)
    return event

'''
Sample code from AWS documentation https://docs.aws.amazon.com/lambda/latest/dg/python-handler.html
'''
def lambda_handler(event, context):
    message = 'Hello {} {}!'.format(event['first_name'], event['last_name'])  
    return { 
        'message' : message
    }

'''
Call the lambda_handler function as aws would, when you invoke a lambda function
'''
event = read_json_to_event("event.json")
print(lambda_handler(event, context=None))