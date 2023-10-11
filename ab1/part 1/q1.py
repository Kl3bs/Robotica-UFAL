import numpy as np
import matplotlib.pyplot as plt
from spatialmath.base import *
from setup import rot_3d


def rot_2d(angle=0, p=np.array([0.4, 0.4]) ):
     
    #Base 
    vector1 = np.array([1, 0])
    vector2 = np.array([0, 1]) 
    
    # Create figure and axis
    plt.figure()
    ax = plt.gca()

    # Plot the vectors
    ax.quiver(0, 0, vector1[0], vector1[1], angles='xy', scale_units='xy', scale=1, color='r', label='Vector 1')
    ax.quiver(0, 0, vector2[0], vector2[1], angles='xy', scale_units='xy', scale=1, color='r', label='Vector 2')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    # Set plot limits
    
    R = rot2((angle/180)*np.pi) # criando uma matriz de rotação SO(2)
 
    #trplot2(R) # visualizando como um frame rotacionado
    tranimate2(R) # animando a rotação
     
    plot_point(p, "ko", text="P")

    plotvol2([-1, 1, -1, 1]) # ajustando limites do plot
    plt.show()


def displayResult(message, result):
    print(message)
    print(result)
    print("\n")



def run2d(theta=30):
    
    vector = np.array([0,1])
       
    #As intial angle of X=0, then:
    R_matrix = np.matrix([[np.cos(theta), -np.sin(theta)],
                        [np.sin(theta), np.cos(theta)]])  
  
    
    R = np.dot(R_matrix,vector)
   

    displayResult("Rotation matrix * vector :", R)

    displayResult("Original matrix: ",R_matrix)

    R_inverse = np.linalg.inv(R_matrix)
    displayResult("Inverse matrix: ",R_inverse)

    displayResult("Original * Inverse :", np.dot(R_matrix,R_inverse))
    
    displayResult("Original determinant: ", np.linalg.det(R_matrix))
    
    displayResult("Inverse matrix determinant: ", np.linalg.det(R_inverse))
    

    rot_2d(angle=theta)
    
def run3d(theta=30):
    
    
    vector = np.array([0,1, 1])
       
    #As intial angle of X=0, then:
    R_matrix = np.matrix([[1,0,0],
                          [0, np.cos(theta), -np.sin(theta)],
                          [0,np.sin(theta), np.cos(theta)]]) 

    R = np.dot(R_matrix,vector)
    
    displayResult("Rotation matrix * vector :", R)


    displayResult("Original matrix: ",np.dot(R_matrix, vector) )

    R_inverse = np.linalg.inv(R_matrix)
    displayResult("Inverse matrix: ",R_inverse)

    displayResult("Original * Inverse :", np.dot(R_matrix,R_inverse))
    
    displayResult("Original determinant: ", np.linalg.det(R_matrix))
    
    displayResult("Inverse matrix determinant: ", np.linalg.det(R_inverse))
    

    rot_3d()
    
run2d()
#run3d()