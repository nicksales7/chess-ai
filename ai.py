import random


class ChessAI:
    def __init__(self, game):
        self.game = game

    def random_move(self):
        legal_moves = self.game.legal_moves()
        if not legal_moves:
            return None
        return str(random.choice(legal_moves))
