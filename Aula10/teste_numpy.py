# -*- coding: utf-8 -*-
import numpy as np

print("NumPy instalado com sucesso!")
print(f"Versao: {np.__version__}")

#   usando numpy, ja tendo uma variavel de nota como faco uma variavel de media?
#   Para calcular a media usando NumPy, voce pode usar a funcao `np.mean()`. Suponha que voce tenha
#   uma variavel de notas chamada `notas`, que e um array NumPy. Voce pode calcular a media da seguinte maneira:

notas = np.array([85, 90, 78, 92, 88])  # Exemplo de array de notas
media = np.mean(notas)  # Calcula a media das notas
print(f"A media das notas e: {media}")