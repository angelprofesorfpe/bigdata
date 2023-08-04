import pandas as pd
import numpy as np


filas = 1000
columnas = 4
data = np.random.randint(0, high=10, size=((filas,columnas)))
print(data)
df = pd.DataFrame(data, columns=['col1', 'col2', 'col3', 'col4'])
print(df)
print(df.head(20))
print(df.tail(20))
print(df.sample(20))
print(df.info())
print(df.describe())

# Multiplicar cada valor en el DataFrame por 2
df = df * 2
print(df)


# Crear una nueva columna que sea la suma de col1 y col2 de 2 formas dieferenes: 1) usando Numpy 2) sumando directamente con +
df['Suma'] = np.add(df['col1'], df['col2'])
df['Suma2'] = df['col1'] + df['col2']

# Crear una nueva columna que sea la resta de col1 y col2
df['Resta'] = np.subtract(df['col1'], df['col2'])
df['Resta2'] = df['col1'] - df['col2']

# Crear una nueva columna que sea el resultado de la multiplicación de col1 y col2
df['Product'] = np.multiply(df['col1'], df['col2'])
df['Product2'] = df['col1'] * df['col2']
print(df)

# Crear una nueva columna que sea el resultado de la multiplicación de col1 y col2
df['Divide'] = np.divide(df['col1'], df['col2'])
df['Divide2'] = df['col1'] / df['col2']
print(df)

# Definir una función personalizada que devuelve el producto de dos columnas
def f(x, y, z):
    if y==0:
        return 0
    return x / y - z

# Aplicar la función a las columnas A y B usando Numpy
df['nuevaCol'] = np.vectorize(f)(df['col1'], df['col2'], df['col3'])
print(df)









