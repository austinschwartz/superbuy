#!/usr/bin/env python3

import requests
import json

HEADERS = {
    'Origin': 'https://www.superbuy.com',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,es;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Mobile Safari/537.36',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'DNT': '1',
}

def get_parcels(cookies):
    params = (
        ('status', 'all'),
        ('page', '1'),
        ('pageSize', '10'),
        ('key', ''),
    )

    response = requests.get('https://front.superbuy.com/package/package/list', 
                            headers=HEADERS, 
                            params=params, 
                            cookies=cookies)
    if not response.ok:
        raise Exception(response.reason)
    return json.loads(response.content)

cookies = {
    # removed
}

parcels = get_parcels(cookies)
if parcels['msg'] == 'Success':
    for parcel in parcels['data']:
        print(parcel)
