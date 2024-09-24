Test run:

```
$ python src/snake_game.py
New Game
Snake 3([Position(0, 0), Position(1, 0), Position(2, 0)])
Direction.DOWN
Snake 3([Position(0, 1), Position(0, 0), Position(1, 0)])
Direction.UP
Game over: Snake collided with itself

New Game
Snake 3([Position(0, 0), Position(1, 0), Position(2, 0)])
Direction.DOWN
Snake 3([Position(0, 1), Position(0, 0), Position(1, 0)])
Direction.DOWN
Snake 3([Position(0, 2), Position(0, 1), Position(0, 0)])
Direction.DOWN
Snake 3([Position(0, 3), Position(0, 2), Position(0, 1)])
Direction.RIGHT
Snake 3([Position(1, 3), Position(0, 3), Position(0, 2)])
Direction.UP
Snake 4([Position(1, 2), Position(1, 3), Position(0, 3), Position(0, 2)])
Direction.UP
Snake 4([Position(1, 1), Position(1, 2), Position(1, 3), Position(0, 3)])
Direction.LEFT
Snake 4([Position(0, 1), Position(1, 1), Position(1, 2), Position(1, 3)])
Direction.UP
Snake 4([Position(0, 0), Position(0, 1), Position(1, 1), Position(1, 2)])
Direction.RIGHT
Snake 4([Position(1, 0), Position(0, 0), Position(0, 1), Position(1, 1)])
Direction.RIGHT
Snake 5([Position(2, 0), Position(1, 0), Position(0, 0), Position(0, 1), Position(1, 1)])
Direction.DOWN
Snake 5([Position(2, 1), Position(2, 0), Position(1, 0), Position(0, 0), Position(0, 1)])
Direction.LEFT
Snake 5([Position(1, 1), Position(2, 1), Position(2, 0), Position(1, 0), Position(0, 0)])
Direction.UP
Game over: Snake collided with itself
```
