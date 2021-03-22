
#tenemos que tener la recomendacion y el test para hacer la comparación
import math

def RMSE(recom, testSet):

    df = testSet
    testSet = testSet.iloc[:, 0:3]
    suma = 0
    suma2 = 0
    count = 0
    
    for i in df.index:
        
        usuario = df['user_id'][i]
        item = df['item_id'][i]
        r = df['rating'][i]
        for u in recom:
            for i,v in recom[u]:
                if(i == item) and (u == usuario):
                    num = r - v
                    suma = suma + pow(num,2)
                    suma2 = suma2 + abs(num)
                    count += 1
    if count == 0:
        return 0,0
    else:
        div = suma / count
        MAE = round(suma2 / count,3)
        RMSE = round( math.sqrt(div),3)


        return RMSE, MAE
    
    

