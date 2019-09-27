import requests
import keys
from access_token import generate_access_token

#Register URL function
def register_url():
    my_access_token = generate_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    header = {"Autherization": "Beares %s" % "my_access_token"}

    requests {
        "ShortCode": "keys.shortcode",
        "ResponseType": "completed",
        "ConfirmationURL": "https://localhost:8000",
        "ValidationURL": "https://localhost:8000"
    }

    response = requests.post(api_url, json=request, headers=headers)
    print(response.text)

# register_url()

def simulate_c2b_transaction():
    my_access_token = generate_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
    header = {"Autherization": "Beares %s" % "my_access_token"}

    request{
        "ShortCode":"keys.shortcode",
        "CommandID":"CustomerPaybillOnline",
        "Amount":"",
        "Msisdn":"keys.msisdn",
        "BillRefNumber":"123456",
    }

    response = requests.post(api_url, json=request, headers=headers)
    print(response.text)
