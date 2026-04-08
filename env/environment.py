from env.data import generate_inbox
from env.graders import grade_action


class EmailEnv:
    def __init__(self, task_id="easy"):
        self.task_id = task_id
        self.inbox = []
        self.current_index = 0
        self.total_reward = 0

    def reset(self):
        size = {"easy": 2, "medium": 3, "hard": 5}[self.task_id]

        self.inbox = generate_inbox(size)
        self.current_index = 0
        self.total_reward = 0

        return self._get_obs()

    def _get_obs(self):
        return {
            "inbox": self.inbox,
            "current_index": self.current_index
        }

    def step(self, action):
        email = self.inbox[self.current_index]

        reward = grade_action(email, action, self.task_id)
        self.total_reward += reward

        self.current_index += 1
        done = self.current_index >= len(self.inbox)

        observation = self._get_obs()

        info = {
            "step": self.current_index,
            "total_reward": self.total_reward
        }

        return observation, reward, done, info

    def state(self):
        return {
            "inbox": self.inbox,
            "index": self.current_index,
            "total_reward": self.total_reward
        }