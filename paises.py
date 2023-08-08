# Uso el metodo de pandas pd.read_html para coger todos los países del mundo de una 
#tabla html de una web de wikipedia. pd.read_html() devuelve una lista de dataframes.
#La lista tendrá tantos elementos de tipo dataframe como tablas haya en esa web.
import pandas as pd
#Se lee los datos de wikipedia de los países
paises=pd.read_html('https://es.wikipedia.org/wiki/Anexo:Pa%C3%ADses') #
print(len(paises)) 
print(type(paises))
print(len(paises[0]))
