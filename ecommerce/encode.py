import keys
import base64


def generate_password():
    data_to_encode = keys.business_shortcode + keys.lipa_na_mpesa_passkey + formatted_time
    encoded = base64.b64encoded(data_to_encode.encode())

    #Changing Password into string
    decoded_password = encoded.sting.decode("utf-8")
    return decoded_password
