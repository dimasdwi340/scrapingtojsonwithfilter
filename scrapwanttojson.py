import requests 
import browser_cookie3
import time, json

def get_account (username_list):

    cookiejar = browser_cookie3.firefox(domain_name='instagram.com')
    for username in username_list:
        scrape = requests.get(f'https://www.instagram.com/{username}/?__a=1', cookies=cookiejar).json()
        with open(f'dataset/{username}.json', 'w') as g:
            json.dump([scrape], g)
        time.sleep(2)
        print ('done')
    


#requests.get(f'https://www.instagram.com/{username}/?__a=1', cookies=cookiejar).json()
#m = requests.get(f'https://www.instagram.com/dim.dimas/?__a=1', cookies = cookiejar).json()
   
#print (m)