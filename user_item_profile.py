from collections import defaultdict
from AspectWeight import userAspectWeight, itemAspectWeight

# En estas funciones se configuran los perfiles de usuario e ítem


def userProfile( users, aspects, data ):

    dictUsers = defaultdict(list)
    for u in users:
        print(f'calculando perfil de usuario para {u}')
        vector = []
        for aspecto in aspects:
            
            weigth = userAspectWeight(u, aspecto, data)
            vector.append(weigth)  # añade la relevancia al array
        dictUsers[str(u)].append(vector)
    
    return dictUsers

def itemProfile( items, aspects, data ):
    
    dictItems = defaultdict(list)  # diccionario de items
    for i in items:
        
        print(f'calculando perfil de item para {i}')
        vector = []
        for aspecto in aspects:
            weight = itemAspectWeight(i, aspecto, data)
            vector.append(weight)  # añade w al array
        dictItems[str(i)].append(vector)
        
    return dictItems 



