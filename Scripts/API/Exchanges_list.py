import requests
import json

url = "https://api.livecoinwatch.com/exchanges/list"

# coins_list = ['BTC', 'ETH', 'BNB', 'ADA', 'DOGE', 'SOL', 'USDT', 'TONCOIN', 'USDC', 'TRON', 'XRP']
# for coin in coins_list:
def exchanges(coin):  
    payload = json.dumps({
    "currency": coin,
    "sort": "volume",
    "order": "descending",
    "offset": 0,
    "limit": 5,
    "meta": True
    })
    headers = {
    'content-type': 'application/json',
    'x-api-key': 'b87e54da-43ab-4e05-97c4-5542199b6f23'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    res_body = json.loads(response.text)
    res_body.append(coin)
    return res_body

# coins_list = ['BTC', 'ETH', 'BNB', 'ADA', 'DOGE', 'SOL', 'USDT', 'TONCOIN', 'USDC', 'XRP']
# for coin in coins_list:
#     a = exchanges('BTC')
#     value = []
#     length = len(a)
#     for i in range (0,length):
#         value = a[i]
#         rem_list = ['png64', 'png128', 'webp64','webp128']
#         for key in rem_list:
#             if key in value:
#                 del value[key]
#         print("#####################################################")
#         print(value)
#     print("*************************************************************")