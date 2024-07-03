import requests
import json

url = "https://api.livecoinwatch.com/coins/list"

payload = json.dumps({
  "currency": "USD",
  "sort": "rank",
  "order": "ascending",
  "offset": 0,
  "limit": 2,
  "meta": True
})
headers = {
  'content-type': 'application/json',
  'x-api-key': '6f4cbfe9-63ea-467c-b35a-3a4e646fc980'
}

response = requests.request("POST", url, headers=headers, data=payload)
msg = json.loads(response.text)
print(msg)

# for message in msg:
#     rem_list = ['symbol', 'rank', 'color', 'png32', 'png64','webp32', 'webp64', 'pairs', 'categories', 'links']
#     for key in rem_list:
#         del message[key]
# print(message)

# import requests
# import json

# url = "https://api.livecoinwatch.com/exchanges/list"

# payload = json.dumps({
#   "currency": "USD",
#   "sort": "volume",
#   "order": "descending",
#   "offset": 0,
#   "limit": 1,
#   "meta": True
# })
# headers = {
#   'content-type': 'application/json',
#   'x-api-key': '6f4cbfe9-63ea-467c-b35a-3a4e646fc980'
# }

# response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)