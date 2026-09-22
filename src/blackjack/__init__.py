from blackjack.components.game_class import Game

def main() -> None:
    game = Game()
    game.start_game()
    game.run_rounds()

if __name__ == "__main__":
    main()
