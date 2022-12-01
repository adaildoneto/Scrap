
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
pdata = ['Data','Titulo', 'Conteúdo', 'Url', 'Imagem']
ws1.append(pdata)

#criando a planilha Polícia
ws2 = wb.create_sheet(title="Polícia")
ws2.append(pdata)

#criando a planilha Covid
ws3 = wb.create_sheet(title="Covid")
ws3.append(pdata)

sites = ['http://ac24horas.com', 'http://contilnetnoticias.com.br', 
'http://folhadoacre.com.br', 'http://yaconews.com', 'http://jornalopiniao.net', 'http://3dejulhonoticias.com.br', 
'http://ecosdanoticia.net.br', 'http://agazetadoacre.com', 'http://www.acre.com.br', 'http://acreagora.com', 
'http://oaltoacre.com', 'http://agazeta.net', 'http://noticiasdahora.com.br',  'http://oacreagora.com', ]

jnews = len (sites)

for i in range (jnews):
    turl = (sites[i] + '/wp-json/wp/v2/search/?subtype=post&search=Cameli')
    response = requests.get(turl)

    data = response.text
    
    if response.status_code == 200:  
      print('site ' + turl + ' ok!')
      dados = json.loads(data)
      for j in dados:
         titulo = j['title']
         link = j['url']
         
         id_ = str(j['id'])
        
         pturl = (sites[i] + '/wp-json/wp/v2/posts/' + id_)
         response = requests.get(pturl)
         artigo = response.text
         data_json = json.loads(artigo)
         k = data_json
         try:
            cdata = k['date']
         except KeyError:
            cdata = 'Data desconhecida'
         try:
            content = k['content']['rendered']
         except KeyError:
            content = 'Não encontrado'
         try:
             img = k['jetpack_featured_media_url']
         except AttributeError:
             turl = (sites[i] + '/wp-json/wp/v2/media/' + id_)
             response = requests.get(turl)
             imagem = response.text
             i_json = json.loads(imagem)
             img = i_json['source_url']
         except KeyError:
             img = ('Imagem não encontrada')
         
         #estruturando o conteudo dentro da celula
         pdata = (cdata, titulo, content, link, img )

         #Criando uma nova planilha para a palavra chave Cameli
         if 'covid' in titulo:
            active_sheet = wb['Covid']
            ws3.append(pdata)

         # Criando uma nova planilha para a palavra chave Bocalom
         if 'ptolomeu' in link:
            active_sheet = wb['Polícia']
            ws2.append(pdata)

         # ativando a planilha workbook
         ws1.append(pdata)
    else:
      print('site ' + turl + ' não habilitado para o json')

# Salvando o planilha
wb.save('theeye.xlsx')
