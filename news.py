from bs4 import BeautifulSoup
import requests

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}

response = requests.get('https://www.reddit.com/r/NHKEasyNews/.rss', headers=headers)

with open('tmp.xml', 'w') as f:
    f.write(response.text)

with open('tmp.xml', 'r') as f:
    data = f.read()


Bs_data = BeautifulSoup(data, "xml")

titles = Bs_data.find_all('title')

del titles[0:2]

for t in titles:
    print(t.get_text())
    print('\n')
