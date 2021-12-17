from flask import Flask, jsonify, request
import pandas as pd
import numpy as np

import config_EngSalary as cfg
import pp_predict_EngSalary as pp
import json
from json import JSONEncoder

app = Flask(__name__)

# Funcion para convertir arreglo de numpy a json
class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)

#ruta para predecir.
@app.route("/prediccion_EngSalary", methods=['POST'])
def predict_from_pp():
    json_data = request.get_json()
    dataframe = pd.json_normalize(json_data)
    data = dataframe

    #prediccion
    data = data[cfg.FEATURES] # Se seleccionan solo las variables a utilizar en el modelo
    data['CollegeID'] = data['CollegeID'].astype('O') # Parseo de variable CollegeID a categorica
    resultado = pp.predict(data)
    numpyData = {"resultado": resultado} #Generacion de diccionario para codificar a json
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # escribir arreglo a archivo json
    print(encodedNumpyData)
    return encodedNumpyData

