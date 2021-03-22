import pickle
import operator
import random
from sklearn.metrics.pairwise import cosine_similarity


# Perfiles de item y usuario
from userItemsAspects import getIUA
from user_item_profile import userProfile, itemProfile

# Algoritmos
from cercanos import itemsCercanos, usuariosCercanos

# Métricas de Precision y Recall (PR)
from promedioPR import promedioPR



def cb(train, test, pr):  # cb


    # obtiene los usuarios e items del dataFrame
    items, users, aspects = getIUA(train)
    perfilItems = itemProfile(items, aspects, train)
    perfilUsuarios = userProfile(users, aspects, train)

    print('Saliendo de perfiles de usuario')

    recom = {}

    for u in perfilUsuarios:
        recom[u] = dict()
        print(f'usuario : {u}')
        for i in perfilItems:
            sim = cosine_similarity(perfilUsuarios[u], perfilItems[i])
            recom[u][i] = round(sim[0][0], 4)

        recom[u] = sorted(recom[u].items(),
                          key=operator.itemgetter(1), reverse=True)

    # with open('./pkl/cb_MUCHOCINE-LDA.pkl','wb') as pickle_file:
    #     pickle.dump(recom,pickle_file)

    # with open('./pkl/cb_MUCHOCINE-LDA.pkl','rb') as pickle_file:
    #       recom= pickle.load(pickle_file)

    avgPrecision, avgRecall = promedioPR(pr, recom, train)

    return avgPrecision, avgRecall


def cbib(train, test, vecinos, pr):

    items, users, aspects = getIUA(train)
    perfilItems = itemProfile(items, aspects, train)
    itemsVecinos = itemsCercanos(perfilItems)

    recom = {}

    for u in users:
        recom[u] = {}
        userData = train[train['user_id'] == u]  # para encontrar el rating
        for i in itemsVecinos:
            sumatoria = 0
            count = 0
            for k, valorSim in itemsVecinos[i]:
                if count > vecinos:
                    break
                else:
                    itemData = userData[userData['item_id'] == k]
                    rating = itemData['rating'].sum()
                    sumatoria = (rating * valorSim) + sumatoria
                    count += 1
            recom[u][i] = sumatoria
        recom[u] = sorted(recom[u].items(),
                          key=operator.itemgetter(1), reverse=True)

    # CARGANDO RECOMENDACIONES CON PICKLE

    # print('guardando recomendaciones...')
    # with open('./pkl/cbib_SPA.pkl','wb') as pickle_file:
    #     pickle.dump(recom,pickle_file)

    # with open('./pkl/cbib_SPA.pkl','rb') as pickle_file:
    #     recom= pickle.load(pickle_file)


    avgPrecision, avgRecall = promedioPR(pr, recom, train)

    return avgPrecision, avgRecall


def cbub(train, testset,vecinos, pr):
    
    
    items, users, aspects = getIUA(train)
    
    perfilUsuarios = userProfile(users, aspects, train)
    
    usuariosVecinos = usuariosCercanos(perfilUsuarios)
    
    recom = {}
    
    tiempo = 0
    for u in usuariosVecinos:
        tiempo = tiempo + 1
        print(len(users), len(users)- tiempo)
        recom[u] = {}
        for i in items:
            sumatoria = 0
            count = 0
            for z, valorSim in usuariosVecinos[u]:
                if count > vecinos:
                    break
                else:
                    userData = train[train['user_id'] == z]
                    itemData = userData[userData['item_id'] == i]
                    rating = itemData['rating'].sum()
                    sumatoria = (rating * valorSim) + sumatoria
                    count += 1
            recom[u][i] = sumatoria
        recom[u] = sorted(recom[u].items(),
                          key=operator.itemgetter(1), reverse=True)

    # print('guardando recomendaciones...')
    # with open('./pkl/cbub_MUCHOCINE-LDA.pkl','wb') as pickle_file:
    #     pickle.dump(recom,pickle_file)

    # with open('./pkl/cbub_MUCHOCINE-LDA.pkl','rb') as pickle_file:
    #     recom= pickle.load(pickle_file)

    avgPrecision, avgRecall = promedioPR(pr, recom, train)

    return avgPrecision, avgRecall

def rnd(train, pr):
    
    items, users, aspects = getIUA(train);
    recom = {}
    
    for u in users:
        recom[u] = {}
        for i in items:
            recom[u][i] = random.randrange(1,5)
        recom[u] = sorted(recom[u].items(),key=operator.itemgetter(1), reverse=True)
    
    
    avgPrecision, avgRecall = promedioPR(pr, recom, train)
    
    return avgPrecision,avgRecall
