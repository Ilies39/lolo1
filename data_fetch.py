import requests

def login_to_line bet(username, password):
    url = "https://1xbet.com/ar/allgamesentrance/crash"  # ???? ????? ?????? ??????
    payload = {
        'username': username,
        'password': password
    }
    
    # ????? ??? POST ?????? ??????
    response = requests.post(url, data=payload)
    
    if response.ok:  # ???? ?? ???? ?????
        return response.cookies  # ???? ??????? ??????
    else:
        return None  # ???? None ??? ??? ????? ??????

def fetch_data(session):
    # ?????? ?????? ???? ???????? ?? ??????
    url = "https://1xbet.com/ar/allgamesentrance/crash"  # ????? ????? ??? ?????? ??? ??????
    response = requests.get(url, cookies=session)
    
    if response.ok:
        return response.json()  # ???? ???????? ????????
    return {}
```
