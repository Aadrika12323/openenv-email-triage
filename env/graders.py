def grade_action(email, action, task_id):
    reward = 0.0

    
    if action["label"] == email["label"]:
        reward += 0.5

    
    if task_id in ["medium", "hard"]:
        response = action.get("response", "").lower()

        if email["label"] == "urgent" and "soon" in response:
            reward += 0.3
        elif email["label"] == "normal" and len(response) > 5:
            reward += 0.2
        elif email["label"] == "spam" and response == "":
            reward += 0.2

   
    if action["label"] == "spam" and email["label"] != "spam":
        reward -= 0.2

    return max(0.0, min(reward, 1.0))