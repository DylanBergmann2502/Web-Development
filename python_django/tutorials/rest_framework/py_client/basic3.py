import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint, json={"product_id": 123})

print(get_response.json()) # used to print JsonResponse(data), cant print text/html
# print(get_response.headers)
# print(get_response.text)