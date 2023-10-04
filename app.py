# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 13:13:53 2023

@author: Amir
"""

import requests
import json
import shutil # save img locally
import threading # save img locally

from pathlib import Path




data = requests.get('https://min-api.cryptocompare.com/data/all/coinlist')

a = data.text

b = json.loads(a)

threads = []
e =[]
c = 0

def download(url, i):
    res = requests.get(url, stream = True)
    if res.status_code == 200:
        with open('folder/'+i+'.png','wb') as f:
            shutil.copyfileobj(res.raw, f)
        print('Image sucessfully Downloaded: ','folder/'+i+'.png')
    else:
        print('Image Couldn\'t be retrieved')
        
        
for i in b['Data']:
    
    if(c > 1000):break
    try:
        print ( b['Data'][i]['ImageUrl'])
        url = 'https://www.cryptocompare.com/'+ b['Data'][i]['ImageUrl']
        
        my_file = Path('folder/'+i+'.png')
        if my_file.is_file():
            continue
        else:
            download(url, i)
            
        c +=1
        print(c)
        
    except:
        e.append(i) 
        
# for t in threads:
#     t.join()
        

    
        
        