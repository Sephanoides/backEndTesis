from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from AppAlgoritmos import AppAlgoritmos
from userItemsAspects import getIUA
import time
import datetime
import pandas as pd
import os
import operator
# import sys


app = Flask(__name__)


CORS(app)


@app.route('/experimentos', methods=['GET', 'POST'])
def experimentos():

    try:

        if (request.method == 'POST'):
            
               
                algoritmos = request.form['algoritmos']
                file = request.files['csvFile']
                testSize = float(request.form['test'])
                vecinos = int(request.form['vecinos'])
                pr = int(request.form['pr'])

                algoritmos = algoritmos.split(',')
                algoritmos.sort()

                if not os.path.isdir('static'):
                    os.mkdir('static')
                filepath = os.path.join('static', file.filename)
                # guarda el archivo csv cargado en la carpeta static
                file.save(filepath)

                data = pd.read_csv(filepath, header=0)
                res = []

                items, users, aspects = getIUA(data)
                items = len(items)
                users = len(users)
                aspects = len(aspects)

                key = 0

                iua = {
                    'items': items,
                    'users': users,
                    'aspects': aspects
                }

                for algo in algoritmos:

                    key += 1
                    start_time = time.time()

                    precision, recall = AppAlgoritmos(algo, data,testSize,vecinos,pr)
                    end_time = time.time()
                    tiempo = round((end_time - start_time), 0)
                    res.append([key, algo.upper(), precision, recall,
                                str(datetime.timedelta(seconds=tiempo))])
                
                # os.remove(filepath)
                # Aqui se envian los datos al cliente con las respuestas de los algoritmos (métricas)
                return jsonify({
                    'ok': True,
                    'data': res,
                    'iua': iua
                })
        else:
            return jsonify({
            'ok': False,
            'data': 'Not method POST'
            })
    except:
        return jsonify({
            'ok':False,
            
        })


if __name__ == "__main__":
    app.run(debug=True)


