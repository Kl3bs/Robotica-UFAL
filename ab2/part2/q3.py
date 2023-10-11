import numpy as np
import matplotlib.pyplot as plt

L1 = 1.0
L2 = 1.0

q = np.array([0.0, 0.0])
x_desejado = 1.5
y_desejado = 0.5

dt = 0.01

erro_pose_x = []
erro_pose_y = []
tempo = []

num_etapas = 100

Kp = 1.0

for i in range(num_etapas):
    x_atual = L1 * np.cos(q[0]) + L2 * np.cos(q[0] + q[1])
    y_atual = L1 * np.sin(q[0]) + L2 * np.sin(q[0] + q[1])

    erro_x = x_desejado - x_atual
    erro_y = y_desejado - y_atual

    J = np.array([
        [-L1 * np.sin(q[0]) - L2 * np.sin(q[0] + q[1]), -
         L2 * np.sin(q[0] + q[1])],
        [L1 * np.cos(q[0]) + L2 * np.cos(q[0] + q[1]),
         L2 * np.cos(q[0] + q[1])]
    ])

    delta_theta = np.linalg.pinv(J) @ np.array([Kp * erro_x, Kp * erro_y])
    q += delta_theta * dt

    erro_pose_x.append(erro_x)
    erro_pose_y.append(erro_y)
    tempo.append(i * dt)

plt.figure(figsize=(10, 6))
plt.plot(tempo, erro_pose_x, label='Erro de Pose em x')
plt.plot(tempo, erro_pose_y, label='Erro de Pose em y')
plt.xlabel('Tempo (s)')
plt.ylabel('Erro de Pose')
plt.legend()
plt.title('Erro de Pose em Função do Tempo')
plt.grid(True)
plt.show()
