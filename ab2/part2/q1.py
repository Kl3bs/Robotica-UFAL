import time
import numpy as np
import matplotlib.pyplot as plt
from roboticstoolbox import ctraj
from spatialmath import SE3
from spatialmath.base import *
from roboticstoolbox import jsingu, xplot, ET2, DHRobot, RevoluteDH, PrismaticDH


def plots(qs, erro, t):

    plt.plot(erro, t)
    plt.xlabel('Tempo')
    plt.ylabel('Erro')
    plt.legend()
    plt.title("Erro X Tempo")
    plt.show()
    # Extraia as posições de cada junta em listas separadas
    theta1_positions = [pos[0] for pos in qs]
    theta2_positions = [pos[1] for pos in qs]

    # Crie um gráfico para a junta 1
    plt.figure(figsize=(10, 6))
    plt.subplot(2, 1, 1)
    plt.plot(t, theta1_positions, label='Junta 1')
    plt.xlabel('Tempo')
    plt.ylabel('Ângulo da Junta 1 (theta1)')
    plt.legend()

    # Crie um gráfico para a junta 2
    plt.subplot(2, 1, 2)
    plt.plot(t, theta2_positions, label='Junta 2')
    plt.xlabel('Tempo')
    plt.ylabel('Ângulo da Junta 2 (theta2)')
    plt.legend()

    # Exiba os gráficos
    plt.tight_layout()
    plt.title("Junta x Tempo")
    plt.show()


def rr_robot(L1=1, L2=1):

    e1 = RevoluteDH(a=L1)
    e2 = RevoluteDH(a=L2)

    rob = DHRobot([e1, e2], name='RR')
    return rob


def trajetoria():
    rr = rr_robot()

    q0 = np.array([-np.pi / 3, np.pi / 2])
    # print(q0)

    TE1 = rr.fkine(q0)
    print("Pose inicial:\n", TE1)
    TE2 = SE3.Trans(0, -0.5, 0) @ TE1
    print("Pose final:\n", TE2)

    t = np.arange(0, 5, 0.02)
    # print(t)

    Ts = ctraj(TE1, TE2, t)
    # print(Ts)
    xplot(t, Ts.t, labels="x y z")
    xplot(t, Ts.rpy("xyz"), labels="roll pitch yaw")
    plt.show()
    return Ts


def resolved_rate_control_2r(L1=1, L2=1):
    robot = rr_robot()
    trajectory = trajetoria()
    time_steps = np.arange(0, 5, 0.02)
    control_update_time = 0.01
    joint_angle_1 = 0.0
    joint_angle_2 = 0.0
    error_list = []
    joint_angles_list = []

    for i in range(len(trajectory)):
        end_effector_pose = trajectory[i]
        end_effector_x = end_effector_pose.t[0]
        end_effector_y = end_effector_pose.t[1]
        cartesian_error_x = end_effector_x - \
            (L1 * np.cos(joint_angle_1) + L2 *
             np.cos(joint_angle_1 + joint_angle_2))
        cartesian_error_y = end_effector_y - \
            (L1 * np.sin(joint_angle_1) + L2 *
             np.sin(joint_angle_1 + joint_angle_2))

        jacobian = np.array([[-L1 * np.sin(joint_angle_1) - L2 * np.sin(joint_angle_1 + joint_angle_2),
                              -L2 * np.sin(joint_angle_1 + joint_angle_2)],
                             [L1 * np.cos(joint_angle_1) + L2 * np.cos(joint_angle_1 + joint_angle_2),
                              L2 * np.cos(joint_angle_1 + joint_angle_2)]])

        determinant = np.linalg.det(jacobian)
        if abs(determinant) < 1e-6:
            regularization_lambda = 0.01
            jacobian_regularized = jacobian + \
                regularization_lambda * np.identity(jacobian.shape[0])
            joint_velocities = np.linalg.solve(
                jacobian_regularized, np.array([cartesian_error_x, cartesian_error_y]))
        else:
            joint_velocities = np.linalg.solve(
                jacobian, np.array([cartesian_error_x, cartesian_error_y]))

        joint_angle_1 += joint_velocities[0] * control_update_time
        joint_angle_2 += joint_velocities[1] * control_update_time

        joint_angles = [joint_angle_1, joint_angle_2]
        joint_angles_list.append(joint_angles)

        end_effector_position = robot.fkine(joint_angles).t[:2]
        error = np.linalg.norm(end_effector_position - trajectory[-1].t[:2])
        error_list.append(error)

        time.sleep(control_update_time)

    print("Joint Angles = {}".format([joint_angle_1, joint_angle_2]))
    robot.teach([joint_angle_1, joint_angle_2])


resolved_rate_control_2r()
