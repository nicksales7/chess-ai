from ai import ChessAI
import chess


class ChessGame:
    def __init__(self, color=True):
        self.color = color
        self.board = chess.Board()
        self.move = chess.Move()

    def legal_moves(self):
        legal = [str(move) for move in self.board.legal_moves]
        return legal

    def make_move(self, move):
        if not self.legal_moves():
            return None
        made_move = self.move(move[:2], move[2:])
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
    ai = ChessAI(game)
    game_over = False

    while not game_over:
        # Game logic
        print(game.board, "\n")
        user_move = input("Move: ")
        game.make_move(user_move)
        print(game.board, "\n")

        bot_move = game.random_move()
        game.make_move(bot_move)
        print(game.board, "\n")

        if game.game_over():
            game_over = True
            print(game.board, "\n")
        ### Main game logic to be done below
