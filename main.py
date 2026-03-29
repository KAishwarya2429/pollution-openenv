from env import PollutionEnv
from agent import Agent
from tasks import TASKS
from grader import grade

env = PollutionEnv(difficulty="hard")
agent = Agent()

task = TASKS["hard"]

state = env.reset()

done = False

while not done:
    action = agent.act(state)
    state, reward, done, _ = env.step(action)

# Final Evaluation
result = grade(state, task)

print("\nFINAL RESULT:", "PASS ✅" if result else "FAIL ❌")
print("Final Pollution:", state["pollution"])