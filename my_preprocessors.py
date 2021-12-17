import pandas as pd
import numpy as np

from sklearn.base import BaseEstimator, TransformerMixin

#Clase para manejo de variables temporales en el modelo de House Price
class TemporalVariableTransformer(BaseEstimator, TransformerMixin):

    #Constructor
    def __init__(self, variables, reference_variable):
        if not isinstance(variables, list):
            raise ValueError("Las varibles debe ser incluida en una lista.")
        
        self.variables = variables
        self.reference_variable = reference_variable

    #metodo fit para habilitar metodo transform
    def fit(self, X, y=None):
        return self

    #metodo para transformar variables temporales.
    def transform(self, X):
        X = X.copy()
        
        for feature in self.variables:
            mode = X[feature].mode()[0]
            X[feature] = np.where(X[feature] == 0, mode, X[feature])
            
        X[self.reference_variable] = X[self.reference_variable].str[0:4].astype('int')
        
        for feature in self.variables:
            X[feature] =  X[feature] - X[self.reference_variable]
        return X