import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL - ')
cnt = int(input('Enter count - '))
pos = int(input('Enter position - '))
print(url)
while cnt>0:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    url=tags[pos-1].get('href',None)
    print(url)
    cnt=cnt-1
