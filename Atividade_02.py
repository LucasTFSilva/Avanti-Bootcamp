#%%
## 1. Escreva uma função que receba uma lista de números e retorne outra lista com os números ímpares.
def definir_impares(lista):
    resultado = []
    for i in lista:
        if i % 2 != 0:
            resultado.append(i)
    return resultado

a = [3, 4, 5, 6, 7, 8, 9, 90, 10]
b = [5, 67, 8, 89,9 ,12, 23, 4, 5,]
definir_impares(a)
#%%
## 2. Escreva uma função que receba uma lista de números e retorne outra lista com os números primos presentes.

def ePrimo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def listaPrimos(lst):
    elst = []
    for i in lst:
        if ePrimo(i):
            elst.append(i)
    return elst

print(listaPrimos(a))
# %%
##3. Escreva uma função que receba duas listas e retorne outra lista com os elementos que estão presentes em apenas uma das listas.
def listas_separadas(lst1, lst2):
    lst_final = []
    result = lst_final.append(lst1)
    return result

print(listas_separadas(a, b))

#%%
## 4. Dada uma lista de números inteiros, escreva uma função para encontrar o segundo maior valor na lista
def seg_maior(n):
    df4 = pd.Series(n)
    segundo = df4.nlargest(2).iloc[-1]
    return segundo

resultado = seg_maior(lista)
print(f'O segundo maior número dessa lista é {resultado}')

# %%
## 5. Crie uma função que receba uma lista de tuplas, cada uma contendo o nome e a idade de uma pessoa, e retorne a lista ordenada pelo nome das pessoas em ordem alfabética.

def list_tuplas(lst):
    resposta = sorted(lst, key=lambda lst:lst[0])
    return resposta

lista_de_tuplas = [('Anderson', 40), ('Renata', 45), ('Lucas', 27), ('Beatriz', 26)]
list_tuplas(lista_de_tuplas)

# %%
## 6. Observe os espaços sublinhados e complete o código

import matplotlib.pyplot as plt
import numpy as np
fig, axs = plt.subplots(ncols=2, nrows=2, figsize=(5.5, 3.5),
 layout="constrained")
for row in range(2):
        for col in range(2):
            axs[row, col].annotate(f'axs[{row}, {col}]', (0.5, 0.5),
            transform=axs[row, col].transAxes, ha='center', va='center', 
            fontsize=18, color='darkgrey')
fig.suptitle('plt.subplots()')

#%%
## 8. Utilizando pandas, como realizar a leitura de um arquivoA CSV em um DataFrame e exibir as primeiras linhas?
cidades = pd.read_csv("../Avanti-Bootcamp/dados/cidades.csv")
cidades.head()

#%%
##9. Utilizando pandas, como selecionar uma coluna específica e filtrar linhas em um “DataFrame” com base em uma condição?
df = pd.DataFrame(cidades)
rj = df[df['uf'] == 'Rio de Janeiro']
print(rj)

#%%
## 10.Utilizando pandas, como lidar com valores ausentes (NaN) em um DataFrame?
## Podemos substituir, ignorar ou remover os valores ausentes dentro de um dataframe.
meteritos = pd.read_csv("../Avanti-Bootcamp/dados/meteorite_landings.csv")
dfmet = pd.DataFrame(meteritos)
dfmet_clean = dfmet.dropna(subset=['year', 'mass (g)', 'reclat', 'reclong', 'GeoLocation'])
dfmet_clean.isna().sum()

