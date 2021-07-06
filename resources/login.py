import requests

def talegur_login(url, user, password):
    body = {"username": user, "password": password}
    headers = {"Content-type": "application/json", "Accept": "application/json"}
    resp = requests.post(url+"User/Login", json=body, headers=headers)
    auth = resp.json()
    token = auth["access_token"]
    return token