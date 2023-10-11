from setup import  *

theta = 90
angle = (theta/180)*np.pi

#First rotation matrix (Frame A)
R_A = rotx(angle)  @ roty(angle)


#Second rotation matrix (Frame B)
R_B = roty(angle) @ rotx(angle)

# print(R_A)

# print(R_B)


print(np.dot(R_A, R_B))