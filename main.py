import pygame
import random
import sys

HEIGHT, WIDTH = 600, 600
pygame.init()
screen = pygame.display.set_mode( (HEIGHT, WIDTH) )


SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)
fps = 20
clock = pygame.time.Clock()

SNAKE = []
score = 0
direction = None
# fpsclock = 

black = (0, 0, 0)

class Snake():
    def __init__(self, x, y, width, color):
        self.x = x
        self.y = y
        self.width = width
        self.color = color

    def draw(self):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.width))

class Food(Snake):
    def __init__(self, x, y, width, color):
        super().__init__(x, y, width, color)

    def detectPlayer(self):
        if SNAKE[0].x == self.x and SNAKE[0].y == self.y:
            global score
            self.x = findSpot(self.width)[0]
            self.y = findSpot(self.width)[1]
            score += 1
            SNAKE.append(Snake(290, 290, 10, SNAKE_COLOR))

def findSpot(width):
    randX = random.randint(0, WIDTH - width)
    randY = random.randint(0, HEIGHT - width)
    
    while randX % 10 !=    0:
        randX = random.randint(0, WIDTH - width)

    while randY % 10 != 0:
        randY = random.randint(0, HEIGHT - width)

    return (randX, randY)

def quit():
    pygame.quit()
    sys.exit()

def collision():
    if SNAKE[0].x < 0 or SNAKE[0].y < 0 or SNAKE[0].x > WIDTH or SNAKE[0].y > HEIGHT:
        quit()
    
    for i in SNAKE[2:]:
        if SNAKE[0].x == i.x and SNAKE[0].y == i.y:
            quit()

SNAKE.append(Snake(290, 290, 10, SNAKE_COLOR))

food = Food(findSpot(10)[0], findSpot(10)[1], 10, FOOD_COLOR)

while True:
    clock.tick(fps)
    screen.fill(black)

    for i in SNAKE:
        i.draw()

    food.draw()
    food.detectPlayer()

    collision()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s and direction != 'n':
                direction = 's'
                
            elif event.key == pygame.K_w and direction != 's':
                direction = 'n'
                
            elif event.key == pygame.K_a and direction != 'e':
                direction = 'w'
                
            elif event.key == pygame.K_d and direction != 'w':
                direction = 'e'
            elif event.key == pygame.K_e:
                SNAKE.append(Snake(290, 290, 10, SNAKE_COLOR))
            
    if direction == 'e':
        SNAKE.insert(0, Snake(SNAKE[0].x + SNAKE[0].width, SNAKE[0].y, 10, SNAKE_COLOR))

    elif direction == 'w':
        SNAKE.insert(0, Snake(SNAKE[0].x - SNAKE[0].width, SNAKE[0].y, 10, SNAKE_COLOR))

    elif direction == 'n':
        SNAKE.insert(0, Snake(SNAKE[0].x, SNAKE[0].y - SNAKE[0].width, 10, SNAKE_COLOR))

    elif direction == 's':
        SNAKE.insert(0, Snake(SNAKE[0].x, SNAKE[0].y + SNAKE[0].width, 10, SNAKE_COLOR))

    if direction != None:
        SNAKE.pop(-1)
        
    pygame.display.update()