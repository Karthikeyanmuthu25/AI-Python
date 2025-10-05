import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Game constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Snake:
    def __init__(self, start_pos, color, player_num=1):
        self.length = 1
        self.positions = [start_pos]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = color
        self.score = 0
        self.player_num = player_num
        self.alive = True

    def get_head_position(self):
        return self.positions[0]

    def update(self, other_snake=None):
        if not self.alive:
            return

        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + x) % GRID_WIDTH), ((cur[1] + y) % GRID_HEIGHT))

        # Check collision with self
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.alive = False
            return

        # Check collision with other snake
        if other_snake and other_snake.alive and new in other_snake.positions:
            self.alive = False
            return

        self.positions.insert(0, new)
        if len(self.positions) > self.length:
            self.positions.pop()

    def reset(self, start_pos):
        self.length = 1
        self.positions = [start_pos]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.score = 0
        self.alive = True

    def render(self, surface):
        if not self.alive:
            return
        for p in self.positions:
            rect = pygame.Rect((p[0] * GRID_SIZE, p[1] * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, self.color, rect)
            pygame.draw.rect(surface, BLACK, rect, 1)

    def handle_keys(self, event):
        if not self.alive:
            return
        if event.type == pygame.KEYDOWN:
            # Player 1 controls (Arrow keys)
            if self.player_num == 1:
                if event.key == pygame.K_UP and self.direction != DOWN:
                    self.direction = UP
                elif event.key == pygame.K_DOWN and self.direction != UP:
                    self.direction = DOWN
                elif event.key == pygame.K_LEFT and self.direction != RIGHT:
                    self.direction = LEFT
                elif event.key == pygame.K_RIGHT and self.direction != LEFT:
                    self.direction = RIGHT
            # Player 2 controls (WASD)
            elif self.player_num == 2:
                if event.key == pygame.K_w and self.direction != DOWN:
                    self.direction = UP
                elif event.key == pygame.K_s and self.direction != UP:
                    self.direction = DOWN
                elif event.key == pygame.K_a and self.direction != RIGHT:
                    self.direction = LEFT
                elif event.key == pygame.K_d and self.direction != LEFT:
                    self.direction = RIGHT

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

    def render(self, surface):
        rect = pygame.Rect((self.position[0] * GRID_SIZE, self.position[1] * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, self.color, rect)
        pygame.draw.rect(surface, BLACK, rect, 1)

def main():
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Snake Game - Multiplayer')

    # Create two snakes at different positions
    snake1 = Snake((GRID_WIDTH // 4, GRID_HEIGHT // 2), GREEN, 1)
    snake2 = Snake((3 * GRID_WIDTH // 4, GRID_HEIGHT // 2), BLUE, 2)
    food = Food()

    font = pygame.font.Font(None, 36)
    game_over_font = pygame.font.Font(None, 72)

    game_over = False
    winner = None

    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if game_over and event.key == pygame.K_SPACE:
                    # Reset game
                    snake1.reset((GRID_WIDTH // 4, GRID_HEIGHT // 2))
                    snake2.reset((3 * GRID_WIDTH // 4, GRID_HEIGHT // 2))
                    food.randomize_position()
                    game_over = False
                    winner = None
                else:
                    snake1.handle_keys(event)
                    snake2.handle_keys(event)

        if not game_over:
            # Update snakes
            snake1.update(snake2)
            snake2.update(snake1)

            # Check if snake1 ate food
            if snake1.alive and snake1.get_head_position() == food.position:
                snake1.length += 1
                snake1.score += 10
                food.randomize_position()

            # Check if snake2 ate food
            if snake2.alive and snake2.get_head_position() == food.position:
                snake2.length += 1
                snake2.score += 10
                food.randomize_position()

            # Check for game over
            if not snake1.alive and not snake2.alive:
                game_over = True
                winner = "Draw"
            elif not snake1.alive:
                game_over = True
                winner = "Player 2"
            elif not snake2.alive:
                game_over = True
                winner = "Player 1"

        # Drawing
        screen.fill(BLACK)
        snake1.render(screen)
        snake2.render(screen)
        food.render(screen)

        # Display scores
        score1_text = font.render(f'P1: {snake1.score}', True, GREEN)
        score2_text = font.render(f'P2: {snake2.score}', True, BLUE)
        screen.blit(score1_text, (10, 10))
        screen.blit(score2_text, (WINDOW_WIDTH - 150, 10))

        # Display game over message
        if game_over:
            if winner == "Draw":
                game_over_text = game_over_font.render("Draw!", True, WHITE)
            else:
                game_over_text = game_over_font.render(f'{winner} Wins!', True, WHITE)
            restart_text = font.render('Press SPACE to restart', True, WHITE)

            text_rect = game_over_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50))
            restart_rect = restart_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50))

            screen.blit(game_over_text, text_rect)
            screen.blit(restart_text, restart_rect)

        pygame.display.update()
        clock.tick(10)

if __name__ == '__main__':
    main()
