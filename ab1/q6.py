import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Função para desenhar um cubo centrado na origem com transformação homogênea
def draw_transformed_cube(transformation_matrix):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Define os vértices do cubo
    vertices = np.array([
        [-0.5, -0.5, -0.5, 1],
        [0.5, -0.5, -0.5, 1],
        [0.5, 0.5, -0.5, 1],
        [-0.5, 0.5, -0.5, 1],
        [-0.5, -0.5, 0.5, 1],
        [0.5, -0.5, 0.5, 1],
        [0.5, 0.5, 0.5, 1],
        [-0.5, 0.5, 0.5, 1]
    ])

    # Aplica a transformação homogênea aos vértices
    transformed_vertices = np.dot(vertices, transformation_matrix.T)

    # Define as faces do cubo
    faces = [
        [transformed_vertices[0], transformed_vertices[1], transformed_vertices[2], transformed_vertices[3]],
        [transformed_vertices[4], transformed_vertices[5], transformed_vertices[6], transformed_vertices[7]],
        [transformed_vertices[0], transformed_vertices[1], transformed_vertices[5], transformed_vertices[4]],
        [transformed_vertices[2], transformed_vertices[3], transformed_vertices[7], transformed_vertices[6]],
        [transformed_vertices[0], transformed_vertices[3], transformed_vertices[7], transformed_vertices[4]],
        [transformed_vertices[1], transformed_vertices[2], transformed_vertices[6], transformed_vertices[5]]
    ]

    # Desenha o cubo
    ax.add_collection3d(Poly3DCollection(faces, edgecolor='b', linewidths=1, alpha=0.5))

    # Define os limites dos eixos
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])

    # Rótulos dos eixos
    ax.set_xlabel('Eixo X')
    ax.set_ylabel('Eixo Y')
    ax.set_zlabel('Eixo Z')

    plt.show()

# Matriz de transformação homogênea de exemplo (identidade neste caso)
transformation_matrix = np.identity(4)

# Chame a função para desenhar o cubo com a transformação
draw_transformed_cube(transformation_matrix)
