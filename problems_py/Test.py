#ссылки на все задачки на первой странице попыток
import requests
from bs4 import BeautifulSoup
url = 'http://codeforces.com/submissions/NyanCake'
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
with open('test.txt', 'w', encoding = 'utf-8') as output:
    for link in soup.find_all('a'):
        s = link.get('href')
        if  s != None and len(s) > 12 and s.find('/problemset') != -1:
            output.write('http://codeforces.com' + s)
            output.write('\n')