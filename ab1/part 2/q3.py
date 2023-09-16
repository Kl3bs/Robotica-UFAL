from tabulate import tabulate


import numpy as np

# Função para calcular a matriz de transformação homogênea DH
def dh_transform(theta, d, a, alpha):
    return np.array([
        [np.cos(theta), -np.sin(theta) * np.cos(alpha), np.sin(theta) * np.sin(alpha), a * np.cos(theta)],
        [np.sin(theta), np.cos(theta) * np.cos(alpha), -np.cos(theta) * np.sin(alpha), a * np.sin(theta)],
        [0, np.sin(alpha), np.cos(alpha), d],
        [0, 0, 0, 1]
    ])

# Função para calcular a posição final do atuador
def calcular_posicao_final(juntas):
    T = np.eye(4)  # Inicializa a matriz de transformação homogênea como uma matriz identidade

    for junta in juntas:
        theta, d, a, alpha = junta
        T_junta = dh_transform(theta, d, a, alpha)
        T = np.dot(T, T_junta)

    # A posição final está na última coluna da matriz resultante
    posicao_final = T[:3, 3]
    return posicao_final

# Exemplo de entrada com ângulos das juntas em radianos (theta, d, a, alpha)
juntas = [
    (np.deg2rad(30), 0.1, 0, np.deg2rad(90)),
    (np.deg2rad(45), 0, 0.2, np.deg2rad(0)),
    (np.deg2rad(60), 0, 0.1, np.deg2rad(0))
]

posicao_final = calcular_posicao_final(juntas)
print("Posição final do atuador:", posicao_final)

 


table = [['i', 'αi-1', 'ai-1', 'di' ,'θi'], 
         ['1', '0', 'L1','d1' , 'θ1'], 
         ['2', '0', 'L2','0' , 'θ2'], 
         ['3', '0', '0', '0' ,'θ3'],
         ['4', 'π', '0', 'd3' ,'θ4']]

print(tabulate(table))


