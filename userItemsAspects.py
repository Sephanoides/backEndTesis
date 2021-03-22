"""
@author: Lincoln Hugo Smith Apolonio

Funciones base de los algoritmos

"""


def getIUA( data ):

    items = []
    users = []

    for index, fila in data.iterrows():
        #print('obteniendo items y usuarios')
        if not fila['item_id'] in items:
            items.append(fila['item_id'])
        if not fila['user_id'] in users:
            users.append(fila['user_id'])
    
    aspects = list(data.columns.values)
    length = len(aspects)
    aspects = aspects[3:length]
            

    return items, users, aspects




