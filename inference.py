import os
import json
import sys
from openai import OpenAI
from env.environment import EmailEnv

os.environ["OPENAI_API_KEY"] = "REPLACE_WITH_YOUR_KEY"

API_BASE_URL = os.getenv("API_BASE_URL", "https://api.groq.com/openai/v1")
MODEL = os.getenv("MODEL_NAME", "llama-3.1-8b-instant")

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY", "").strip(), 
    base_url=API_BASE_URL
)


def call_llm(email):
    prompt = f"""
You are an email assistant.
Email: {email['text']}
Sender: {email['sender']}
Return ONLY valid JSON:
{{
  "label": one of ["spam", "urgent", "normal"],
  "response": "text"
}}
Rules:
- spam → response MUST be ""
- urgent → include "soon" or "immediately"
- normal → polite short reply
Do NOT include anything except JSON.
"""

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        text = response.choices[0].message.content.strip()

        data = json.loads(text)

        label = data.get("label", "normal").lower().strip()

        
        if label not in ["spam", "urgent", "normal"]:
            label = "normal"

        response_text = data.get("response", "")

        
        if label == "spam":
            response_text = ""
        elif label == "urgent" and ("soon" not in response_text.lower() and "immediately" not in response_text.lower()):
            response_text += " I will handle this immediately."

        return {
            "label": label,
            "response": response_text
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
    lock_file = "/tmp/executed.lock"

    
    if os.path.exists(lock_file):
        sys.exit(0)

    
    with open(lock_file, "w") as f:
        f.write("done")

    for task in ["easy", "medium", "hard"]:
        run_task(task)

    sys.exit(0)



