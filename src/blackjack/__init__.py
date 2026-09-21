from blackjack.components.game_class import Game

def main() -> None:
    game = Game()
    game.start_game()
    game.round()

if __name__ == "__main__":
    main()
