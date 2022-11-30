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
pdata = ['Data', 'Titulo', 'Descricao', 'Url',]
ws1.append(pdata)

#criando a planilha Polícia
ws2 = wb.create_sheet(title="Polícia")
pdata = ['Data', 'Titulo', 'Descricao', 'Url',]
ws2.append(pdata)

#criando a planilha Covid
ws3 = wb.create_sheet(title="Covid")
pdata = ['Data', 'Titulo', 'Descricao', 'Url',]
ws3.append(pdata)

sites = ['http://ac24horas.com', 'http://contilnetnoticias.com.br', 'http://correio68.com','http://folhadoacre.com.br', 'http://yaconews.com',
'http://jornalopiniao.net', 'http://3dejulhonoticias.com.br', 'https://ecosdanoticia.net.br' ]

for i in range(0,8):
    url = (sites[i] + '/wp-json/wp/v2/posts')
    response = requests.get(url)

    data = response.text
    dados = json.loads(data)

    for j in dados:
        titulo = j['title']['rendered']
        descricao = j['content']['rendered']
        link = j['link']
        #img = j['jetpack_featured_media_url']
        data = j['date']

        #conteudo = item.find('content:encoded').text

        #estruturando o conteudo dentro da celula
        pdata = (data, titulo, descricao, link)

        #Criando uma nova planilha para a palavra chave Cameli
        if 'covid' in descricao:
           active_sheet = wb['Covid']
           ws3.append(pdata)

        # Criando uma nova planilha para a palavra chave Bocalom
        if 'polícia' in descricao:
           active_sheet = wb['Polícia']
           ws2.append(pdata)

        # ativando a planilha workbook
        ws1.append(pdata)

# Salvando o planilha
wb.save('thundera.xlsx')
