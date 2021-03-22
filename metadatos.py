import pandas as pd
from userItemsAspects import getIUA

lda = pd.read_csv('./static/muchocine_lda_beto_fixedvalues.csv', header=0)
# sabre = pd.read_csv('./static/corpuscine_aspects_sabre_esol.csv', header=0)
sabre = pd.read_csv('./static/muchocine_lda_beto_fixedvalues.csv', header=0)
aspects = list(sabre.columns.values)
length = len(aspects)
aspects = aspects[3:length]


i= 3
suma= 0

print(0)
while i < length:
    suma = suma + sabre[sabre.columns[i]].count()
    i += 1
print('ASPECTOS / RATING')
print(suma/sabre[sabre.columns[2]].count())

print('')


items, users, aspects = getIUA(sabre)
print(len(items),len(users),len(aspects))
print('items',len(items))

print('')
print('RATINGS / USUARIO')
suma = 0
for u in users:
    usuario = sabre[sabre['user_id'] == u]
    ratings = usuario['rating'].count()
    suma = suma + ratings
    
print(suma/len(users))

print('')
print('RATINGS / ITEM')

suma = 0
for i in items:
    itemsFiltrados = sabre[sabre['item_id'] == i]
    ratings = itemsFiltrados['rating'].count()
    suma = suma + ratings
print(suma/len(items))
    




    

