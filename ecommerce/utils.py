from datetime import datetime

def get_timestamp():
    unformatted_time = datetime_now()
    formatted_time = unformatted_time.striftime(%Y%m%d%H%M%S)

    return formatted_time
