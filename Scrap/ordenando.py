# import pandas lib as pd
import pandas as pd
 
# read by default 1st sheet of an excel file
df1 = pd.read_excel('theeye.xlsx')

# checking datatype
print(type(df1.Data[0]))
 
# convert to date
#df1['Data'] = df1['Data'].apply(pd.to_datetime)

#df1['Data'] = pd.to_datetime(df1['Data'], format='%Y-%m-%d')


# verify datatype
print(type(df1.Data[0]))

ok = df1.sort_values(by=['Data', 'Hora'])

ok.to_json(r'ordenado.json')

ok.to_excel("ordenado.xlsx")  