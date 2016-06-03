from two1.wallet import Wallet
from two1.bitrequests import BitTransferRequests

SERVER_IP_ADDRESS = '127.0.0.1'

# Configure your Bitcoin wallet.
wallet = Wallet()
requests = BitTransferRequests(wallet)


def send_email(email):
    print('You send {0}'.format(email))

    # 402 endpoint
    uri = 'http://'+SERVER_IP_ADDRESS+':5000/getgrav?email={0}'
    grav = requests.get(url=uri.format(email))

    print(grav.text)
    return grav.text

    
if __name__ == '__main__':
    from sys import argv
    send_email(argv[1])
        


    
