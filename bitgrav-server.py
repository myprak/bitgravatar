import hashlib

from flask import Flask
from flask import request

from two1.wallet import Wallet
from two1.bitserv.flask import Payment

# Configure the app and wallet
app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)

@app.route('/getgrav')
@payment.required(1)
def getgrav():
    raw_email = str(request.args.get('email'))
    print(raw_email)
    clean_email = raw_email.encode('utf-8').strip().lower()
    print(clean_email)
    email_md5 = hashlib.md5()
    email_md5.update(clean_email)
    email_hash = email_md5.hexdigest()
    uri = 'https://secure.gravatar.com/avatar/'
    return(uri+email_hash)

# Initialize and run the server
if __name__ == '__main__':
    app.run(host='0.0.0.0')
    
    
    

