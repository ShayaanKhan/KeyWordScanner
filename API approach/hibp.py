import requests
import os

# Replace 'YOUR_API_KEY' with your actual API key
API_KEY = os.getenv('hibpToken')

def get_pwned_data(email):
    url = f'https://haveibeenpwned.com/api/v3/breachedaccount/{email}'
    headers = {'hibp-api-key': API_KEY}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        return f'No breaches found for {email}.'
    else:
        return f'Error: {response.status_code}'

email = 'example@example.com'
result = get_pwned_data(email)
print(result)
