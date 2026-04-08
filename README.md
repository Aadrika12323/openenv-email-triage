---
title: OpenEnv Email Triage
emoji: 📧
colorFrom: blue
colorTo: purple
sdk: docker
app_file: app.py
pinned: false
---

# 📧 OpenEnv Email Triage Environment

## 🚀 Description
This project implements a real-world **email triage environment** using the OpenEnv specification.  
An AI agent classifies emails (spam, urgent, normal) and generates responses.

---

## 🧠 Tasks

### Easy
- Classify emails (spam / normal)

### Medium
- Classify + generate response

### Hard
- Full inbox processing with mixed scenarios

---

## 📥 Observation Space

```json
{
  "inbox": [
    {"text": "string", "sender": "string"}
  ],
  "current_index": 0
}
