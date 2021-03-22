from algoritmos import cb, cbib, cbub, rnd
from KNNBasico import knnBasico
# import pandas as pd

from sklearn.model_selection import train_test_split


def AppAlgoritmos(algoritmo, data, testSize, vecinos, pr):

    df = data
    train, test = train_test_split(df, test_size=0.2, shuffle=False)

    # Obtener numero de usuarios,items y aspectos

    if algoritmo == 'cb':
        precision, recall = cb(train, test, pr)
        print('cb',precision,recall,'@',pr)
        return precision, recall

    elif algoritmo == 'cbib':
        precision, recall = cbib(train, test, vecinos, pr)
        print('cbib',precision,recall,'@',pr)
        
        return precision, recall

    elif algoritmo == 'cbub':
        precision, recall = cbub(train, test, vecinos, pr)
        print('cbub',precision,recall)
    
        return precision, recall

    elif algoritmo == 'knn-u':
        precision, recall = knnBasico(df, testSize, vecinos, pr,True)
        print('knn-u',precision,recall)
        return precision, recall
    
    elif algoritmo == 'knn-i':
        precision, recall = knnBasico(df, testSize, vecinos, pr, False)
        print('knn-i',precision,recall)
        return precision, recall
    
    elif algoritmo == 'rnd':
        precision, recall = rnd(train, pr)
        print('rnd',precision,recall)
        return precision, recall

        

    return 0, 0


'''DATASETS
yelp_hotels_aspects // YELP-HOT
yelp_beautySpa_aspects // YELP-SPA
yelp_restaurants_aspects10000 //YELP-RES
corpuscine_aspects_sabre_esol // MUCHOCINE SABRE
muchocine_lda_beto_fixedvalues //MUCHOCINE LDA

 '''