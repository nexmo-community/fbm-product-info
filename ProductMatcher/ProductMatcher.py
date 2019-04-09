from FBMClient.FBMClient import FBMClient

class ProductMatcher:

    auto_mode = True

    cats_dict = {
        'other': 'Our products: toys, food, meds, and bling',
        'toys': 'More info on cat toys here https://bit.ly/abc',
        'food': 'More info on cat food here https://bit.ly/def',
        'meds': 'More info on cat meds here https://bit.ly/ghi',
        'bling': 'More info on cat bling here https://bit.ly/jkl'
    }

    def __init__(self, nexmo_app_id):
        filename = "private.key"
        jwt_expiry = 1*60*60 # JWT expires after one hour (default is 15 minutes)
        self.fbm = FBMClient(nexmo_app_id, filename, jwt_expiry)
        return

    def product_matcher(self, fb_sender, user, msg):
        product = 'other'
        msg = msg.lower().strip()
        if self.auto_mode:
            if "auto: off" in msg:
                self.auto_mode = False
                self.fbm.send_message(fb_sender, user, "Auto mode is off")
                return
            for k in self.cats_dict.keys():
                if k in msg:
                    product = k
                    break
            self.fbm.send_message(fb_sender, user, self.cats_dict[product])
        if "auto: on" in msg:
                self.auto_mode = True
                self.fbm.send_message(fb_sender, user, "Auto mode is on")
        print("Product: %s" % product)
        return product
