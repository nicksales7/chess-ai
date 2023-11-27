from ai import ChessAI
import chess


class ChessGame:
    def __init__(self, color=True):
        self.color = color
        self.board = chess.Board()

    def legal_moves(self):
        return [str(move) for move in self.board.legal_moves]

    def make_move(self, move_str):
        try:
            move = self.board.parse_san(move_str)
            self.board.push(move)
        except ValueError:
            print("Invalid move")
            return False
        return True

    def game_over(self):
        conditions = {
            self.board.is_checkmate: "Checkmate!",
            self.board.is_stalemate: "Draw by Stalemate",
            lambda: self.board.has_insufficient_material(
                self.color
            ): "Draw by insufficient material",
            self.board.is_seventyfive_moves: "Draw by seventyfive move rule",
            self.board.is_fivefold_repetition: "Draw by fivefold repetition",
        }
        for condition, message in conditions.items():
            if condition():
                print(message)
                return True
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

    print(game.board, "\n")
