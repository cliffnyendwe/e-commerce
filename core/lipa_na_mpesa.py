import base64
import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime
import keys

unformatted_time = datetime_now()
formatted_time = unformatted_time.striftime(%Y%m%d%H%M%S)

# This Password
data_to_encode = keys.business_shortcode + keys.lipa_na_mpesa_passkey + formatted_time
encoded = base64.b64encoded(data_to_encode.encode())

#Changing Password into string again
decoded_password = encoded.sting.decode("utf-8")
credentialscredentials
consumer_key = "keys
consumer_key = "keys
# Authentication credentials
consumer_key = "keys.consumer_key"
secret_key = "keys.secret_key"
api_url = ("httcredentials
consumer_key = "keyscredentials
consumer_key = "keyscredentials
consumer_key = "keysps://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials")
r = requests.get(api_url, auth = HTTPBasicAuth(consumer_key, consumer_secret))

#Returning the response in a json formatted_time
json_response = r.json()
my_access_token = json_response("access_token")
# Lipa na mpesa function
def lipa_na_mpesa():
    access_token = "my_access_token"
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    header = {"Autherization": "Beares %s" % "access_token"}
    request {
        "BusinessShortCode": "keys.business_shortcode";
        "Password": "decoded_password",
        "Timestamp": "formatted_time",
        "TransactionType": "CustomerPaybillOnline",
        credentials
consumercredentials
consumer_key = "keys_key = "keys"Amount": "1",
        "PartyA": "keys.phone_number",
        "PartyB": "keys.business_shortcode",
        "PhoneNumber": "keys.phone_number",
        "CallBackURL": "https://www.come.com",
        "AccountReference": "123456",
        "TransactionDesc": "pay goods and services",
    }

    response = requests.post(api_url, json = request, headers = headers)
    print(response.txt)
