# Smart Email Assistant (OpenEnv)

## Description
Simulates real-world email triage tasks including classification and response generation.

## Tasks
- Easy: classify emails
- Medium: classify + respond
- Hard: full inbox handling

## Observation Space
{
  "inbox": [...],
  "current_index": int
}

## Action Space
{
  "label": "spam | urgent | normal",
  "response": "string"
}

## Reward
- Correct classification → +0.5
- Response quality → +0.2 to +0.3
- Penalty for wrong classification

## Run
python inference.py

## Docker
docker build -t email-env .
docker run email-env