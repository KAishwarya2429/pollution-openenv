def get_reward(pollution, action):
    reward = 0

    # Action-based reward
    if action == "control_factory":
        reward += 15
    elif action == "reduce_traffic":
        reward += 10
    elif action == "plant_trees":
        reward += 5
    else:
        reward -= 5

    # Pollution-based shaping
    if pollution < 30:
        reward += 25
    elif pollution < 50:
        reward += 15
    elif pollution < 70:
        reward += 5

    # Penalty for high pollution
    if pollution > 80:
        reward -= 10

    return reward