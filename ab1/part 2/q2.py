from setup import * 

import numpy as np
import matplotlib.pyplot as plt

from spatialmath.base import *
def htransform_3d():
    """
    Matriz de transformação homogênea 3D.
    """
    T0 = transl(0, 0, 0)
    # T = transl(3, 0, 0) @ trotx(np.pi / 2) @ transl(0, 4, 0)
    # P = transl(1, 3, 1)

    trplot(T0, frame="O", color="k")
    # trplot(T, frame="A", color="b")
    # trplot(P, frame="P", color="r", length=0, axislabel=False)
    
    print(T0)

    plt.show()


def ets_3d2(joint_angle):
    """
    Cria um manipulador espacial do tipo RRRRRR.
    """
    print("# --- Exemplo simples ETS 3D --- #")
    a_1 = 1
    a_2 = 1
    a_3 = 0.5
    
    robot3 = ERobot(
        ET.tz(a_1) * ET.Rz() * ET.Ry() * ET.tz(a_2) * ET.Ry()  * ET.tz(a_3) 
    )

    print(f"Fkine =\n{robot3.fkine(np.deg2rad(joint_angle))}")
    print(f"# Joints: {robot3.n}")
    print(f"Structure: {robot3.structure}")

    robot3.teach(q=np.deg2rad(joint_angle))


#theta = np.array([0,0,0])
#theta = np.array([30,45,60])
#theta = np.array([45,60,75])
theta = np.array([60,75,90])
ets_3d2(theta)