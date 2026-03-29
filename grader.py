def grade(state, task):
    target = task["target"]
    return state["pollution"] <= target