import requests
from requests.auth import HTTPBasicAuth
import keys

def generate_access_token():
    consumer_key = keys.consumer_key
    consumer_secret = keys.consumer_secret
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/generate?grant_type=client_credentials"
    r=requests.get(api_url, auth=HTTPBasicAuth(consumer_key, consumer_key))
    json_response = (r.json())
    my_access_token = json_response["access_token"]
    return my_access_token
