from pprint import pprint
from bs4 import BeautifulSoup as bs
import requests
import openpyxl

def new_func():
    url = "https://ac24horas.com/ultimas-noticias/"
    return url

url = new_func()     

response  = requests.get(url)
pprint(response.status_code)
soup = bs (response.content, 'lxml')
title = soup.find_all('li', class_="mvp-blog-story-wrap")
for t in title:
    print('Categoria :' + t.find(class_="mvp-cd-cat").get_text(strip=True))
    print('imagem :' + t.find('img').get('src'))
    print('Título :' + t.find('h2').get_text(strip=True))
    print('link :' + t.find('a').get('href'))
    conteudoUrl = t.find('a').get('href')
    contenido = requests.get(conteudoUrl)
    conteudoex = bs (contenido.content, 'lxml')
    print('Autor :' + conteudoex.find('span', class_="author-name").get_text(strip=True))
    print('Data :' + conteudoex.find('time', class_="post-date").get_text(strip=True))
    print('Texto completo :' + conteudoex.find("div", id="mvp-content-main").get_text(strip=True))
    print('Descrição:' + t.find('p').get_text(strip=True))
    print('--------------------')