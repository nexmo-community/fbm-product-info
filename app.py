from flask import Flask, request, jsonify
from pprint import pprint

# Mini client library
from FBMClient.FBMClient import FBMClient

FB_SENDER = "YOUR_FB_SENDER"
NEXMO_APP_ID = "YOUR_NEXMO_APP_ID"

def product_matcher (user, msg):
    msg = msg.lower().strip()
    print("DEBUG: msg is %s" % msg)
    if 'crane' in msg:
        product = "crane"
        fbm.send_message(FB_SENDER, user, "For details of Crane hire services go here https://crane.example.com.")
    elif 'tank' in msg:
        product = "tank"
        fbm.send_message(FB_SENDER, user, "For details of Tank Cleaning services go here https://tank.example.com.")
    elif 'tool' in msg:
        product = "toolshed"
        fbm.send_message(FB_SENDER, user, "For details of Toolshed hire services go here https://toolshed.example.com.")
    else:
        product = "other"
        fbm.send_message(FB_SENDER, user, "For details of our complete range of services go here https://crane.example.com.")
    return product    

def log_to_database (user, product):
    print("User: %s with interest in Product: %s logged to database." % (user, product))
    return

jwt_expiry = 1*60*60 # JWT expires after one hour (default is 15 minutes)
filename = "private.key"
fbm = FBMClient(NEXMO_APP_ID, filename, jwt_expiry)
app = Flask(__name__)

@app.route('/inbound', methods=['POST'])
def inbound_message():
    data = request.get_json()
    user = data['from']['id']
    in_msg = data['message']['content']['text']
    if "info:" not in in_msg:
        fbm.send_message(FB_SENDER, user, "Thanks for contacting us. Type 'info: product' to receive info for a specific service. For example - send us a message 'info: tank cleaning'")
    else:
        in_msg = in_msg.split(':')[1]
        product = product_matcher(user, in_msg)
        #log_to_database(user, product)
    return ("200")

@app.route('/status', methods=['POST'])
def message_status():
    print ("Message status:")    
    data = request.get_json()
    pprint(data)
    return ("200")

if __name__ == '__main__':
    app.run(host="localhost", port=9000)
    
