from flask import Flask, request, jsonify
from pprint import pprint
from ProductMatcher.ProductMatcher import ProductMatcher

NEXMO_APP_ID = "YOUR_NEXMO_APP_ID"

pm = ProductMatcher(NEXMO_APP_ID)
app = Flask(__name__)

@app.route('/inbound', methods=['POST'])
def inbound_message():
    print ("Inbound Message...")    
    data = request.get_json()
    user = data['from']['id']
    fb_sender = data['to']['id']
    in_msg = data['message']['content']['text']
    pm.product_match(fb_sender, user, in_msg)
    return ("200")

@app.route('/status', methods=['POST'])
def message_status():
    print ("Message status:")    
    data = request.get_json()
    pprint(data)
    return ("200")

if __name__ == '__main__':
    app.run(host="localhost", port=9000)
    
