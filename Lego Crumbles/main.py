import pygame  #import pygame module
import random

pygame.init()  # initialize pygame

# Variables
# Create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 1000

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Player sprite
# TODO 1: Place your player at the bottom center of the screen
playerWidth = SCREEN_WIDTH
playerHeight = 500
playerSurface = pygame.image.load('COOKIES.png').convert_alpha()
playerSurface = pygame.transform.scale(playerSurface, (playerWidth, playerHeight))
player = playerSurface.get_rect(midbottom=(SCREEN_WIDTH / 2, 999))

# TODO 3: add another sprite for the object you want to collect
collectSurface = pygame.image.load('collectible.png').convert_alpha()
collectSurface = pygame.transform.scale(collectSurface, (60, 60))
collectible = collectSurface.get_rect(midbottom=(random.randint(0, SCREEN_WIDTH),0))  # TODO 4: Place your collectible in a random spot at the top

# Background image
bgSurface = pygame.image.load('PIXEL COOKIE.jpg').convert_alpha()
bgSurface = pygame.transform.scale(bgSurface, (SCREEN_WIDTH, SCREEN_HEIGHT))
background = bgSurface.get_rect()

# TODO 7: Import a Font
# Text
font = pygame.font.Font(None, 32)

# TODO 8: Make a score variable
score = 0

# Create the game loop
run = True
while run:

  # TODO 5: Make the collectible fall down
  collectible.y += 5
  # TODO 6: Make your collectible go back up at a random position when it hits the ground
  if collectible.y >= player.y:
    collectible.y = 0
    collectible.x = random.randint(0, SCREEN_WIDTH)
    # TODO 8.2: Reset your score
    score = 0
  #TODO 6.1: Make your collectible go back up at a random position when the player catches it
  if collectible.colliderect(player):
    collectible.y = 0
    collectible.x = random.randint(0, SCREEN_WIDTH)
    # TODO 8.1: Add a point to score
    score += 1
    playerWidth -= 10
    playerHeight -= 8
    player.y += 8
  # TODO 7.1: Make the text surface and rectangle. Optional: adjust text placement
  # TODO 9: Concatenate your score to the display text
  textSurf = font.render('Score: ' + str(score), True, (255,255,255), (0,0,255))
  text = textSurf.get_rect()
  
  # Player controls
  # TODO 2: remove some lines so that your player can only move left/right
  key = pygame.key.get_pressed()
  if key[pygame.K_LEFT] == True:
    player.x -= 6
  if key[pygame.K_RIGHT] == True:
    player.x += 6

  # Event handler
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  playerSurface = pygame.transform.scale(playerSurface, (playerWidth, playerHeight))
  # Display player
  screen.blit(bgSurface, background)
  screen.blit(playerSurface, player)
  # TODO 3.1: display the collectible
  screen.blit(collectSurface, collectible)
  # TODO 7.2: display the text
  screen.blit(textSurf, text)
  # Update Display
  pygame.display.update()
  # must be called, determines how many times method should be called per second
  pygame.time.Clock().tick(60)

pygame.quit()