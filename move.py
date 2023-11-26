import chess
import random


class ChessGame:
    def __init__(self, color, board):
        self.color = color
        self.board = chess.Board()

    def legal_moves(self):
        legal = [str(move) for move in self.board.legal_moves]
        return legal

    def random_move(self, legal_move):
        move = str(random.choice(legal_move))
        return move


if __name__ == "__main__":
    board = ChessGame.chess_board()
    print(ChessGame.legal_moves(board))
'''
    game_over = False
    while game_over == False:
        if board.is_checkmate() == False:
            for i in legal_moves(board):
                print("Legal Move", i)
            user_move = input("Move: ")
            board.push_san(user_move)
            print(board, "\n")

            print(legal_moves(board))
            random_move = make_move(board, legal_moves(board))
            board.push_san(random_move)
            print(board, "\n")
        else:
            game_over = True
'''
