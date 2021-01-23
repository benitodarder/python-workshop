
from typing import NamedTuple
import random
import sys
import pygame
import time
import queue
import collections

pygame.init()
pygame.font.init()

NUMBER_OF_FLAKES = 100
FLAKE_RADIUS = 3
FLAKE_RADIUS_BACK = 2
DEPTHS = 5
SPEEDS = 3
SCREEN_WIDTH=320 * 3
SCREEN_HEIGHT=200 * 3
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT
TICKS = 50
NUMBER_OF_FLOOR_FLAKES = 800

class Flake(NamedTuple):
    x: int
    y: int
    depth : int
    speed : int
    radius: int
    color: pygame.Color

FlakeColor = pygame.Color(255, 255, 255, 255)
FlakeColorBack = pygame.Color(128, 128, 128, 255)
Background = pygame.Color(0, 0, 0, 255)

clock=pygame.time.Clock()
Flakes = queue.Queue()    
FloorFlakes = collections.deque(maxlen=NUMBER_OF_FLOOR_FLAKES)

def main(args):
    
    for i in range(NUMBER_OF_FLAKES):
        Flakes.put(getNewFlake(random.randrange(SCREEN_HEIGHT - 1)))

        
    screen = pygame.display.set_mode(SCREEN_SIZE)
    
    exitFlag = True
    
    while exitFlag:
        clock.tick(TICKS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                exitFlag = False    
        
        screen.fill(Background)
        
        for i in range(NUMBER_OF_FLAKES):
            currentFlake = Flakes.get(i)
            y = currentFlake.y + currentFlake.speed
            if y >= SCREEN_HEIGHT:
                FloorFlakes.append(Flake(currentFlake.x, currentFlake.y, currentFlake.depth, currentFlake.speed, currentFlake.radius, FlakeColor))
                currentFlake = getNewFlake(0)
            elif isAtBottom(screen, currentFlake):
                FloorFlakes.append(Flake(currentFlake.x, currentFlake.y, currentFlake.depth, currentFlake.speed, currentFlake.radius, FlakeColor))
            else:
                x = currentFlake.x
                if 1 < x and x < (SCREEN_WIDTH - 2):
                    xSwing = random.randrange(3)
                    if xSwing == 0:
                        x = x - 1
                    elif xSwing == 2:
                        x = x + 1
                currentFlake = Flake(x, y, currentFlake.depth, currentFlake.speed, currentFlake.radius, currentFlake.color)
            
            pygame.draw.circle(screen, currentFlake.color, (currentFlake.x, currentFlake.y), currentFlake.radius) 
            
            Flakes.put(currentFlake)
            
        for currentFlake in FloorFlakes:
            pygame.draw.circle(screen, currentFlake.color, (currentFlake.x, currentFlake.y), currentFlake.radius)   
            
                                              
        pygame.display.flip() 

        
    return 0

def isAtBottom(screen, currentFlake):
    for y in range(currentFlake.y, SCREEN_HEIGHT - 1):
        if screen.get_at((currentFlake.x, y)) == Background: 
            return False
    return True
    
def getNewFlake(y):
    newFlakeDepth = random.randrange(1, DEPTHS)
    if newFlakeDepth <= DEPTHS / 2:
        currentFlake = Flake(random.randrange(SCREEN_WIDTH - 1), y, random.randrange(1, DEPTHS), random.randrange(1, SPEEDS), FLAKE_RADIUS_BACK, FlakeColorBack)
    else:
        currentFlake = Flake(random.randrange(SCREEN_WIDTH - 1), y, random.randrange(1, DEPTHS), random.randrange(1, SPEEDS), FLAKE_RADIUS, FlakeColor)        
    return currentFlake
    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
