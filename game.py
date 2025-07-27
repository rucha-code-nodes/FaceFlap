


import pygame
from modules.head_control import HeadController

class FlappyBirdGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((608, 457))  # Screen size (width x height)
        self.clock = pygame.time.Clock()

        # Load game assets
        self.bird = pygame.image.load('D:\\Handicap Game\\assets\\b.png').convert_alpha()
        self.background = pygame.image.load('D:\\Handicap Game\\assets\\background.png').convert_alpha()
        self.pipe = pygame.image.load('D:\\Handicap Game\\assets\\pipe.png').convert_alpha()

        self.bird_y = 250  # Initial bird y position
        self.bird_x = 50   # Initial bird x position
        self.bird_movement_y = 0
        self.bird_movement_x = 0
        self.gravity = 1  # Simulated gravity effect

        self.pipe_x = 800  # Start the pipe offscreen to the right
        self.pipe_speed = -3  # Speed at which the pipe moves to the left
        self.pipe_gap = 150  # The gap between the top and bottom pipes

        self.score = 0  # Initialize the score
        self.font = pygame.font.Font(None, 36)  # Score font
        self.game_over_font = pygame.font.Font(None, 72)  # "Game Over" message font

        self.game_over = False  # Game over flag
        self.bird_passed_pipe = False  # Flag to track if bird passed the pipe
        self.bird_visible = True  # Flag to control bird visibility after collision
        self.head_controller = HeadController()

    def run_game(self):
        running = True
        while running:
            self.screen.blit(self.background, (0, 0))  # Draw background

            # Handle Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if not self.game_over:
                # Get head movement
                movement_direction = self.head_controller.get_head_movement()

                # Control the bird based on head movement
                if movement_direction == 'up':
                    self.bird_movement_y = -5  # Move bird up
                elif movement_direction == 'down':
                    self.bird_movement_y = 5  # Move bird down
                else:
                    self.bird_movement_y = 1  # Natural falling movement

                if movement_direction == 'right':
                    self.bird_movement_x = 5  # Move bird right
                elif movement_direction == 'left':
                    self.bird_movement_x = -5  # Move bird left
                else:
                    self.bird_movement_x = 0  # Stop horizontal movement

                # Update bird position
                self.bird_y += self.bird_movement_y
                self.bird_x += self.bird_movement_x

                # Boundary control for bird movement
                if self.bird_y < 0:
                    self.bird_y = 0
                if self.bird_y > 457 - self.bird.get_height():  # Adjusted for screen height (457)
                    self.bird_y = 457 - self.bird.get_height()

                if self.bird_x < 0:
                    self.bird_x = 0
                if self.bird_x > 608 - self.bird.get_width():  # Adjusted for screen width (608)
                    self.bird_x = 608 - self.bird.get_width()

                # Move the pipe to the left
                self.pipe_x += self.pipe_speed
                if self.pipe_x < -self.pipe.get_width():  # Pipe has moved off-screen
                    self.pipe_x = 800
                    self.bird_passed_pipe = False  # Reset flag for next pipe

                # Draw the top and bottom pipes
                pipe_height = self.pipe.get_height()

                # Bottom pipe
                bottom_pipe_y = 300  # Adjust y-position of the bottom pipe
                self.screen.blit(self.pipe, (self.pipe_x, bottom_pipe_y))

                # Top pipe (inverted)
                top_pipe_y = bottom_pipe_y - pipe_height - self.pipe_gap
                top_pipe = pygame.transform.flip(self.pipe, False, True)  # Invert the pipe
                self.screen.blit(top_pipe, (self.pipe_x, top_pipe_y))

                # Check for collision between bird and pipes
                bird_rect = pygame.Rect(self.bird_x, self.bird_y, self.bird.get_width(), self.bird.get_height())
                bottom_pipe_rect = pygame.Rect(self.pipe_x, bottom_pipe_y, self.pipe.get_width(), pipe_height)
                top_pipe_rect = pygame.Rect(self.pipe_x, top_pipe_y, self.pipe.get_width(), pipe_height)

                if bird_rect.colliderect(bottom_pipe_rect) or bird_rect.colliderect(top_pipe_rect):
                    print("Collision detected!")
                    self.game_over = True  # Trigger game over
                    self.bird_visible = False  # Make bird disappear

                # If bird passes the pipe successfully (bird's center passes the pipe's center)
                pipe_center_x = self.pipe_x + self.pipe.get_width() // 2
                bird_center_x = self.bird_x + self.bird.get_width() // 2

                if not self.bird_passed_pipe and bird_center_x > pipe_center_x:
                    self.bird_passed_pipe = True  # Mark that bird has passed the pipe
                    self.score += 1  # Increase score
                    print(f"Score increased: {self.score}")

            else:
                # Display Game Over message
                game_over_surface = self.game_over_font.render('Game Over', True, (255, 0, 0))
                self.screen.blit(game_over_surface, (150, 200))  # Position the "Game Over" message in the center

                # Apply gravity after the collision (falling effect)
                self.bird_movement_y += self.gravity
                self.bird_y += self.bird_movement_y

                # Stop horizontal movement after the crash
                self.bird_movement_x = 0

                # Boundary control for falling
                if self.bird_y > 457 - self.bird.get_height():  # Stop at the ground
                    self.bird_y = 457 - self.bird.get_height()

            # Draw the bird (only if it's still visible)
            if self.bird_visible:
                self.screen.blit(self.bird, (self.bird_x, self.bird_y))

            # Draw the score
            score_surface = self.font.render(f'Score: {self.score}', True, (255, 255, 255))
            self.screen.blit(score_surface, (10, 10))  # Position the score at the top-left corner

            # Update display
            pygame.display.update()
            self.clock.tick(30)  # 30 FPS

        self.head_controller.release()
        pygame.quit()

# For testing purposes
if __name__ == "__main__":
    game = FlappyBirdGame()
    game.run_game()

