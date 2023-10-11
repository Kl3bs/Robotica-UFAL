import matplotlib.pyplot as plt
import numpy as np
from roboticstoolbox import ctraj, xplot,  DHRobot, RevoluteDH
from spatialmath import SE3
import time


def dh_rr():

    link1 = RevoluteDH(a=1)
    link2 = RevoluteDH(a=1)

    robot_dh = DHRobot([link1, link2], name="RR")

    return robot_dh


def path():
    rr_robot = dh_rr()

    q0 = np.array([-np.pi, np.pi/2])

    t1 = rr_robot.fkine(q0)
    print("Initial pose:\n", t1)

    t2 = SE3.Trans(0, -0.5, 0) @ t1
    print("Final pose:\n", t2)

    t = np.arange(0, 5, 0.02)
    ts = ctraj(t1, t2, t)

    xplot(t, ts.t, labels="x y z")

    xplot(t, ts.rpy("xyz"), labels="roll pitch yaw")

    plt.show()
    return ts


def resolved_rate_control_2r(L1=1, L2=1):
    robot = dh_rr()
    trajectory = path()
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
    plots(joint_angles_list, error_list, time_steps)
