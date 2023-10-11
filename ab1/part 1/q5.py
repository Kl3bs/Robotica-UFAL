from setup import *

T = transl(2, 0, 0) @ trotx(np.pi / 2) @ transl(0, 1, 0) 
T_inv = np.linalg.inv(T)

result = np.dot(T, T_inv)

identity_matrix = np.identity(T.shape[0])

if np.array_equal(result, identity_matrix):
    print("T * T^(-1) é igual à matriz identidade:")
    print(result)
else:
    print("T * T^(-1) não é igual à matriz identidade.")

 
