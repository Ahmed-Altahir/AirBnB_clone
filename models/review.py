#!/usr/bin/python3
"""review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """handling review objects"""

    place_id = ""
    user_id = ""
    text = ""
