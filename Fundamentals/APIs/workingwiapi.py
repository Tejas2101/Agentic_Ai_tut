import requests
import json

response = requests.get('http://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow')

print(response) # prints <Response [200]>
print(response.json()) # output similar to postman (All the data)

print(response.json()['items']) # we will get list of items

for data in response.json()['items']:
    print(data['title'])
    print(data['link'])

