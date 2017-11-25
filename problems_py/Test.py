#ссылки на все когда либо решаемые задачки при вводе хендла
import requests
from bs4 import BeautifulSoup

username = str(input())
url = 'http://codeforces.com/submissions/' + username
r = requests.get(url)
max_page = 0
soup = BeautifulSoup(r.text, "lxml")

for link in soup.find_all(attrs={"class" : "page-index"}):
    s = link.find('a')
    s2 = s.get("href").split('/')
    max_page = max(max_page, int(s2[4]))
	
a = set()

for i in range(0, max_page):
    r = requests.get('http://codeforces.com/submissions/' + username + '/page/' + str(i))
    soup = BeautifulSoup(r.text, "lxml")

    for link in soup.find_all('a'):
        s = link.get('href')
        if  s != None and len(s) > 12 and s.find('/problemset') != -1:
            a.add('http://codeforces.com' + s)
			
with open('test.txt', 'w', encoding = 'utf-8') as output:                
    for i in a:
        output.write(i + '\n')