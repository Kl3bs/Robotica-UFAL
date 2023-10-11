"""
Inicializa o workspace do robotics toolbox no iPython.
"""

import numpy as np
from roboticstoolbox import ET2, ET, ERobot, DHRobot, RevoluteDH, PrismaticDH, models


PLOT = True
PI = np.pi


def ets_2d(theta):
    """
    Cria um manipulador planar do tipo RR.
    """
    print("# --- Exemplo simples ETS 2D --- #")
    a_1 = 0.5
    a_2 = 0.75
    a_3 = 1
    robot_2 = ET2.R() * ET2.tx(a_1) * ET2.R() * ET2.tx(a_2) * ET2.R() * ET2.tx(a_3)

    print(f"Fkine =\n{robot_2.fkine(np.deg2rad(theta))}")
    print(f"# Joints: {robot_2.n}")
    print(f"Joints: {robot_2.joints()}")
    print(f"Structure: {robot_2.structure}")

    robot_2.teach(q=np.rad2deg(theta))
    
#ALTERNATIVA A
    
# theta_list = [-0.4240,2.4188]
# ets_2d(theta_list)

# Fkine =
#    0.9994   -0.03481   1.999     
#    0.03481   0.9994    0.02741   
#    0         0         1         


# theta_list = [1.9948,- 2.4188]
# ets_2d(theta_list)

# Fkine =
#    1         0.0074    1.999     
#   -0.0074    1         0.02741   
#    0         0         1  

""" É possível observar que deslocamento, em relação ao frame inicial,
    em ambos conjuntos de angulos é o mesmo."""


#ALTERNATIVA B e C

theta_list = [0,0.5, 0.5]
ets_2d(np.deg2rad(theta_list))
