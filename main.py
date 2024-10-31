import pygame
import sys
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (updatable, drawable, shots)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return       
        
        

        for u in updatable:
            u.update(dt)

        for a in asteroids:
            for s in shots:
                if s.collision(a):
                    a.kill()
                    s.kill()
            if a.collision(player):
                print("Game Over!")
                sys.exit()

        screen.fill("black")

        for d in drawable:
            d.draw(screen)    
        
        pygame.display.flip()
        dt = (clock.tick(60) / 1000)        

if __name__ == "__main__":
    main()