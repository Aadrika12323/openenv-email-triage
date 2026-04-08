def get_task(task_id):
    if task_id == "easy":
        return {
            "observation": {
                "email_id": 1,
                "email_text": "You won a lottery! Click here!",
                "sender": "unknown@spam.com"
            },
            "label": "spam"
        }

    elif task_id == "medium":
        return {
            "observation": {
                "email_id": 2,
                "email_text": "Meeting rescheduled to tomorrow morning.",
                "sender": "boss@company.com"
            },
            "label": "urgent"
        }

    elif task_id == "hard":
        return {
            "observation": {
                "email_id": 3,
                "email_text": "Can you send the project report?",
                "sender": "manager@company.com"
            },
            "label": "normal",
            "expected_response": "Sure, I will send the report soon."
        }