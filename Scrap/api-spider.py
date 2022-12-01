from bs4 import BeautifulSoup as bs
import requests
import json
from openpyxl import Workbook, load_workbook
# If you need to get the column letter, also import this
from openpyxl.utils import get_column_letter

# criando a planilha workbook
wb = Workbook()

# ativando a planilha workbook
ws1 = wb.active

# Renomeando a planilha workbook geral
ws1.title = 'Olho de Thundera'

#criando a primeira linha da tabela para servir de guia
pdata = ['Data', 'Titulo', 'Descricao', 'Url','Imagem']
ws1.append(pdata)

#criando a planilha Polícia
ws2 = wb.create_sheet(title="Polícia")
pdata = ['Data', 'Titulo', 'Descricao', 'Url','Imagem']
ws2.append(pdata)

#criando a planilha Covid
ws3 = wb.create_sheet(title="Covid")
pdata = ['Data', 'Titulo', 'Descricao', 'Url','Imagem']
ws3.append(pdata)

sites = ['http://ac24horas.com', 'http://contilnetnoticias.com.br', 'http://correio68.com',
'http://folhadoacre.com.br', 'http://yaconews.com', 'http://jornalopiniao.net', 'http://3dejulhonoticias.com.br', 
'https://ecosdanoticia.net.br', 'https://agazetadoacre.com', 'https://www.acre.com.br', 'https://acreagora.com', 
'https://oaltoacre.com', 'https://agazeta.net', 'http://noticiasdahora.com.br',  'https://oacreagora.com', ]

jnews = len (sites)

for i in range (jnews):
    turl = (sites[i] + '/wp-json/wp/v2/posts')
    response = requests.get(turl)

    data = response.text
    
    if response.status_code == 200:  
      print('site ' + turl + ' ok!')
      dados = json.loads(data)
      for j in dados:
         titulo = j['title']['rendered']
         descricao = j['content']['rendered']
         link = j['link']
         
         try:
          img = j['jetpack_featured_media_url']
         except KeyError:
          img = 'Imagem não encontrada'        
         
         data = j['date']

         #estruturando o conteudo dentro da celula
         pdata = (data, titulo, descricao, link, img)

         #Criando uma nova planilha para a palavra chave Cameli
         if 'covid' in titulo:
            active_sheet = wb['Covid']
            ws3.append(pdata)

         # Criando uma nova planilha para a palavra chave Bocalom
         if 'polícia' in descricao:
            active_sheet = wb['Polícia']
            ws2.append(pdata)

         # ativando a planilha workbook
         ws1.append(pdata)
    else:
      print('site ' + turl + ' não habilitado para o json')

# Salvando o planilha
wb.save('thundera.xlsx')
