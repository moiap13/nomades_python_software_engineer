import pygame
import random

# Initialize Pygame
pygame.init()

# CONSTANTS
# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

BLOCK_SIZE = 10

# Set up the display
WIDTH, HEIGHT = 640, 480

# init screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# set caption
pygame.display.set_caption("Snake Game")

# Point class
class Point:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.x, self.y = self.get_random_point()
    
    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.x, self.y = x, y

    def copy(self):
        return Point(self.width, self.height, self.x, self.y)
    
    def get_random_point(self):
        x = random.randint(0, (self.width-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
        y = random.randint(0, (self.height-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
        return Point(self.width, self.height, x, y)
  
    @staticmethod
    def get_random_point(width, height):
        x = random.randint(0, (width-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
        y = random.randint(0, (height-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
        return Point(width, height, x, y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

# Food class
class Food:
    position:Point = None
    def choose_position(self, snake) -> Point:
        """
        Function to choose a random position for the food. 
        The position should not be on the snake.

        Note: Feel free to use the @staticmethod get_random_point() of the Point class.
        Une methode statique, c'est une methode qui n'a pas besoin d'etre instanciee pour etre appelee.
        Exemple: Point.get_random_point(10, 10), retourne un objet de type Point avec les coordonnees x et y aleatoires comprise dans la grille 10/10.
        
        Args:
            snake (Snake): The snake object.

        Returns:
            Point: The position of the food.
        """
        return None
    
    def __init__(self, snake) -> None:
        """
        Constructor of the Food class used to create a food object.

        Args:
            snake (Snake): The snake object.
        """
        pass
    
    def create(self, snake) -> None:
        """
        Function to create a new food object.
        this functions set the position (type Point) of the food object. (self.position)
        to a random position that is not on the snake.
        
        Args:
            snake (Snake): The snake object.
      
        """
        pass
    
    def draw(self) -> None:
        pygame.draw.rect(screen, RED, (self.position.x, self.position.y, BLOCK_SIZE, BLOCK_SIZE))

# Snake class
class Snake:
    _current_direction:str = "UP"
    _body = []
    def __init__(self) -> None:
        """
        Constructor of the Snake class used to create a snake object.
        - The constructor should initialize the position of the snake with a random position.
        - The constructor should initialize the snake with 3 segments.
        - The constructor should initialize the direction of the snake with a random direction. (UP, DOWN, RIGHT)
        """
        pass
    
    def move(self) -> None:
        """
        Function to move the snake.

        - The function should move the snake in the current direction.
          Mooving in the current direction means that the (x, y) position of the head of the snake should be updated.
          according to the current direction.
          For exemple: if the current direction is "UP" the "y" position of the head should be decreased by BLOCK_SIZE (10).
        
        - The function should add a new segment at the head of the snake.
          This mean the new head of the snake should be added at the index 0 of the list of segments.

        - The function should remove the last segment of the snake.

         Note :  The 0,0 position is the top left corner of the screen. 
                The x axis is the horizontal axis and the y axis is the vertical axis.
                That mean to move the snake:
                  - UP you must decrease the y position of the head of the snake.
                  - DOWN you must increase the y position of the head of the snake.
                  - RIGHT you must increase the x position of the head of the snake.
                  - LEFT you must decrease the x position of the head of the snake.
        """
        pass
        
    
    def change_direction(self, direction:str) -> None:
        """
        Function to update the direction of the snake.
        - The function should upadte the direction of the snake 
          The function test if the direction is valid, 
          a valid direction is a direction that is not the opposite of the current direction.
          For exemple: if the current direction is "UP" the current direction will be updated if and only if the new direction is not DOWN.
        
        Args:
            direction (str): The new direction of the snake.
        """
        pass
    
    def grow(self) -> None:
        """
        Function to grow the snake. 
        To make the snake grow you must add a new segment at the end of the snake.
        
        - The function should add a new segment at the end of the snake.
        """
        pass

    def check_border_collision(self) -> bool:
        """
        Function to check if the snake hits the border of the screen.
        To check if the snake hits the border of the screen you must check if the head of the snake is outside the screen.
        The screen size is (WIDTH, HEIGHT).
        For exemple: if the x position of the head is less than 0 the snake hits the left border of the screen.

        Returns:
            bool: True if the snake hits the border of the screen, False otherwise.
        """
        return True

    def check_self_collision(self) -> bool:
        """
        Function to check if the snake hits itself.
        To check if the snake hits itself you must check if the head of the snake is on the same position as one of the segments of the snake.
        The segments of the snake are stored in the self.segments attribute.
        
        Returns:
            bool: True if the snake hits itself, False otherwise.
        """
        return True
    
    def check_collision(self, item:Food) -> bool:
        """
        Function to check if the snake hits the food.
        To check if the snake hits the food you must check if the head of the snake is on the same position as the food.
        The food position is stored in the item.position attribute.

        Args:
            item (Food): The food object.

        Returns:
            bool: True if the snake hits the food, False otherwise.
        """
        return True
    
    def check_game_over(self) -> bool:
        """
        Function to check if the game is over.
        The game is over if the snake hits the border of the screen or if the snake hits itself.

        Returns:
            bool: True if the game is over, False otherwise.
        """
        return True
    
    def draw(self) -> None:
        for segment in self.segments:
            pygame.draw.rect(screen, GREEN, (segment.x, segment.y, BLOCK_SIZE, BLOCK_SIZE))

# Create instances of Snake and Food - Global variables
snake = Snake()
food = Food(snake)

# Helpers functions
def press_space_to_start(font, running):
  start_text = font.render("Press SPACE to start the game", True, WHITE, BLACK)
  start_text_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
      
  screen.fill(BLACK)
  screen.blit(start_text, start_text_rect)
  pygame.display.flip()

  clock = pygame.time.Clock()
  while True:
      clock.tick(30)  # 30 FPS
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              return False
          elif event.type == pygame.KEYDOWN:
              if event.key == pygame.K_SPACE:
                  return True

def display_score(font, score):
    score_text = font.render(f"Score: {score}", True, WHITE, None)
    score_text_rect = score_text.get_rect(center=(WIDTH // 2, 20))
    screen.blit(score_text, score_text_rect)

# Main function
def snake_game():
  # Game loop
  update_direction = True
  clock = pygame.time.Clock()
  font = pygame.font.Font('freesansbold.ttf', 32)
  score = 0

  running = press_space_to_start(font, running) # -> blocking function

  while running:
      clock.tick(20) # 20 FPS
      
      # ================= EVENT PART =================
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              running = False
          elif event.type == pygame.KEYDOWN and update_direction:
              if event.key == pygame.K_UP:
                  snake.change_direction("UP")
              elif event.key == pygame.K_DOWN:
                  snake.change_direction("DOWN")
              elif event.key == pygame.K_LEFT:
                  snake.change_direction("LEFT")
              elif event.key == pygame.K_RIGHT:
                  snake.change_direction("RIGHT")
              
              update_direction = False
      # ================= END EVENT PART =================


      # ================= LOGIC PART =================
      #Move snake
      snake.move()

      #Check for collision with food
      if (snake.check_collision(food)):
        snake.grow()
        food.create(snake)
        score += 1


      #Check for game over
      if(snake.check_game_over()):
          # TODO: Display game over message + score
          running = False

      # ================= END LOGIC PART =================
      
      
      # ================= DISPLAY PART =================
      #Clear canvas
      screen.fill(BLACK)
      #Draw snake and food
      snake.draw()
      food.draw()
      
      display_score(font, score)

      # update screen to display the drawing
      pygame.display.update()
      # ================= END DISPLAY PART =================

      # Reset the direction
      update_direction = True

if __name__ == "__main__":
  snake_game()
  pygame.quit()