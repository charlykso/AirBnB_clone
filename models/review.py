#!/usr/bin/python3
"""contains Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """temp"""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        init
        """
        super().__init__(*args, **kwargs)
