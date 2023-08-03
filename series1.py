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