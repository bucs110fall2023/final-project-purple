import pygame
import random
import sys
from src.player import Player

class Game:
  def __init__(self):
      self.width = 800
      self.height = 600
      self.fps = 60
      self.white = "white"
      self.red = "red"
      self.player_size = 50
      self.obstacle_size = 50
      self.player_speed = 10
      self.obstacle_speed = 5
      self.obstacle_movement = 25
      self.obstacles = []
      self.score = 0
      self.running = True
      self.screen = pygame.display.set_mode((800, 600))
      self.obstacle_speed = 5
      self.obstacle_movement = 25
      self.obstacles = []
      self.clock = pygame.time.Clock()
      self.player = Player(self.width // 2 - self.player_size // 2, self.height - self.player_size, self.player_size, self.red)

      """
      Basic structure for what the game is going to consist off. There will be colors, 
      parameters for the red sqaure, speed, movement, and consturction of the player model.
      Also 3rd class (Make sure to change class Game to something else as written in our notes)
      """

  def update(self):
      for obstacle in self.obstacles:
          obstacle[1] += self.obstacle_speed
          if obstacle[1] > self.height:
              self.obstacles.remove(obstacle)
              self.score += 1

              """
              Updates the score everytime the red sqaure passes a random number of
              blocks on screen.
              """


      if random.randint(1, self.obstacle_movement) == 1:
          obstacle_x = random.randint(0, self.width - self.obstacle_size)
          obstacle_y = 0 - self.obstacle_size
          self.obstacles.append([obstacle_x, obstacle_y, self.obstacle_size, self.obstacle_size])

          """
          Provides a random number of sqaures to fall on the red sqaure on screen.
          """

      for obstacle in self.obstacles:
          if (self.player.rect.y < obstacle[1] + obstacle[3]):
              if(self.player.rect.y + self.player.rect.height > obstacle[1]):
                  if(self.player.rect.x < obstacle[0] + obstacle[2]):
                      if(self.player.rect.x + self.player.rect.width > obstacle[0]):
                          self.game_over()
      """
      Very tough challenge but, this for loop provides a basic overview if the red sqare
      will collide with the falling white sqaures and since it does, the test is proven
      to be correct. 
      """
  
  def draw(self):
      self.screen.fill("Black")
      self.player.player_red_rectangle(self.screen)
      self.draw_obstacles(self.obstacles)


      font = pygame.font.Font(None, 36)
      score_text = font.render(f"Score: {self.score}", True, self.white)
      self.screen.blit(score_text, (10, 10))

      pygame.display.flip()

      # Set the frame rate
      self.clock.tick(self.fps)

  def draw_obstacles(self, obstacle_list):
          for obstacle in obstacle_list:
              pygame.draw.rect(self.screen, "white", obstacle)


  def game_over(self):
      font = pygame.font.Font(None, 74)
      text = font.render("Game Over", True, self.white)
      self.screen.blit(text, (self.width // 2 - 200, self.height // 2 - 37))
      pygame.display.flip()
      pygame.time.wait(2000)
      pygame.quit()
      sys.exit()

      """
      Code to check if the red sqaure will collide with the white falling sqaures.
      If the red sqaure is going to collide with the white sqaures, then the game
      will display a message saying that the game is over and will exit. Needed a
      system exit as pygame.quit was giving us diffculties and not giving our 
      intended code as expected. 
      """