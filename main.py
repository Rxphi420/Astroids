import pygame
from constants import *
from player import Player
from asteroidfield import *
from Shot import Shot
def main():
	pygame.init()
	print ("Starting Asteroids!")
	print (f"Screen width: {SCREEN_WIDTH}")
	print (f"Screen height: {SCREEN_HEIGHT}")
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	dt = 0
	asteroids = pygame.sprite.Group()
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	Shot.containers = (shots, updatable, drawable)
	AsteroidField.containers = (updatable,)
	Asteroid.containers = (asteroids, updatable, drawable)
	Player.containers = (updatable, drawable)
	Asteroidfield = AsteroidField()
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	Game_over = True
	while Game_over == True :
		for event in pygame.event.get():
    			if event.type == pygame.QUIT:
        			return
		updatable.update(dt)
		for thing in asteroids:
			if thing.collision(player) == False:
				print ("Game over!")
				Game_over = False
		for thing in asteroids:
			for bullet in shots:
                                if thing.collision(bullet) == False:
                                        bullet.kill()
                                        thing.split()
		screen.fill("black")
		for thing in drawable:
		   thing.draw(screen)

		pygame.display.flip()
		dt= clock.tick(60) / 1000

if __name__ == "__main__":
    main()
