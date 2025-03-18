#%%
## 1. Escreva uma função que receba uma lista de números e retorne outra lista com os números ímpares.
import pandas as pd

def filtrar_impares(lista):
    sr = pd.Series(lista)
    impar = sr[sr % 2 != 0].to_list()
    return impar

lista = [1, 2, 3, 45, 569, 7, 8, 9 , 14, 34, 567]
impares = filtrar_impares(lista)
print(f'Lista: {lista}\nNúmeros impares: {impares}')

#%%
## 4. Dada uma lista de números inteiros, escreva uma função para encontrar o segundo maior valor na lista
def seg_maior(n):
    df4 = pd.Series(n)
    segundo = df4.nlargest(2).iloc[-1]
    return segundo

resultado = seg_maior(lista)
print(f'O segundo maior número dessa lista é {resultado}')

#%%
## 8. Utilizando pandas, como realizar a leitura de um arquivoA CSV em um DataFrame e exibir as primeiras linhas?
dfcsv = pd.read_csv("../Avanti-Bootcamp/cidades.csv")
dfcsv.head()

#%%
##9. Utilizando pandas, como selecionar uma coluna específica e filtrar linhas em um “DataFrame” com base em uma condição?
df = pd.DataFrame(dfcsv)
rj = df[df['uf'] == 'Rio de Janeiro']
rj

#%%
## 10.Utilizando pandas, como lidar com valores ausentes (NaN) em um DataFrame?
dfm = pd.read_csv('../dados/meteorite_landings.csv')
dfm = dfm.dropna(subset='year')
dfm.isna().sum()

