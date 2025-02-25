import requests
import password

user = password.user
password = password.password

r = requests.get("http://127.0.0.1:80/basic-auth/awclemen/password", auth=(user, password))

print(r.status_code)
print(r.headers)
print(r.text)
