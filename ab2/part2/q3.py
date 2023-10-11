import numpy as np
import matplotlib.pyplot as plt

# Defina os parâmetros do robô SCARA
L1 = 1.0  # Comprimento do primeiro braço
L2 = 1.0  # Comprimento do segundo braço

# Condições iniciais
# Valores iniciais das juntas (ângulo de rotação e deslocamento da junta de prisma)
q = np.array([0.0, 0.0])
x_desejado = 1.5  # Posição x desejada
y_desejado = 0.5  # Posição y desejada

# Taxa de amostragem
dt = 0.01  # Intervalo de tempo

# Listas para armazenar os erros de pose e o tempo
erro_pose_x = []
erro_pose_y = []
tempo = []

# Número total de etapas de tempo
num_etapas = 100

# Ganho do controlador
Kp = 1.0

for i in range(num_etapas):
    # Cinemática direta para calcular a posição atual do efetuador
    x_atual = L1 * np.cos(q[0]) + L2 * np.cos(q[0] + q[1])
    y_atual = L1 * np.sin(q[0]) + L2 * np.sin(q[0] + q[1])

    # Erro de pose
    erro_x = x_desejado - x_atual
    erro_y = y_desejado - y_atual

    # Atualização das juntas usando o controle de taxa resolvida
    J = np.array([
        [-L1 * np.sin(q[0]) - L2 * np.sin(q[0] + q[1]), -
         L2 * np.sin(q[0] + q[1])],
        [L1 * np.cos(q[0]) + L2 * np.cos(q[0] + q[1]),
         L2 * np.cos(q[0] + q[1])]
    ])

    delta_theta = np.linalg.pinv(J) @ np.array([Kp * erro_x, Kp * erro_y])
    q += delta_theta * dt

    # Armazena os erros de pose e o tempo
    erro_pose_x.append(erro_x)
    erro_pose_y.append(erro_y)
    tempo.append(i * dt)

# Plota o erro de pose em função do tempo
plt.figure(figsize=(10, 6))
plt.plot(tempo, erro_pose_x, label='Erro de Pose em x')
plt.plot(tempo, erro_pose_y, label='Erro de Pose em y')
plt.xlabel('Tempo (s)')
plt.ylabel('Erro de Pose')
plt.legend()
plt.title('Erro de Pose em Função do Tempo')
plt.grid(True)
plt.show()
