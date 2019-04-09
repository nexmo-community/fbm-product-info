from FBMClient.FBMClient import FBMClient

class ProductMatcher:

    cats_dict = {
        'none': 'Try `info: toys | food | meds | bling`',
        'toys': 'More info on cat toys here https://bit.ly/abc',
        'food': 'More info on cat food here https://bit.ly/def',
        'meds': 'More info on cat meds here https://bit.ly/ghi',
        'bling': 'More info on cat bling here https://bit.ly/jkl'
    }
    
    def __init__(nexmo_app_id):
        filename = "private.key"
        jwt_expiry = 1*60*60 # JWT expires after one hour (default is 15 minutes)
        self.fbm = FBMClient(nexmo_app_id, filename, jwt_expiry)
        return

    def product_matcher (fb_sender, user, msg):
        msg = msg.lower().strip()
        if "info:" not in msg:
            product = 'none' 
        else:
            msg = msg.split(':')[1]
            for k in cats_dict.items():
                if k in msg:
                    product = k
                    break
        fbm.send_message(fb_sender, user, cats_dict[product])
        return product    


