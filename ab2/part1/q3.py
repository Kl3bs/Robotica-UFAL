import numpy as np

def ikine_scara(L1, L2, x, y, theta=0.0):
    """
    Inverse kinematics for a SCARA robot with specified position and orientation.

    Args:
    L1 (float): Length of the first link.
    L2 (float): Length of the second link.
    x (float): x-coordinate of the end-effector's final position.
    y (float): y-coordinate of the end-effector's final position.
    theta (float, optional): Orientation angle (in radians) of the end-effector (default: 0.0).

    Returns:
    tuple: A tuple containing joint configurations (theta1, theta2) in radians.
    """
    # Calculate intermediate variables
    r = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)

    # Calculate theta2
    cos_theta2 = (r**2 - L1**2 - L2**2) / (2 * L1 * L2)
    theta2 = np.arccos(cos_theta2)

    # Calculate theta1
    sin_theta2 = np.sin(theta2)
    A = L1 + L2 * cos_theta2
    B = L2 * sin_theta2
    theta1 = np.arctan2(y, x) - np.arctan2(B, A)

    return theta1, theta2

# Example usage
L1 = 1.0  # Length of the first link
L2 = 1.0  # Length of the second link
x_target = 1.5  # x-coordinate of the end-effector's final position
y_target = 0.5  # y-coordinate of the end-effector's final position
theta_target = 0.0  # Orientation angle (0 radians) of the end-effector

theta1, theta2 = ikine_scara(L1, L2, x_target, y_target, theta_target)
print(f"Joint configurations (theta1, theta2): ({theta1}, {theta2}) radians")
