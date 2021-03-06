import sys
from flask import Flask, request, jsonify
from pprint import pprint
from ProductMatcher.ProductMatcher import ProductMatcher

NEXMO_APP_ID = sys.argv[1]
print("Nexmo App ID: %s" % NEXMO_APP_ID)

pm = ProductMatcher(NEXMO_APP_ID)
app = Flask(__name__)

@app.route('/inbound', methods=['POST'])
def inbound_message():
    print ("Inbound Message...")    
    data = request.get_json()
    user = data['from']['id']
    fb_sender = data['to']['id']
    in_msg = data['message']['content']['text']
    pm.product_matcher(fb_sender, user, in_msg)
    print("DEBUG: Return from Message sent.")
    return ("200")

@app.route('/status', methods=['POST'])
def message_status():
    print ("Message status:")    
    data = request.get_json()
    #pprint(data)
    return ("200")

if __name__ == '__main__':
    app.run(host="localhost", port=9000)
    
