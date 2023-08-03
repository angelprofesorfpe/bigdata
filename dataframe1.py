import pandas as pd
import numpy as np

df_vacio = pd.DataFrame()
print(df_vacio)
print(type(df_vacio))

data = {
    'Nombre': ['Juan', 'Mary', 'Carlos']       
}
df = pd.DataFrame(data)
print(df)


data = {
    'Nombre': ['Juan', 'Mary', 'Carlos'],       
    'Edad' : [33, 45, 22]   
}
df1 = pd.DataFrame(data)
print(df1)



data = {
    'Nombre': ['Juan', 'Mary', 'Carlos'],       
    'Edad' : [33, 45, 22],
    'Ciudad': ["Madrid", "Bilbao", "Valencia"]
}
df2 = pd.DataFrame(data)
print(df2)

df2.to_excel("excel.xlsx")

df3 = pd.read_excel("animal.xlsx")
print(df3)

filas = 100
columnas = 3
data = np.random.rand(filas, columnas)
print(data)
df4 = pd.DataFrame(data, columns=['radiacion_ionica', 'ganma', 'impedancia'])
print(df4)
print(df4.head(20))
print(df4.tail(20))
print(df4.sample(20))
print(df4.info())
print(df4.describe())


print(df3.loc[0, 'Animal'])
print(df3.loc[1, 'Animal'])
print(df3.loc[2, 'Animal'])
print(df3.loc[0, 'Edad'])
print(df3.loc[1, 'Edad'])
print(df3.loc[2, 'Edad'])
print(df3.loc[0, 'Peso'])
print(df3.loc[1, 'Peso'])
print(df3.loc[2, 'Peso'])

df3.loc[0, 'Animal'] = "Elefante"
print(df3)
df3['estatura'] = 999
print(df3)
df3['estatura'] = [123,111,166]
print(df3)
df3 = df3.append ({'Animal': 'Correcaminos', 'Edad': 8, 'Peso': 876, 'estatura': 321}, ignore_index=True)
print(df3)
df_t = df3.T
print(df_t)
df_t.to_excel("df_transpuesto.xlsx")
df3['Edad'] = df3['Edad'].map(lambda x:x+1)
print(df3)












