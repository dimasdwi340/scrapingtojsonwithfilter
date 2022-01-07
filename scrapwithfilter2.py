import requests
import json
import browser_cookie3

cookiejar = browser_cookie3.firefox(domain_name='instagram.com')
data = requests.get(f'https://www.instagram.com/dim.dimas/?__a=1', cookies = cookiejar).json()

# generator for extracting values in dictionary
def gen_dict_extract(key, var):
    if isinstance(var, dict):
        if hasattr(var,'items'):
            for k, v in var.items():
                if k == key:
                    yield v
                if isinstance(v, dict):
                    for result in gen_dict_extract(key, v):
                        yield result
                elif isinstance(v, list):
                    for d in v:
                        for result in gen_dict_extract(key, d):
                            yield result
    elif isinstance(var, list):
        for item in var:
            for result in gen_dict_extract(key, item):
                yield result

def scraping_instagram(username):
    cookiejar = browser_cookie3.firefox(domain_name='instagram.com')
    data = requests.get(f'https://www.instagram.com/{username}/?__a=1', cookies = cookiejar).json()
    if not data:
        return
    uname = next(gen_dict_extract('owner',data),{}).get('username')
    if not uname:
        return

    #filtering
    captions = gen_dict_extract('text',data)
    doc = dict(
        username = uname,
        post_count = next(gen_dict_extract('edge_owner_to_timeline_media',data)).get('count'),
        follower = next(gen_dict_extract('edge_followed_by',data)).get('count'),
        following = next(gen_dict_extract('edge_follow',data)).get('count'),
        category_name = next(gen_dict_extract('category_name',data)),
        biography = next(gen_dict_extract('biography',data)),
        captions = [next(captions),
            next(captions),
            next(captions),
            next(captions),
            next(captions),
            next(captions),
            next(captions),
            next(captions),
            next(captions)]
    )

    #dump to json file
    with open(f'dataset2/{username}.json', 'w') as g:
            json.dump([doc], g)
    if doc: #if success
        return True



