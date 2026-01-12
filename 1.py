# packeges : they are predefined codes that we can import to use in our code
import requests

response = requests.get('https://api.github.com')
print(response.status_code)  # to check the status of the response

print(requests.__version__)  # to check the version of the package