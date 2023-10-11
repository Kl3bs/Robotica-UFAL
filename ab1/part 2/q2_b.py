import numpy as np

# Função para calcular a matriz de transformação homogênea DH
def dh_transform(theta, d, a, alpha):
    return np.array([
        [np.cos(theta), -np.sin(theta) * np.cos(alpha), np.sin(theta) * np.sin(alpha), a * np.cos(theta)],
        [np.sin(theta), np.cos(theta) * np.cos(alpha), -np.cos(theta) * np.sin(alpha), a * np.sin(theta)],
        [0, np.sin(alpha), np.cos(alpha), d],
        [0, 0, 0, 1]
    ])

# Ângulos em graus para cada frame
theta0 = np.deg2rad(0)
theta1 = np.deg2rad(30)
theta2 = np.deg2rad(45)
theta3 = np.deg2rad(60)

# Calcula as matrizes de transformação homogênea
T01 = dh_transform(theta0, 0, 0, 0)
T12 = dh_transform(theta1, 0, 0, 0)
T23 = dh_transform(theta2, 0, 0, 0)

# Calcula a transformação de 0 para 3 (T03)
T03 = np.dot(np.dot(T01, T12), T23)

# Exibe as matrizes de transformação homogênea
print("T01:")
print(T01)
print("\nT12:")
print(T12)
print("\nT23:")
print(T23)
print("\nT03:")
print(T03)
