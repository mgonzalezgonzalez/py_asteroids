# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))      
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable    
    asteroidfield = AsteroidField()

    Shot.containers = (shots, updatable, drawable)


    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)    
    
    dt = 0

    print(f"{len(drawable)}")

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for ob in updatable:
            ob.update(dt)
        
        for ast in asteroids:
            if ast.check_collisions(player):
                print("GAME OVER!")
                return
            
            for shot in shots:
                if ast.check_collisions(shot):
                    shot.kill()
                    ast.kill()
                    
        screen.fill("black")

        for ob in drawable:
            ob.draw(screen)

        pygame.display.flip()
        
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()