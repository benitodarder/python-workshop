
from typing import NamedTuple
import random
import sys
import pygame
import time
import queue

pygame.init()
pygame.font.init()

NUMBER_OF_STARS = 100
STAR_RADIUS = 3
STAR_RADIUS_BACK = 2
DEPTHS = 5
SCREEN_WIDTH=320 * 3
SCREEN_HEIGHT=200 * 3
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT
TICKS = 60
SLEEP = .05

class Star(NamedTuple):
    x: int
    y: int
    depth : int

StarColor = pygame.Color(255, 255, 255, 255)
StarColorBack = pygame.Color(128, 128, 128, 255)
Background = pygame.Color(0, 0, 0, 255)

clock=pygame.time.Clock()
stars = queue.Queue()    

def main(args):
    
    for i in range(NUMBER_OF_STARS):
        newStar = Star(random.randrange(SCREEN_WIDTH - 1), random.randrange(SCREEN_HEIGHT - 1), random.randrange(1, DEPTHS))
        stars.put(newStar)
        
    screen = pygame.display.set_mode(SCREEN_SIZE)
    
    exitFlag = True
    
    while exitFlag:
#        time.sleep(SLEEP)
        clock.tick(TICKS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                exitFlag = False    
        
        screen.fill(Background)
        
        for i in range(NUMBER_OF_STARS):
            currentStar = stars.get(i)
            x = currentStar.x - currentStar.depth
            
            if x <= 0:
                currentStar = Star(SCREEN_WIDTH - 1, random.randrange(SCREEN_HEIGHT - 1), random.randrange(1, DEPTHS))
            else:
                currentStar = Star(x, currentStar.y, currentStar.depth)

            if currentStar.depth <= DEPTHS / 2:
                pygame.draw.circle(screen, StarColorBack, (currentStar.x, currentStar.y), STAR_RADIUS_BACK)
            else:
                pygame.draw.circle(screen, StarColor, (currentStar.x, currentStar.y), STAR_RADIUS) 
            
            stars.put(currentStar)
            
        pygame.display.flip() 

        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
