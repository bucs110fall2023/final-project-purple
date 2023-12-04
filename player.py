import pygame

class Player:
  def __init__(self, x, y, size, color,):
      self.rect = pygame.Rect(x, y, size, size)
      self.color = color
      self.is_jumping = False
      self.block_jump = 10

      """
      First class is the player. These are some basic parameters used for how we
      were going to consturction the red sqaure. Size, color, and if the sqaure is
      or is not jumping.
      """

  def jump(self):
      if self.block_jump >= -10:
          neg = 1.1
          if self.block_jump < 0:
              neg = -1.1
          self.rect.y -= (self.block_jump ** 2) * 0.5 * neg
          self.block_jump -= 1
      else:
          self.is_jumping = False
          self.block_jump = 10

  def movement(self, keys):
      if keys[pygame.K_LEFT] and self.rect.x > 0:
          self.rect.x -= player_speed
      if keys[pygame.K_RIGHT] and self.rect.x < WIDTH - self.rect.width:
          self.rect.x += player_speed

  def player_red_rectangle(self, screen):
      pygame.draw.rect(screen, self.color, self.rect)