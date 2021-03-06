from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')
    
class Imputer(TransformerMixin):
    def __init__(self):
        """Impute missing values.
        Columns of dtype object are imputed with the most frequent value 
        in column.
        Columns of other types are imputed with mean of column.
        """
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        new_values = {'NOTA_GO':data['NOTA_GO'].median(), 'INGLES': data['INGLES'].median() }
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.fillna(value=new_values)

class Scaler(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Depois convertemos as colunas para o tipo numérico
        data[self.columns] = data[self.columns].apply(pd.to_numeric)
        # Em seguida aplicamos a função de normalização
        data[self.columns] = data[self.columns].apply(minmax_scale)
        # Retornamos o dataframe com as colunas normalizadas
        return data
