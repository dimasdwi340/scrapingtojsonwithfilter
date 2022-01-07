import requests
import json
import browser_cookie3

cookiejar = browser_cookie3.firefox(domain_name='instagram.com')
data = requests.get(f'https://www.instagram.com/dim.dimas/?__a=1', cookies = cookiejar).json()
def fun (data):
    if 'full_name' in data:
        yield data['full_name']
    for k in data:
        if isinstance(data[k], list): 
            for i in data[k]:
                for j in fun(i):
                    yield j


print (fun(data))

