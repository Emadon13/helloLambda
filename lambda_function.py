import json
import os

def lambda_handler(event, context):
    
    name = os.environ['DEFAULT_NAME']
    if "name" in event:
        name = event['name']
        
    helloer = Helloer(name)
    message = helloer.hello()
    
    return {
        'statusCode': 200,
        'body': json.dumps(message)
    }


class Helloer:
    
    name = "utilisateur lambda"
    def __init__(self, name):
        self.name = name
    
    def hello(self):
        return "Hello {} !".format(self.name)
    
    def goodbye(self):
        return "Goodbye {} !".format(self.name)
