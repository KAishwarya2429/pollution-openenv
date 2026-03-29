from config import MAX_STEPS, INITIAL_POLLUTION
from reward import get_reward
from logger import log

class PollutionEnv:
    def __init__(self, difficulty="hard"):
        self.difficulty = difficulty
        self.reset()

    def reset(self):
        self.pollution = INITIAL_POLLUTION
        self.steps = 0
        self.done = False
        return self._get_obs()

    def _get_obs(self):
        return {
            "pollution": self.pollution,
            "steps": self.steps,
            "difficulty": self.difficulty
        }

    def step(self, action):
        if self.done:
            return self._get_obs(), 0, True, {}

        self._apply_action(action)

        reward = get_reward(self.pollution, action)

        self.steps += 1

        self.done = self._check_done()

        log(self.pollution, action, reward)

        return self._get_obs(), reward, self.done, {}

    def _apply_action(self, action):
        actions = {
            "reduce_traffic": -10,
            "control_factory": -15,
            "plant_trees": -5
        }

        if action in actions:
            self.pollution += actions[action]
        else:
            self.pollution += 3  # penalty

        self.pollution = max(0, self.pollution)

    def _check_done(self):
        return self.pollution <= 20 or self.steps >= MAX_STEPS