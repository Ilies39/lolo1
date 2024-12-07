import re

def is_valid_username(username):
    return len(username) >= 3

def is_valid_password(password):
    return len(password) >= 6 and re.search(r'\d', password)  # ??? ?? ????? ??? ???
```