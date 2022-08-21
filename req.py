import requests

x = requests.post(url='http://localhost/',json={"name":"a"})
print(x.text)
