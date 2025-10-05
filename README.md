# Snake Game - Multiplayer

A classic Snake game implementation with multiplayer support built using Pygame. Two players can compete simultaneously on the same screen to collect food and grow their snakes.

## Features

- **Multiplayer Mode**: Two players can play simultaneously
- **Collision Detection**: Snakes die when hitting themselves or each other
- **Score Tracking**: Real-time score display for both players
- **Responsive Controls**: Separate keyboard controls for each player
- **Wrap-around Edges**: Snakes wrap around screen edges
- **Restart Functionality**: Quick restart with spacebar after game over

## Requirements

- Python 3.x
- Pygame

## Installation

1. Make sure you have Python installed on your system

2. Install Pygame using pip:
```bash
pip install pygame
```

## How to Play

Run the game:
```bash
python snake_game.py
```

### Controls

**Player 1 (Green Snake)**:
- Arrow Keys: Move up, down, left, right

**Player 2 (Blue Snake)**:
- W: Move up
- S: Move down
- A: Move left
- D: Move right

### Game Rules

1. Control your snake to collect red food items
2. Each food item increases your snake's length by 1 and adds 10 points to your score
3. Avoid colliding with your own body or the opponent's snake
4. If both players die simultaneously, the game is a draw
5. Press SPACE to restart after game over

## Game Settings

The game can be customized by modifying the following constants in `snake_game.py`:

- `WINDOW_WIDTH`: Width of the game window (default: 800)
- `WINDOW_HEIGHT`: Height of the game window (default: 600)
- `GRID_SIZE`: Size of each grid cell (default: 20)
- `clock.tick()`: Game speed in FPS (default: 10)

## Screenshots

Game Window: 800x600 pixels
Grid: 40x30 cells
Snake Colors: Green (Player 1), Blue (Player 2)
Food Color: Red

## Winning Conditions

- Player 1 wins if Player 2's snake dies while Player 1 is alive
- Player 2 wins if Player 1's snake dies while Player 2 is alive
- Draw if both snakes die at the same time

## License

This project is open source and available for educational purposes.

## Future Enhancements

Potential features to add:
- Single player mode with AI opponent
- Different difficulty levels
- Power-ups and special food items
- Obstacles and maze elements
- High score persistence
- Sound effects and background music
