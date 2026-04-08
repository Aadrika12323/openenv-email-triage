import random


random.seed(42)

EMAILS = [
    {"text": "Win a free iPhone now!", "sender": "spam@fake.com", "label": "spam"},
    {"text": "Project deadline is today!", "sender": "boss@company.com", "label": "urgent"},
    {"text": "Let's catch up this weekend", "sender": "friend@mail.com", "label": "normal"},
    {"text": "Invoice attached, please review", "sender": "finance@company.com", "label": "urgent"},
    {"text": "Limited time offer, buy now!", "sender": "ads@promo.com", "label": "spam"}
]


def generate_inbox(size=3):
    return random.sample(EMAILS, size)