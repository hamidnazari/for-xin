from .snake import Snake


class Game:
    def __init__(self, width: int = 16, height: int = 32):
        self.width = width
        self.height = height

        self.snake = Snake()

    def restart(self):
        self.snake = Snake()
