import requests
import json



url = "https://api.livecoinwatch.com/credits"

payload={}
headers = {
  'content-type': 'application/json',
  'x-api-key': '6f4cbfe9-63ea-467c-b35a-3a4e646fc980'
}

response = requests.request("POST", url, headers=headers, data=payload)

res_body = json.loads(response.text)
credits_remaining = res_body['dailyCreditsRemaining']
credits_limit = res_body['dailyCreditsLimit']
print(credits_remaining)
print(credits_limit)