from models.Game import Game

INTERACTIVE_MODE = False


def main() -> None:
    names = ['lucas', 'john', 'mike']
    game = Game(names, INTERACTIVE_MODE)
    game.play()


if __name__ == "__main__":
    main()
