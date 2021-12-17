import joblib
import config_EngSalary as cfg
import pandas as pd
import numpy as np
from scipy.special import inv_boxcox

#Cargamos modelo y pipeline
EngSalary_model = joblib.load('EngineeringSalary_pipeline.pkl')
param_boxcox = joblib.load('boxcox_y.joblib')

#Funcion para hacer predicciones.
def predict(X):
    predicts = EngSalary_model.predict(X)
    salida = inv_boxcox(predicts, param_boxcox)
    print(salida)
    return salida

#Test = pd.read_csv('test.csv')
#Test = Test[cfg.FEATURES]
#Test['CollegeID'] = Test['CollegeID'].astype('O')
#preds = predict(Test)