import requests
import json

import pysnowball.cons as cons
import pysnowball.token as token

def fetch(url):
    # HEADERS = {'Accept': 'application/json',
    #            'Accept-Encoding': 'br, gzip, deflate',
    #            'Cookie': token.get_token(),
    #            'Accept-Language': 'zh-Hans-CN;q=1, ja-JP;q=0.9',
    #            'Connection': 'keep-alive'}

    HEADERS = {'Cookie': token.get_token()}

    response = requests.get(url,headers=HEADERS)

    print(url)
    print(HEADERS)
    print(response)
    print(response.content)

    if response.status_code != 200:
        raise Exception(cons.NOT200_ERROR_MSG)

    return json.loads(response.content)
