"""LOLIN_S3_MINI_PRO
"""

from machine import Pin


class Buttons:
    """Buttons class."""

    def __init__(self):
        self.name = "LOLIN_S3_MINI_PRO"
        self.left = 0
        self.right = 0
        self.hyper = 0
        self.thrust = 0
        self.fire = 0
