import chess
import random


class ChessGame:
    def __init__(self, color):
        self.color = color

    def chess_board():
        chess_board = chess.Board()
        return chess_board

    def legal_moves(board):
        legal = [str(move) for move in board.legal_moves]
        return legal


def make_move(board, legal_move):
    rand_move = str(random.choice(legal_moves))
    return rand_move


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
