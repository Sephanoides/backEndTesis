from sklearn.metrics.pairwise import cosine_similarity
import operator


def itemsCercanos(perfilItems, num_vecinos=5):

    vecinosCercanos = {}
    # count = 0

    for item in perfilItems:
        print(item)
        vecinosCercanos[item] = {}
        for j in perfilItems:
            if j != item:
                sim = cosine_similarity(perfilItems[item], perfilItems[j])
                vecinosCercanos[item][j] = sim[0][0]
              
        vecinosCercanos[item] = sorted(
            vecinosCercanos[item].items(), key=operator.itemgetter(1), reverse=True)

    return vecinosCercanos


def usuariosCercanos(perfilUsuarios, num_vecinos=5):
    vecinosCercanos = {}
    # count = 0

    for usuario in perfilUsuarios:
        print(usuario)
        vecinosCercanos[usuario] = {}
        # print('Calculando vecinos cercanos...')
        for j in perfilUsuarios:
            if j != usuario:
                
                sim = cosine_similarity(
                    perfilUsuarios[usuario], perfilUsuarios[j])
                vecinosCercanos[usuario][j] = sim[0][0]
            
        vecinosCercanos[usuario] = sorted(
            vecinosCercanos[usuario].items(), key=operator.itemgetter(1), reverse=True)

    return vecinosCercanos


# def usuariosCercanosCopia(perfilUsuarios):
#     vecinosCercanos = {}

#     for usuario in perfilUsuarios:
#         # print(f'calculando el usuario cercano para {usuario}')
#         vecinosCercanos[usuario] = {}
#         k = 0
#         for j in perfilUsuarios:
#             if k > 5:
#                 # print(f'Saliendo del ciclo k={k}')
#                 break
#             else:
#                 if j != usuario:
#                     sim = cosine_similarity(
#                         perfilUsuarios[usuario], perfilUsuarios[j])
#                     vecinosCercanos[usuario][j] = sim[0][0]
#                     k = k + 1

#         vecinosCercanos[usuario] = sorted(
#             vecinosCercanos[usuario].items(), key=operator.itemgetter(1), reverse=True)

#     return vecinosCercanos
