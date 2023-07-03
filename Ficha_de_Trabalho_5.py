#1. Importar os dados:

import matplotlib.pyplot as plt
import pandas as pd

dados = pd.read_csv("AtividadePedagogica4_10793_02.csv")

# 2. Aplicar Algoritmos de Ordenação:
    
"""Ordenar pelo Bubble_Sort"""
def bubble_sort(dados):
    n = len(dados)
    for i in range(n - 1):
        for j in range(n-i-1):
            if dados['quantidade_vendida'].iloc[j] > dados['quantidade_vendida'].iloc[j+1]:
                dados.iloc[j], dados.iloc[j+1] = dados.iloc[j+1], dados.iloc[j]
    return dados
                
dados_ordenados_bubble = bubble_sort(dados)
print("***Dados ordenados pelo Bubble Sort***")
print("")
print(dados_ordenados_bubble)


""""Ordenar pelo Quick_Sort"""
def quick_sort(dados):
    if len(dados) <= 1:
        return dados

# Este trecho define a divisão dos dados em 3 partes: menor, igual ou superior ao pivot - valor do index central. 
    pivot = dados['quantidade_vendida'].iloc[len(dados) // 2]
    left = dados[dados['quantidade_vendida'] < pivot]
    middle = dados[dados['quantidade_vendida'] == pivot]
    right = dados[dados['quantidade_vendida'] > pivot]

#Esta linha ordena as partes anteriormente definidas:  e usa o pd.concat para retornar um DataFrame final ordenado. O ignore_index=True faz com que se redifina os index do novo DataFrame.
    return pd.concat([quick_sort(left), middle, quick_sort(right)], ignore_index=True)

dados_ordenados_quick = quick_sort(dados)

print("")
print("***Dados ordenados pelo Quick Sort***")
print(dados_ordenados_quick)



#3. Apresentar Resultados: 
# Agrupar por produto e calcular a soma das vendas
dados_soma_produto = dados.groupby('produto')['quantidade_vendida'].sum().reset_index()
dados_ordenados_soma_produto = dados_soma_produto.sort_values('quantidade_vendida')

# Criar o gráfico de barras
plt.bar(dados_ordenados_soma_produto['produto'], dados_ordenados_soma_produto['quantidade_vendida'], color=['green'])
plt.xlabel('Produto')
plt.ylabel('Total de Vendas')
plt.title('Total de Vendas por Produto')

# Exibir o gráfico
plt.show()