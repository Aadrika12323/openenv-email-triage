import os
import json
from openai import OpenAI
from env.environment import EmailEnv


os.environ["OPENAI_API_KEY"] = "REPLACE_WITH_YOUR_KEY"
os.environ["API_BASE_URL"] = "https://api.groq.com/openai/v1"
os.environ["MODEL_NAME"] = "llama-3.1-8b-instant"

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("API_BASE_URL")
)

MODEL = os.getenv("MODEL_NAME")


def call_llm(email):
    prompt = f"""
You are an email assistant.

Email: {email['text']}
Sender: {email['sender']}

Return ONLY valid JSON:
{{
  "label": "spam | urgent | normal",
  "response": "text"
}}
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    text = response.choices[0].message.content.strip()

    try:
        data = json.loads(text)
        return {
            "label": data.get("label", "normal"),
            "response": data.get("response", "")
        }
    except:
        return {"label": "normal", "response": ""}


def run_task(task_id):
    env = EmailEnv(task_id)
    obs = env.reset()

    print("[START]")
    print(f"task_id={task_id}")

    done = False

    while not done:
        idx = obs["current_index"]
        email = obs["inbox"][idx]

        action = call_llm(email)

        obs, reward, done, info = env.step(action)

        print("[STEP]")
        print(f"action={action}")
        print(f"reward={reward}")

    print("[END]")
    print(f"score={info['total_reward']}")


if __name__ == "__main__":
    for task in ["easy", "medium", "hard"]:
        run_task(task)