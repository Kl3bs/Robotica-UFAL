from setup import *

def dh():
    """
    Cria um manipulador do tipo RRP.
    """
    print("# --- Exemplo utilizando DH --- #")

    link1 = PrismaticDH(a=1, alpha = 1, offset = 2, qlim=(1., 1.))  # cria um link prismatico  # cria um link de revolução
    link2 = RevoluteDH(a=1) # cria um link de revolução
    #link2 = PrismaticDH(theta=PI/2, alpha=PI/2, qlim=(0., 1.)) # cria um link prismatico
    link3 = RevoluteDH(a=1)

    print(link1.A(0.5)) # calcula a matriz de transformação homogênea para theta=0.5

    robot_dh = DHRobot([link1, link2, link3], name="RRR") # cria um manipulador DH

    print(robot_dh)
    print(robot_dh.fkine(q=[0, 0.5, 0]))

    robot_dh.teach(q=[0, 0.5, 0]) # visualiza o manipulador com interação
    
dh()