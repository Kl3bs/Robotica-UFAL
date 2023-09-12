import numpy as np

#Angle in degrees
t1 = 90 
t2 = 0

#Angles converted (radian)
t1= (t1/180)*np.pi
t2= (t2/180)*np.pi

#Rotation from 0 to 1
R0_1 = np.matrix([[np.cos(t1), -np.sin(t1), 0],
                 [np.sin(t1), np.cos(t1), 0],
                 [0,0,1]])

#Rotation from 1 to 2
R1_2 = np.matrix([[np.cos(t2), -np.sin(t2), 0],
                 [np.sin(t2), np.cos(t2), 0],
                 [0,0,1]])

#Rotation from 0 to 2
R0_2 = np.dot(R0_1, R1_2)

print(R0_2)