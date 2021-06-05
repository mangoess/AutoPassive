import requests
import time

time.sleep(Put your time in seconds here)
url = 'put the channel here!'
auth = 'put your token here!'
payload = {
    'content': "insert your command here!"
    }
header = {
    'authorization': auth
    }
r = requests.post(url,
                  data=payload, headers=header)
print("Task Done!")
