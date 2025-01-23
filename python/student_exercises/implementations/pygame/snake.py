import pygame
import random

# To install pygame inside conda run:
# run `pip install pygame` inside the coonda environment
# To run the example run this inside the pygame folder:
# python snake.pyc

# Initialize Pygame
pygame.init()

# CONSTANTS
# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

BLOCK_SIZE = 10

# Set up the display
WIDTH, HEIGHT = 640, 480

# init screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# set caption
pygame.display.set_caption("Snake Game")

# Point class
class Point(object):
    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.x, self.y = (x, y)

    def copy(self):
        return Point(self.width, self.height, self.x, self.y)
  
    @staticmethod
    def get_random_point(width, height):
        x = random.randint(0, (width-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
        y = random.randint(0, (height-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
        return Point(width, height, x, y)
    
    def __eq__(self, other):
        """
        Magic Function to compare two Point objects.
        """
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

# Food class
class Food:
    position: Point = None
    def __init__(self, snake) -> None:
        """
        Constructor of the Food class used to create a food object.

        Args:
            snake (Snake): The snake object.
        """
        # TODO: Initialize the position of the food with a random position.
        pass
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
        p: Point = Point.get_random_point(WIDTH, HEIGHT)
        # TODO: Check if the position is on the snake.
        #       If the position is on the snake, choose another position.
        return p
    
    
    def create_new_food_item(self, snake) -> None:
        """
        Function to create a new food object.
        this functions set the position (type Point) of the food object. (self.position)
        to a random position that is not on the snake.
        
        Args:
            snake (Snake): The snake object.
      
        """
        # TODO: Set the position of the food object to a random position that is not on the snake.
        pass

    def draw(self) -> None:
        pygame.draw.rect(screen, RED, (self.position.x, self.position.y, BLOCK_SIZE, BLOCK_SIZE))

# Snake class
class Snake:
    """
    Class to represent the snake.

    Attributes:
        _current_direction (str): The current direction of the snake. (UP, DOWN, RIGHT, LEFT)
        body (list): The list of segments of the snake. A segment is a Point object.

    ********************************************************************************************************************
    The main idea is to store the position of each segment on the screen in a list (body).
    When drawing the snake we will draw a rectangle for each segment of the snake given the position.

    To make the snake move, we will add a new segment at the head of the snake and remove the last segment of the snake.
    The new head segment is a copy of the current head segment with the new position.
    The new position is defined by the current direction of the snake. look at the move() function for more details.

    To change the direction of the snake, we will use the change_direction() function. The new direction is passed as an argument.
    The new direction is valid if and only if it's not the opposite of the current direction.

    To grow the snake, we will add a new segment at the end of the snake.
    This new segment will be deleted when the move function will be called

    Then we will check if the snake hits the border of the screen or if the snake hits itself.
    This will be done using the position of the head. (the first segment of the snake)
    if the head is at the same position of one of the segments of the snake, the snake hits itself.
    if the head is outside the screen, the snake hits the border of the screen.

    To eat the food, we will check if the head of the snake is at the same position as the food. using the check_collision() function.

    The game is over if the snake hits the border of the screen or if the snake hits itself.
    """
    _current_direction: str = ""
    body: list[Point] = []
    def __init__(self) -> None:
        """
        Constructor of the Snake class used to create a snake object.
        -   The constructor should initialize the position of the snake with a random position.
        -   The constructor should initialize the snake with 3 segments (on the left).
        -   The constructor should initialize the direction of the snake with a random direction. (UP, DOWN, RIGHT)
                only these directions because the snake can't go left at the beginning, as the left part of the head will be the body.
        """
        # TODO: Initialize the position of the snake with a random position.
        head: Point = None
        # TODO: Initialize the snake with 3 segments. the segments are stored in the self.body attribute.
        #       the first segment is the head of the snake. the next one is the head of the snake - BLOCK_SIZE (10) on the x axis. and the third one is the head of the snake - 2*BLOCK_SIZE (20) on the x axis.
        #       This will create a snake with 3 segments of 10px (BLOCK_SIZE) each.
        self.body = None
        # TODO: Initialize the direction of the snake with a random direction. (UP, DOWN, RIGHT)
        self._current_direction: str = None
    
    def move(self) -> None:
        """
        Function to move the snake.
        For moving the snake we will
        -   add a new head (the current head values + BLOCK_SIZE (10) (according the direction))
        -   and remove the last segment of the snake.

        ****************************************************************************************************************
        - The function should move the snake in the current direction (using the current direction variable).
          Mooving in the current direction means that the (x, y) position of the head of the snake should be updated.
          according to the current direction variable.
          For exemple: if the current direction is "UP" the "y" position of the head should be decreased by BLOCK_SIZE (10).
        
        - The function should add a new segment at the head of the snake.
          This mean the new head of the snake should be added at the index 0 of the list of segments.

        - The function should remove the last segment of the snake.

         Note : The 0,0 position is the top left corner of the screen.
                The x axis is the horizontal axis and the y axis is the vertical axis.
                That mean to move the snake:
                  - UP you must decrease the y position of the head of the snake.
                  - DOWN you must increase the y position of the head of the snake.
                  - RIGHT you must increase the x position of the head of the snake.
                  - LEFT you must decrease the x position of the head of the snake.
        """
        new_head:Point = self.body[0].copy() # don't change this line, it's used to copy the head of the snake.

        # TODO: Update the position of the head_copy of the snake according to the current direction.
        # TODO: Add the new segment at the head of the snake.
        # TODO: Remove the last segment of the snake.
        pass
    
    def change_direction(self, direction: str) -> None:
        """
        Function to update the direction of the snake.
        - The function should update the direction of the snake
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
        The new segment is a copy of the last segment of the snake.
        
        - The function should add a new segment at the end of the snake.
        """
        # TODO: Add a new segment at the end of the snake.
        pass
    
    def check_collision(self, item: Food) -> bool:
        """
        Function to check if the snake hits the food.
        To check if the snake hits the food you must check if the head of the snake is on the same position as the food.
        The food position is stored in the item.position attribute.

        Args:
            item (Food): The food object.

        Returns:
            bool: True if the snake hits the food, False otherwise.
        """
        return False


    def check_border_collision(self) -> bool:
        """
        Function to check if the snake hits the border of the screen.
        To check if the snake hits the border of the screen you must check if the head of the snake is outside the screen.
        The screen size is (WIDTH, HEIGHT).
        For exemple: if the x position of the head is less than 0 the snake hits the left border of the screen.

        Returns:
            bool: True if the snake hits the border of the screen, False otherwise.
        """
        return False

    def check_self_collision(self) -> bool:
        """
        Function to check if the snake hits itself.
        To check if the snake hits itself you must check if the head of the snake is on the same position as one of the segments of the snake.
        The segments of the snake are stored in the self.segments attribute.
        
        Returns:
            bool: True if the snake hits itself, False otherwise.
        """
        return False
    
    
    def check_game_over(self) -> bool:
        """
        Function to check if the game is over.
        The game is over if the snake hits the border of the screen or if the snake hits itself.

        Returns:
            bool: True if the game is over, False otherwise.
        """
        return False
    
    def draw(self) -> None:
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (segment.x, segment.y, BLOCK_SIZE, BLOCK_SIZE))

# Create instances of Snake and Food - Global variables
snake = Snake()
food = Food(snake)

# Helpers functions
def press_space_to_start(font):
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
  update_direction: bool = True
  clock = pygame.time.Clock()
  font = pygame.font.Font('freesansbold.ttf', 32)
  score: int = 0

  running: bool = press_space_to_start(font) # -> blocking function

  while running:
      clock.tick(20) # 20 FPS
      
      # ================= EVENT PART =================
      # getting the key events used to change the direction of the snake.
      # To change the direction we'll use the direction arrow keys of the keyboard.
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
      # Move the snake
      snake.move()

      #Check for food collision
      if (snake.check_collision(food)):
        snake.grow()
        food.create_new_food_item(snake)
        score += 1


      #Check for game over
      if(snake.check_game_over()):
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