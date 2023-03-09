import requests
from bs4 import BeautifulSoup

url = 'https://www.idnfinancials.com/id/pack'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
# print(soup.prettify())

# for tma in soup.find_all('div', {'class': 'tma-item'}):
    # print(tma.find('strong').text + " : " + tma.find('span').text)
gfg = soup.find_all(lambda tag: tag.name == "script" and 'var app' in tag.text)

txt_main_script = gfg[0]

txt_main_script = txt_main_script.text
fx = txt_main_script.find("var app")
txt_main_script = txt_main_script[fx:50].split(":")[1].strip()
txt_main_script = ''.join(filter(str.isalnum, txt_main_script))
print(txt_main_script)