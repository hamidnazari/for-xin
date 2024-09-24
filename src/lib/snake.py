from .direction import Direction
from .position import Position


class SnakeException(Exception):
    pass


class Snake:
    def __init__(self, starting_size: int = 3, grows_every_blocks: int = 5):
        self.grows_every_blocks = grows_every_blocks
        self.positions: list[Position] = []

        for x in range(starting_size):
            self.positions.append(Position(x, 0))

        self.step_counter: int = 0

    def move(self, direction: Direction):
        head = self.positions[0]

        self.step_counter += 1

        if self.step_counter > 0 and self.step_counter % self.grows_every_blocks == 0:
            # keep the last body block, i.e. grow
            body = self.positions
        else:
            # drop the last body block
            body = self.positions[:-1]

        if direction == Direction.UP:
            head = Position(head.x, head.y - 1)
        elif direction == Direction.DOWN:
            head = Position(head.x, head.y + 1)
        elif direction == Direction.LEFT:
            head = Position(head.x - 1, head.y)
        elif direction == Direction.RIGHT:
            head = Position(head.x + 1, head.y)

        positions = [head]
        positions.extend(body)
        self.positions = positions

        self.check_collision()

    def check_collision(self):
        positions_set = set(self.positions)
        if len(self.positions) != len(positions_set):
            raise SnakeException("Snake collided with itself")

    def __repr__(self) -> str:
        return f"Snake {len(self.positions)}({self.positions})"
