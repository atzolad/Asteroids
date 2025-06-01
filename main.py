import pygame
from constants import *
from player import *
#source venv/bin/activate

def main():

    #Initialize the game environment
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)

    while True:
        
        #Allows the user to close out the window and end the game loop. 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  
              
        player.update(dt)

        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        #Restricts the game FPS to 60 and returns the time in seconds.
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
