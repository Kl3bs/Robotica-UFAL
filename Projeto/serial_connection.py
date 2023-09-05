import serial
import time

# Configuração da porta serial (ajuste a porta e a velocidade conforme necessário)
ser = serial.Serial('/dev/cu.usbmodem14201', 9600)

while True:
    # Código para calcular o ângulo aqui (como no exemplo anterior)
    angle_deg = 45.0  # Substitua isso pelo ângulo real calculado

    # Enviar o ângulo pela porta serial
    ser.write(str(angle_deg).encode())
    time.sleep(0.1)  # Pausa para evitar envio muito rápido
