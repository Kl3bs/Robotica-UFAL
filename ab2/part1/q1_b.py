import numpy as np

def ikine_rr(L1, L2, x, y):
    """
    Args:
    L1 (float): Length of the first link.
    L2 (float): Length of the second link.
    x (float): x-coordinate of the end-effector's final position.
    y (float): y-coordinate of the end-effector's final position.

    Returns:
    tuple: A tuple containing joint configurations (q1, q2) in radians.
    """
    # Calculate the distance from the end-effector to the origin (base of the manipulator)
    distance = np.sqrt(x**2 + y**2)

    # Check if the desired position is within the manipulator's reach
    if distance > L1 + L2:
        raise ValueError("Out of range!")

    # Calculate the q2 angle using the law of cosines
    cos_q2 = (x**2 + y**2 - L1**2 - L2**2) / (2 * L1 * L2)
    q2 = np.arccos(cos_q2)

    # Calculate the q1 angle using the arctangent
    q1 = np.arctan2(y, x) - np.arctan2(L2 * np.sin(q2), L1 + L2 * np.cos(q2))

    return q1, q2

# Example usage
L1 = 1.0  # Length of the first link
L2 = 1.0  # Length of the second link
x_target = 1.5  # x-coordinate of the end-effector's final position
y_target = 0.5  # y-coordinate of the end-effector's final position

q1, q2 = ikine_rr(L1, L2, x_target, y_target)
print(f"Joint configurations (q1, q2): ({q1}, {q2}) radians")
