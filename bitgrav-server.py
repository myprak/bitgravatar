import hashlib
import json
import yaml

from flask import Flask
from flask import request

from two1.wallet import Wallet
from two1.bitserv.flask import Payment

# Configure the app and wallet
app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)


@app.route('/manifest')
def manifest():
    """Provide the app manifest to the 21 crawler. """
    with open('./manifest.yaml', 'r') as f:
        manifest = yaml.load(f)
    return json.dumps(manifest)


@app.route('/')
@payment.required(1)
def getgrav():
    """ Takes an email address and calculates an md5 hash on that
         email address, then adds the gravatar uri and returns both
         the email address and the gravatar url for the image of 
         said gravatar. Note that even if gravatar does not have 
         the image for the hash, gravatar will still provide one 
         of the defaults"""

    raw_email = str(request.args.get('email'))
    print(raw_email)
    clean_email = raw_email.encode('utf-8').strip().lower()
    print(clean_email)
    email_md5 = hashlib.md5()
    email_md5.update(clean_email)
    email_hash = email_md5.hexdigest()
    uri = 'https://secure.gravatar.com/avatar/'
    output = json.dumps({
        "email": clean_email.decode("utf-8"),
        "url": uri+email_hash
    })
    return output


# Initialize and run the server
if __name__ == '__main__':
    app.run(host='0.0.0.0')
    
    
    

