from ai import ChessAI
import chess


class ChessGame:
    def __init__(self, color=True):
        self.color = color
        self.board = chess.Board()

    def legal_moves(self):
        legal = [str(move) for move in self.board.legal_moves]
        return legal

    def make_move(self, move_str):
        try:
            move = self.board.parse_san(move_str)
            self.board.push(move)
        except ValueError:
            print("Invalid move")
            return False
        return True

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
    ai = ChessAI(game)
    game_over = False

    while not game_over:
        # Game logic
        print(game.board, "\n")
        user_move = input("Move: ")
        if not game.make_move(user_move):
            continue

        if game.game_over():
            game_over = True
            break

        ai_move = ai.random_move()
        if not game.make_move(ai_move):
            continue

        if game.game_over():
            game_over = True
            break

        print(game.board, "\n")
