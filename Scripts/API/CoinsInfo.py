import requests
import json
import time



def coin_info(i):
    while(i<1):
        url = "https://api.livecoinwatch.com/coins/single"

        payload = json.dumps({
        "currency": "USD",
        "code": "BTC",
        "meta": True
        })

        headers = {
        'content-type': 'application/json',
        'x-api-key': '6f4cbfe9-63ea-467c-b35a-3a4e646fc980'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        res_body = json.loads(response.text)
        print(res_body)
        i = i+1
        return res_body
    