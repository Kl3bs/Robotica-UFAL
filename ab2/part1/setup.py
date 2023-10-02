"""
Inicializa o workspace do robotics toolbox no iPython.
"""

import matplotlib.pyplot as plt

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

def dh_rr():
    """
    Cria um manipulador do tipo RR.
    """
    print("# --- Exemplo utilizando DH --- #")

    link1 = RevoluteDH(a=1) # cria um link de revolução
    link2 = RevoluteDH(a=1)

    robot_dh = DHRobot([link1, link2], name="RR") # cria um manipulador DH

    print(robot_dh)

    return robot_dh

def numeric_ikine_rr(x, y, z):
    """
    Calcula a cinemática inversa de um manipulador RR (numericamente).
    """
    rr_robot = dh_rr()
    return rr_robot.ikine_LM(
        transl(x, y, z) # pose SO3 desejada
    )