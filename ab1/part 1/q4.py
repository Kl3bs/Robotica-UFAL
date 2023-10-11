from setup import *


def displayResult(message, result):
    print(message)
    print(result)
    print("\n")

vector = [0,1,2,1] 
T = transl(0, 2, 0) @ trotx(np.pi / 2) @ transl(0, 4, 0) 

 
trplot(T, frame="A", color="red")
tranimate(T)

#Vector transformation
displayResult("Homogeneous transformation matrix * Vector :" , T@vector)


#Inverse * Original
displayResult("Inverse * Original matrix :",  np.dot(np.linalg.inv(T), T))

#Original * Inverse
displayResult("Original matrix * Inverse: ", np.dot(T , np.linalg.inv(T)))

# plt.show()