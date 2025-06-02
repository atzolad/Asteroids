import pygame
import sys
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from Shot import Shot
#source venv/bin/activate

def main():

    #Initialize the game environment
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    #Initialize all the empty groups to store the game objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)

    Shot.containers = (shots, updatable, drawable)
    

    while True:
        
        #Allows the user to close out the window and end the game loop. 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  
              
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collisions(player):
                print("Game over!")
                sys.exit()


        screen.fill("black")

        #Create all drawable game objects in the play field.
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()

        #Restricts the game FPS to 60 and returns the time in seconds.
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
