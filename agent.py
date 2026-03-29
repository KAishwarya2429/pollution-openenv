import random

class Agent:
    def act(self, state):
        if state["pollution"] > 80:
            return "control_factory"
        elif state["pollution"] > 50:
            return random.choice(["reduce_traffic", "plant_trees"])
        else:
            return "plant_trees"