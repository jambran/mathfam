from .player import Player
from typing import List


class Round:
    """
    - Features
        Keep track of the points
    """

    def __init__(self, players: List[Player]):
        self.players = players

    def play(self):
        return None
