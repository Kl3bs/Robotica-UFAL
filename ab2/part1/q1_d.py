from q1_a import *


# Comprimento do primeiro elo
L1 = 1.0

# Comprimento do segundo elo (não será usado neste exemplo)
L2 = 1.0

# Lista para armazenar as coordenadas X e Y da nuvem de pontos
x_points = []
y_points = []

# Range de valores de q1 (de 0 a pi)
q1_values = np.linspace(0, np.pi, 100)

# Configuração fixa da junta q2 (0 radianos)
q2 = 0

# Loop através das configurações da junta q1
for q1 in q1_values:
    # Calcula as coordenadas X e Y para a configuração atual (q1, q2)
    x = L1 * np.cos(q1)
    y = L1 * np.sin(q1)
    
    # Adicione as coordenadas à lista
    x_points.append(x)
    y_points.append(y)

# Plote a nuvem de pontos 2D que exemplifica o trabalho da junta 1
point_cloud_2d(x_points, y_points)