import pygame
import time
import random
from pygame import mixer
#pygame.mixer.init()
 
pygame.init()
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
 
dis_width = 300
dis_height = 300
font = pygame.font.SysFont( None, 30)
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('GAME')
 
clock = pygame.time.Clock()
 
blocksize = 10
snake_speed = 15


def snake(blocksize, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], blocksize, blocksize])
  
 
 
def message(msg, colour):
    mesg = font.render(msg, True, colour)
    dis.blit(mesg, [dis_width / 3, dis_height / 2])
 
scorefont = pygame.font.SysFont('comicsansms', 20)
def Fscore(score):
  text = scorefont.render('Score: '+str(score), True, blue)
  dis.blit(text,[0,0])
 
def gameLoop():
  score = 0 
  game_over = False
  game_close = False
  Intro = True
  x1 = dis_width / 2
  y1 = dis_height / 2
  x1_change = 0
  y1_change = 0
  snake_List = []
  Length_of_snake = 1

  
 
  randAppleX = round(random.randrange(0, dis_width - blocksize) / 10.0) * 10.0
  randAppleY = round(random.randrange(0, dis_height - blocksize) / 10.0) * 10.0

  randWallX = round(random.randrange(0, dis_width - blocksize) / 10.0) * 10.0
  randWallY = round(random.randrange(0, dis_height - blocksize) / 10.0) * 10.0
  randWall2X = round(random.randrange(0, dis_width - blocksize) / 10.0) * 10.0
  randWall2Y = round(random.randrange(0, dis_height - blocksize) / 10.0) * 10.0
  randWall3X = round(random.randrange(0, dis_width - blocksize) / 10.0) * 10.0
  randWall3Y = round(random.randrange(0, dis_height - blocksize) / 10.0) * 10.0
  
 
  while not game_over:

        while Intro == True:
          message("press space to start",white)
          pygame.display.update()
          pygame.time.wait(2000)
          for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_SPACE:
                Intro = False
 
        while game_close == True:
            dis.fill(black)
            message("You lost", red)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = - (blocksize)
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = + (blocksize)
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = - (blocksize)
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = + (blocksize)
                    x1_change = 0
        ### Collision ?
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, red, [randAppleX, randAppleY, blocksize, blocksize])
        pygame.draw.rect(dis, blue, [randWallX, randWallY, blocksize, blocksize])
        pygame.draw.rect(dis, blue, [randWall2X, randWall2Y, blocksize, blocksize])
        pygame.draw.rect(dis, blue, [randWall3X, randWall3Y, blocksize, blocksize])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        snake(blocksize, snake_List)
        Fscore(score)
 
        pygame.display.update()
 
        if x1 == randAppleX and y1 == randAppleY:
            randAppleX = round(random.randrange(0, dis_width - blocksize) / 10.0) * 10.0
            randAppleY = round(random.randrange(0, dis_height - blocksize) / 10.0) * 10.0
            Length_of_snake += 1
            score += 10
            randWallX = round(random.randrange(0, dis_width - blocksize) / 10.0) * 10.0
            randWallY = round(random.randrange(0, dis_height - blocksize) / 10.0) * 10.0
            randWall2X = round(random.randrange(0, dis_width - blocksize) / 10.0) * 10.0
            randWall2Y = round(random.randrange(0, dis_height - blocksize) / 10.0) * 10.0
            randWall3X = round(random.randrange(0, dis_width - blocksize) / 10.0) * 10.0
            randWall3Y = round(random.randrange(0, dis_height - blocksize) / 10.0) * 10.0
            
            
        

        pygame.display.update()

        
      
        
        clock.tick(snake_speed)
 
  pygame.quit()
  quit()
 
 
gameLoop()