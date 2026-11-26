import pandas as pd
import numpy as np

# IMPORTAR DATOS
url_test = "https://raw.githubusercontent.com/a01713204/Natural-Language-Processing-with-Disaster-Tweets/refs/heads/main/Datos/test.csv"
url_train = "https://raw.githubusercontent.com/a01713204/Natural-Language-Processing-with-Disaster-Tweets/refs/heads/main/Datos/train.csv"

# Dataframes
df_train = pd.read_csv(url_train)
df_test = pd.read_csv(url_test)

# VISUALIZAR Y ANALIZAR DATOS
# Tamaño de dataframes
print("Train:", df_train.shape)
print("Test:", df_test.shape)

# Visualización de dataframe ( a partir de aqui usamos los datos de 'train', ya que son con lps cuales entrenaremos al modelo inicialmete)
display(df_train.head())

# Info del dataset
df_train.info()

# Columnas del dataset
print(df_train.columns)

# Buscamos valores null
print(df_train.isnull().sum())

# Estadistica y descripcipon general
display(df_train.describe(include='all'))

# Revisión de las etiquetas
print(df_train['target'].value_counts())
print(df_train['target'].value_counts(normalize=True) * 100) # ahora normalizados


