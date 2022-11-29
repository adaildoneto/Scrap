from bs4 import BeautifulSoup as bs
import requests

for i in range(1,5): 
    if i == 1:
        url = "https://ac24horas.com/ultimas-noticias/"
        response  = requests.get(url)
    else:
        purl = "https://ac24horas.com/ultimas-noticias/page/"
        page = i - 1
        url = purl + str(page)
        response  = requests.get(url)
    print("Página :" + str(i))
    soup = bs (response.content, 'lxml')
    title = soup.find_all('li', class_="mvp-blog-story-wrap")
    
    for t in title:
        print('Categoria :' + t.find(class_="mvp-cd-cat").get_text(strip=True))
        
        try:
            img = t.find('img').get('src')
            print('Imagem :' + img)
        except AttributeError:
            print('Imagem não encontrada')  
            
        print('Título :' + t.find('h2').get_text(strip=True))
        conteudoUrl = t.find('a').get('href')
        contenido = requests.get(conteudoUrl)
        conteudoex = bs (contenido.content, 'lxml')
                
        try:
            aut = conteudoex.find('span', class_="author-name").get_text(strip=True)
            print('Autor :' + aut)
        except AttributeError:
            print('Autor não encontrado')
                
        print('Data :' + conteudoex.find('time', class_="post-date").get_text(strip=True))
        print('Texto completo :' + conteudoex.find("div", id="mvp-content-main").get_text(strip=True))
        print('Descrição:' + t.find('p').get_text(strip=True))
        print   ('--------------------')