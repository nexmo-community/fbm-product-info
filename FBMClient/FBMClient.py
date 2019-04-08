# https://github.com/jpadilla/pyjwt -- pip3 install PyJWT
import jwt 
import time
import json
import requests
from uuid import uuid4
from pprint import pprint

class FBMClient:
    
    def __init__(self, app_id, filename, expiry):
        
        # Read in private key from store
        f = open(filename, 'r')
        self.private_key = f.read()
        f.close()

        # Build JWT payload
        self.payload = {
            'application_id': app_id,
            'iat': int(time.time()),
            'jti': str(uuid4()),
            'exp': int(time.time()) + expiry,
        }
        return

    def send_message (self, fb_sender, fb_recipient, msg):

        print("Sending FBM message...")
        
        data_body = {
            "from": {
	        "type": "messenger",
	        "id": fb_sender
            },
            "to": {
	        "type": "messenger",
	        "id": fb_recipient
            },
            "message": {
	        "content": {
	            "type": "text",
	            "text": msg
	        }
            }
        }

        data_body = json.dumps(data_body)        
        gen_jwt  = jwt.encode(self.payload, self.private_key, algorithm='RS256')
        auth = b'Bearer '+gen_jwt
        headers = {'Authorization': auth, 'Content-Type': 'application/json'}
        r = requests.post('https://api.nexmo.com/v0.1/messages', headers=headers, data=data_body)
        j = r.json()
        pprint(j)
