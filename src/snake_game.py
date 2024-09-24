import sys
from lib.game import Game
from lib.snake import Direction, SnakeException

if __name__ == "__main__":
    game = Game()

    def move(direction: Direction, snake):
        snake.move(direction)
        print(direction)
        print(snake)

    try:
        print("New Game")
        game.restart()
        print(game.snake)

        move(Direction.DOWN, game.snake)
        move(Direction.UP, game.snake)
    except SnakeException as e:
        sys.stdout.write(f"Game over: {e}\n")

    try:
        print("\nNew Game")
        game.restart()
        print(game.snake)

        move(Direction.DOWN, game.snake)
        move(Direction.DOWN, game.snake)
        move(Direction.DOWN, game.snake)
        move(Direction.RIGHT, game.snake)
        move(Direction.RIGHT, game.snake)
        move(Direction.UP, game.snake)
        move(Direction.UP, game.snake)
        move(Direction.LEFT, game.snake)
        move(Direction.UP, game.snake)
        move(Direction.LEFT, game.snake)
    except SnakeException as e:
        sys.stdout.write(f"Game over: {e}\n")
