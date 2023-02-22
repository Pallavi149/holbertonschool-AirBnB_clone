#!/usr/bin/pyhton3
"""
  The City class.
"""


from models.base_model import BaseModel


class City(BaseModel):
    """Constructs a City."""
    state_id = ""
    name = ""
