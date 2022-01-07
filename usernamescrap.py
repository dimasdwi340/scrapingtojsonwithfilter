from scrapwanttojson import get_account
from scrapwithfilter2 import scraping_instagram
import time

username_list = ['Gypsea_Lust',
    'Loki the Wolfdog',
    'TaraMilkTea',
    'DoYouTravel',
    'Spiritedpursuit',
    'Calsnape',
    'NoBackHome',
    'FunForLouis',
    'Aniab',
    'Benjaminortega',
    'Grainedevoyageuse',
    'Muradosmann',
    'ChrisBurkard',
    'Izkiz',
    'Tuulavintage',
    'TheBucketListFamily',
    'Mialvess',
    'JamesRelfdyer',
    'Emitoms',
    'Mr.Pokee',
    'LucyLaucht',
    'Worldwanderlust',
    'Morganphillips',
    'Asasteinars',
    'TheSlowTraveler',
    'Alexstrohl',
    'CarleysCamera',
    'BeMyTravelMuse',
    'FreyaDowson']
    
# get_account(username_list)

#new scrap method
for username in username_list:
    success = scraping_instagram(username)
    if success:
        print(username, '...ok')
    else:
        print(username, '...failed')

    time.sleep(2)

