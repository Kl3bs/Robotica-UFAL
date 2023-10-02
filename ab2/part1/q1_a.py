
import matplotlib.pyplot as plt
import numpy as np
from roboticstoolbox import DHRobot, RevoluteDH
from spatialmath.base import transl


def point_cloud_2d(x, y):
    """
    Plota uma nuvem de pontos 2D.
    """

    # Create a scatter plot
    plt.figure(figsize=(8, 6))  # Adjust the figure size as needed
    plt.scatter(x, y, s=20, c='b', marker='o', label='Point Cloud')  # Adjust parameters as needed

    # Add labels and a legend (customize as needed)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Point Cloud Visualization')
    plt.legend(loc='upper right')

    # Show the plot
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    
# Intervalos para q1 e q2
q1_values = np.linspace(0, np.pi, 100)  # Intervalo de 0 a pi
q2_values = np.linspace(-np.pi/2, np.pi, 100)  # Intervalo de -pi/2 a pi

# Listas para armazenar as coordenadas X e Y da nuvem de pontos
x_points = []
y_points = []

#Comprimento das juntas
L1 = 1 
L2 = 2

# # Loop através das configurações do manipulador
# for q1 in q1_values:
#     for q2 in q2_values:
#         # Calcule as coordenadas X e Y para a configuração atual (q1, q2)
#         x = L1 * np.cos(q1) + L2 * np.cos(q1 + q2)
#         y = L1 * np.sin(q1) + L2 * np.sin(q1 + q2)
        
#         # Adicione as coordenadas à lista
#         x_points.append(x)
#         y_points.append(y)

# # Plote a nuvem de pontos 2D do espaço de trabalho
# point_cloud_2d(x_points, y_points)

 
