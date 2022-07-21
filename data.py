import requests


parameters = {
    "amount": 10,
    "type": "boolean"
}

# Data Source
response = requests.get('https://opentdb.com/api.php', params=parameters)
response.raise_for_status()
data = response.json()
print(data)

response_code = data["response_code"]
question_data = data["results"]
