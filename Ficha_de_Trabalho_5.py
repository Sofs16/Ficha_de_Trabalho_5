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
