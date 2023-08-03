import pandas as pd
import numpy as np
s = pd.Series(dtype="float64")
print(type(s))
datos=[1.5,6.02,8.8,7.1]
indices=['A','B','C','D']
s=pd.Series(index=indices,dtype='float64')
print(s)
print(len(s))

datos=[1,2,3,1,1,1,5,2,3,8,88,88,89]
s=pd.Series(datos)
print(s.unique())
print(type(s.unique()))
print(s.value_counts())
datos1=[3,3,5,6,7,7,8]
s1=pd.Series(datos1)
suma=s+s1
print(suma)
print(type(suma))

datos2=[10,20,30]
indices1=['A','B','C']
s2=pd.Series(datos2,index=indices1)
datos3=[5,100]
indices2=['B','C']
s3=pd.Series(datos3,index=indices2)
x=s2+s3
print(x)

print(x.mean())
print(x.std())
print('moda=',x.mode())
print(x.median())


datos = [10, 20, 30, 40, 50]
etiquetas = ['A', 'B', 'C', 'D', 'E']

# Creamos la Series con los datos y etiquetas
serie_ejercicio = pd.Series(data=datos, index=etiquetas)

# Seleccionamos los elementos mayores a 30
elementos_mayores_a_30 = serie_ejercicio[serie_ejercicio > 30]
print("Elementos mayores a 30:")
print(elementos_mayores_a_30)


serie_ejercicio = pd.Series(data=['a','b','c','d', 'e', 'ef'])
elementos_mayores_a_30 = serie_ejercicio[serie_ejercicio > 'e']
print("Elementos mayores a 30:")
print(elementos_mayores_a_30)


# Datos como una lista
datos = [1, 2, 3, 3, 4, 4, 4, 5]

# Creamos la Series con los datos
serie_datos = pd.Series(data=datos)

# Condiciones: Filtramos los datos que sean mayores o iguales a 3 y menores o iguales a 5
condicion_1 = serie_datos >= 3
condicion_2 = serie_datos <= 5

# Aplicamos las dos condiciones
serie_filtrada = serie_datos[condicion_1 & condicion_2]

# Calculamos la mediana de la serie filtrada
mediana_filtrada = serie_filtrada.median()

print("Mediana con dos condiciones:", mediana_filtrada)

pasar string de minúsculas a mayúsculas: 
import pandas as pd
#ponemos aqui los strings, proque necesitamos comparar con los strings y no con numeros.
datos = ['a', 'b', 'c', 'd', 'e', 'f']

s2 = pd.Series(datos)
print(s2)

x = (s2.str.upper())
print(x)


#Valor absoluto y poner en mayúsculas:
import pandas as pd
def valor_ab(x):
    if x<0:
        return x*(-1)
    return x
datos=[-10,-20,30,-40,50,60]
indices=['A','B','C','D','E','F']
s=pd.Series(datos,index=indices)
s_va=s.map(valor_ab)
print(s_va)

datos=['a','b','c','d','e','f']
indices1=['0','1','2','3','4','5']
s1=pd.Series(datos,index=indices1)
print(s1.str.upper())

