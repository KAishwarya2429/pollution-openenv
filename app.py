import gradio as gr
from env import PollutionEnv
from agent import Agent

env = PollutionEnv()
agent = Agent()

def run_simulation():
    state = env.reset()
    done = False
    logs = []

    while not done:
        action = agent.act(state)
        state, reward, done, _ = env.step(action)
        logs.append(f"Action: {action} | Pollution: {state['pollution']} | Reward: {reward}")

    logs.append("\nFINAL RESULT:")
    logs.append(f"Pollution: {state['pollution']}")
    logs.append("Status: PASS ✅" if state['pollution'] <= 30 else "FAIL ❌")

    return "\n".join(logs)

demo = gr.Interface(
    fn=run_simulation,
    inputs=[],
    outputs="text",
    title="🌍 AI Pollution Control OpenEnv",
    description="AI agent reduces pollution step-by-step"
)

demo.launch()