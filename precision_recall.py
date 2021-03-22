
def precision_recall_at_k(predictions, usuario, data, n, threshold=4):

    goodItemsRecom = [] #Lista de recomendación
    for i, k in predictions:
        goodItemsRecom.append(i)
        
    goodItemsRecom = goodItemsRecom[:int(n)] #lista de items recomendados, cortando la recomendación
  
    
    # Lista de items relevantes
    userData = data[data['user_id'] == usuario]
    itemsRelevantes = userData[userData['rating'] >= threshold]['item_id']
    
    allGoodItems = []

    for i, k in itemsRelevantes.iteritems():
        allGoodItems.append(k)
   
    tp = 0
    tpfp = len(goodItemsRecom)  # lista de recomendacion
    tpfn = len(allGoodItems)  # lista relevante

    for i in goodItemsRecom:
        if i in allGoodItems:
            tp = tp + 1

    if tp == 0:
        precision = 0
        recall = 0
    
    else:
        precision = tp / tpfp
        recall = tp / tpfn
        
    print(precision,recall)
    


    return precision, recall

