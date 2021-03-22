from precision_recall import precision_recall_at_k


def promedioPR( largoRecom, recomendaciones, data ):
    
    v_precision = []
    v_recall = []
   
    for usuario in recomendaciones:

        precision, recall = precision_recall_at_k(recomendaciones[usuario], usuario, data, largoRecom)
        v_precision.append(precision)
        v_recall.append(recall)

    sumaP = 0
    sumaR = 0

    for j in v_precision:
        
        sumaP  = sumaP + j
 
    for k in v_recall:
        
        sumaR = sumaR + k
        
    avgPrecision = round(sumaP / len(v_precision), 3)
    avgRecall = round(sumaR / len(v_recall), 3)
    
 

    return  avgPrecision, avgRecall   
