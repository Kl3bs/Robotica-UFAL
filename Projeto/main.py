import cv2
import mediapipe as mp
import math
import time
import serial


ser = serial.Serial('/dev/cu.usbmodem14201', 9600)


# Inicializar o módulo de detecção de mãos do Mediapipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Inicializar a captura de vídeo da webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Converter o frame para escala de cores RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Detectar mãos no frame
    results = hands.process(rgb_frame)
    
    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            # Verificar se existem pontos suficientes para o dedo indicador
            if len(landmarks.landmark) >= 5:
                # Obter as coordenadas normalizadas do dedo indicador
                h, w, c = frame.shape
                x1, y1 = int(landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * w), int(landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * h)
                x2, y2 = int(landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].x * w), int(landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y * h)
                
                # Calcular o ângulo entre o dedo indicador e o eixo vertical
                angle_rad = math.atan2(y1 - y2, x1 - x2)
                angle_deg = math.degrees(angle_rad)
                
                # Exibir o ângulo no terminal
                print(f"Ângulo formado pelo dedo indicador: {angle_deg:.2f} graus")
                
                ser.write(str(angle_deg).encode())
                time.sleep(0.1)  # Pausa para evitar envio muito rápido
    
    # Exibir o frame com as marcações das mãos
    cv2.imshow('Hand Tracking', frame)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
