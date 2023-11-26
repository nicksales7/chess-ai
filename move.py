import chess
import random


class ChessGame:
    def __init__(self, color=True):
        self.color = color
        self.board = chess.Board()

    def legal_moves(self):
        legal = [str(move) for move in self.board.legal_moves]
        return legal

    def random_move(self):
        move = str(random.choice(self.legal_moves()))
        return move

    def make_move(self, move):
        made_move = self.board.push_san(move)
        return made_move

    def game_over(self):
        if (
            self.board.is_checkmate()
            or self.board.is_stalemate()
            or self.board.has_insufficient_material(self.color)
            or self.board.is_seventyfive_moves()
            or self.board.is_fivefold_repetition()
        ):
            return True
        else:
            return False


if __name__ == "__main__":
    game = ChessGame(True)
    game_over = False

    while not game_over:
        # Game logic

        if game.game_over():
            game_over = True
            print(game.board)
        ### Main game logic to be done below
