
# En estas fucniones se calcula la relevancia de los aspectos para los usuarios e ítem

def itemAspectWeight(item, aspect, data):

    # retorna un dataFrame con el item buscado
    itemFiltered = data[data['item_id'] == item]
    itemFiltered = itemFiltered[itemFiltered[aspect] != 'NULL']
    
    # Suma todas las polaridades de cada tupla (item1,aspecto1)

    suma = itemFiltered[aspect].sum()
    count = itemFiltered[aspect].count()  # cuenta la cantidad de polaridades

    if count == 0:
        return 0
    else:
        
        average = suma / count
        return round(average,4)


def userAspectWeight(user, aspect, data):

    userFiltered = data[data['user_id'] == user]
    userFiltered = userFiltered[userFiltered[aspect] != 'NULL']

    suma = userFiltered[aspect].sum()
    count = userFiltered[aspect].count()

    if count == 0:
        return 0
    else:
        average = suma/count
        return round(average,4)
