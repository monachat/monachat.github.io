#!/usr/bin/env python3

import urllib.request
from bs4 import BeautifulSoup

urls = [
    'entrance',
    '''
    'main',
    'area',
    'theme',
    'crisscross',
    'wide',
    'large',
    'pulloff1',
    'pulloff2',
    'lab',
    'monachat.dyndns.org/monachatfb.html',
    'chat.moja.jp/animal.html',
    'cool.moja.jp',
    'cool.moja.jp/kanpu.html','''
]

for url in urls:
    if '.' in url:
        url = f'http://{url}'
    else:
        url = f'http://monachat.dyndns.org/monachat_{url}.html'

    content = urllib.request.urlopen(url).read().decode('cp932')
    soup = BeautifulSoup(content, 'html.parser')
    print(soup.prettify())
