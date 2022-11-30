import pprint
from bs4 import BeautifulSoup as bs
import requests
from openpyxl import Workbook, load_workbook
# If you need to get the column letter, also import this
from openpyxl.utils import get_column_letter

# criando a planilha workbook
wb = Workbook()

# ativando a planilha workbook
ws1 = wb.active

# Renomeando a planilha workbook geral
ws1.title = 'Olho de Sauron'

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

for i in range (0,8): 
    url = (sites[i] + '/feed')
    response = requests.get(url)
    soup = bs (response.content, features='xml')
    items = soup.find_all('item')
    print(url)
    for item in items :
        titulo = item.find('title').text
        data = item.find('pubDate').text
        #autor = item.find('dc:creator').text
        descricao = item.find('description').text
        url = item.find('link').text
        #conteudo = item.find('content:encoded').text

        #estruturando o conteudo dentro da celula
        pdata = (data, titulo, descricao, url)
        
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
wb.save('olhodesauron.xlsx')