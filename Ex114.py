#Ex. Crie um programa que verifique se o site Pudim está disponível.

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O Site não está disponível no momento.')
else:
    print('Consegui acessar o site normalmente.')