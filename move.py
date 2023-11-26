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


if __name__ == "__main__":
    # using below functions to test funcionality and see what happens, not final logic
    game = ChessGame(True)
    legal_moves = game.legal_moves()
    board = game.board
    print(board)
    game.make_move("e4")
    print(board)
