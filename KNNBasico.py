# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 02:37:32 2021

@author: Hugo
"""
from surprise import KNNWithMeans
from surprise import Reader
# import pandas as pd
from surprise import Dataset
from surprise.model_selection import train_test_split
from collections import defaultdict


def precision_recall_at_k(predictions, k=10, threshold=4):
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



def knnBasico(df, testSize, vecinos,pr, bool):

    # df = pd.read_csv('../datasets/yelp_beautySpa_aspects.csv', header=0)
    reader = Reader(rating_scale=(1, 5))
    data = Dataset.load_from_df(df[['user_id', 'item_id', 'rating']], reader)
    trainset, testset = train_test_split(data, test_size=testSize, shuffle=False)


    sim_options = {'name': 'cosine',
                'user_based': bool  # compute  similarities between items
                }
    algo = KNNWithMeans(k=vecinos,sim_options=sim_options)


    algo.fit(trainset)
    predictions = algo.test(testset)
    precisions, recalls = precision_recall_at_k(predictions, pr, 4)

    # Precision and recall can then be averaged over all users
    # print(sum(prec for prec in precisions.values()) / len(precisions))
    # print(sum(rec for rec in recalls.values()) / len(recalls))

    precision = round(sum(prec for prec in precisions.values()) / len(precisions),3)
    recall = round(sum(rec for rec in recalls.values()) / len(recalls),3)
    
    return precision, recall
    # print(predictions)
