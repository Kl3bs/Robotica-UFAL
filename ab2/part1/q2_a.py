import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def point_cloud_3d(x, y, z):
    """
    Plots a 3D point cloud.
    """
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, s=20, c='b', marker='o', label='Point Cloud')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Point Cloud Visualization')
    ax.legend(loc='upper right')

    ax.grid(True)
    plt.tight_layout()
    plt.show()

# Range de valores para q1, q2 e q3
q1_values = np.linspace(-np.pi/2, np.pi/2, 20)
q2_values = np.linspace(-np.pi/2, np.pi/2, 20)
q3_values = np.linspace(-np.pi/2, np.pi/2, 20)

# Listas para armazenar as coordenadas X, Y e Z da nuvem de pontos
x_points = []
y_points = []
z_points = []


L1 =  1
L2 =  1
L3 =  1
# Loop através das configurações das juntas q1, q2 e q3
for q1 in q1_values:
    for q2 in q2_values:
        for q3 in q3_values:
            # Calcule as coordenadas X, Y e Z para a configuração atual (q1, q2, q3)
            x = L1 * np.cos(q1) + L2 * np.cos(q1 + q2) + L3 * np.cos(q1 + q2 + q3)
            y = L1 * np.sin(q1) + L2 * np.sin(q1 + q2) + L3 * np.sin(q1 + q2 + q3)
            z = 0  # Apenas um exemplo; o valor de z pode variar com base no seu sistema

            # Adicione as coordenadas à lista
            x_points.append(x)
            y_points.append(y)
            z_points.append(z)

# Plote a nuvem de pontos 3D do espaço de trabalho do manipulador 3 DOF
point_cloud_3d(x_points, y_points, z_points)
