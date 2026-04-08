from fastapi import FastAPI
from env.environment import EmailEnv

app = FastAPI()

env = None

@app.post("/reset")
def reset(task_id: str = "easy"):
    global env
    env = EmailEnv(task_id)
    obs = env.reset()
    return obs

@app.post("/step")
def step(action: dict):
    global env
    obs, reward, done, info = env.step(action)
    return {
        "observation": obs,
        "reward": reward,
        "done": done,
        "info": info
    }

@app.get("/state")
def state():
    global env
    return env.state()
