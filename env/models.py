from pydantic import BaseModel
from typing import List, Dict


class Observation(BaseModel):
    inbox: List[Dict]
    current_index: int


class Action(BaseModel):
    label: str
    response: str = ""


class Reward(BaseModel):
    score: float