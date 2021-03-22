from surprise import KNNBasic
from surprise import Dataset
from surprise import accuracy
from surprise.model_selection import train_test_split, cross_validate

import pandas as pd
from collections import defaultdict
from surprise import Reader
from surprise.model_selection import KFold

import json

def PR(algo,data, num_fold):
    
    kf = KFold(n_splits=num_fold)
    
    #solo 1 vez, sin tecnica kFold
    trainset, testset = train_test_split(data, test_size=.2, shuffle=False)
    
    algo.fit(trainset)
    predictions = algo.test(testset)
    precisions, recalls = precision_recall_at_k(predictions, k=5, threshold=3.5)

        # Precision and recall can then be averaged over all users
    print('     Precision')
    print(sum(prec for prec in precisions.values()) / len(precisions))
    print('     Recall')
    print(sum(rec for rec in recalls.values()) / len(recalls))
   
        
    return 0




def precision_recall_at_k(predictions, k=5, threshold=4):
    """Return precision and recall at k metrics for each user"""

    # First map the predictions to each user.
    user_est_true = defaultdict(list)
    for uid, _, true_r, est, _ in predictions:
        user_est_true[uid].append((est, true_r))

    precisions = dict()
    recalls = dict()
    for uid, user_ratings in user_est_true.items():

        # Sort user ratings by estimated value
        user_ratings.sort(key=lambda x: x[0], reverse=True)

        # Number of relevant items
        n_rel = sum((true_r >= threshold) for (_, true_r) in user_ratings)

        # Number of recommended items in top k
        n_rec_k = sum((est >= threshold) for (est, _) in user_ratings[:k])

        # Number of relevant and recommended items in top k
        n_rel_and_rec_k = sum(((true_r >= threshold) and (est >= threshold))
                              for (est, true_r) in user_ratings[:k])

        # Precision@K: Proportion of recommended items that are relevant
        # When n_rec_k is 0, Precision is undefined. We here set it to 0.

        precisions[uid] = n_rel_and_rec_k / n_rec_k if n_rec_k != 0 else 0

        # Recall@K: Proportion of relevant items that are recommended
        # When n_rel is 0, Recall is undefined. We here set it to 0.

        recalls[uid] = n_rel_and_rec_k / n_rel if n_rel != 0 else 0

    return precisions, recalls


#------------------------------------------------------------------

def traindAndFit(algo, data):
    
    trainset, testset = train_test_split(data, test_size=.2, shuffle=False)
    
    # Train the algorithm on the trainset, and predict ratings for the testset
    algo.fit(trainset) #con fit entrenamos el algoritmo
    predictions = algo.test(testset)
    
    rmse = accuracy.rmse(predictions) #metrica RMSE
    mae = accuracy.mae(predictions) #métrica MAE
    

    return rmse, mae


def crossValidation(algo, data, num_fold):
    
    cv = cross_validate(algo, data, measures=['RMSE','MAE'], cv=num_fold, verbose=True)
    
    num = 0
    rmse = ['RMSE']
    mae = ['MAE']
    
    while num < num_fold:
        
        rmse.append(round(cv['test_rmse'][num],4))
        mae.append(round(cv['test_mae'][num],4))
        num += 1

    return rmse,mae


def KNNBasico(num_fold, datos = ''):
    
    print('KNN basado en user RMSE MAE  P@5  R@5')
    #df = pd.read_excel('../datasets/yelp_beautySpa_aspects.csv')
    df = pd.read_csv('../datasets/yelp_hotels_aspects.csv', header=0)
    reader = Reader(rating_scale=(1, 5))
    data = Dataset.load_from_df(df[['user_id', 'item_id', 'rating']], reader)
    
    k = 5
    k_min = 1
    sim_options = {'name': 'cosine',
                   'user_based': False  # basado en usuario
                   }
    
    #Utilizamos el algortimos de KNN basico
    algo = KNNBasic(k,k_min,sim_options=sim_options)
    
    #rmse, mae = crossValidation(algo, data, num_fold)
    rmse, mae =traindAndFit(algo,data)
    print()
    PR(algo,data,5)
    
    return 0



KNNBasico(5)












    

    
    

    