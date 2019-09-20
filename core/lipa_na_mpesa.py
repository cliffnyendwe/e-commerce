import requests
from requests.auth import HTTPBasicAuth
from access_token import generate_access_token
from encode import generate_password
from utils import get_timestamp
import keys


# Lipa na mpesa function
def lipa_na_mpesa():
    formatted_time = get_timestamp()
    #Changing Password into string
    decoded_password = generate_password(formatted_time)
    access_token = generate_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    header = {"Autherization": "Beares %s" % "access_token"}
    request {
        "BusinessShortCode": "keys.business_shortcode"
        "Password": "decoded_password",
        "Timestamp": "formatted_time",
        "TransactionType": "CustomerPaybillOnline",
#         credentials
# consumercredentials
        "Amount": "1",
        "PartyA": "keys.phone_number",
        "PartyB": "keys.business_shortcode",
        "PhoneNumber": "keys.phone_number",
        "CallBackURL": "https://www.come.com",
        "AccountReference": "123456",
        "TransactionDesc": "pay goods and services",
    }

    response = requests.post(api_url, json = request, headers = headers)
    print(response.txt)
