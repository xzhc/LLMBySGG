"""
This case demonstrates fetching Hitokoto(quote) information by sending a http request
"""

import requests

#The API address for Hitokoto
url = 'https://international.v1.hitokoto.cn'

#Request parameters:Special content type(e.g., 'a'for Animation) and format
params = {
    'c': 'a', # 'a' represents Animation, 'b' represents Comic, etc.
    'encode': 'json'
}

try:
    print(f'Sending GET request to {url},, params: {params}')
    response = requests.get(url, params=params)
    status_code = response.status_code

    if status_code == 200:
        print(f'Request successful! Status code: {status_code}')
        data = response.json()
        #Extract the quote and author/source
        hitokoto = data['hitokoto']
        from_who = data['from_who'] if data['from_who'] else 'Unknown'
        print(f'Random quote: {hitokoto} - {from_who}')

    elif status_code == 404:
        print(f'Request failed. Status code: {status_code}')
    elif status_code == 500:
        print(f'Server error. Status code: {status_code}')
    else:
        print(f'Unexpected status code: {status_code}')
except requests.exceptions.RequestException as e:
    print(f'An error occurred: {e}')