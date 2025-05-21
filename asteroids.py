import pygame
from circleshape import CircleShape
import random
from constants import ASTEROID_MIN_RADIUS
class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		self.x = x
		self.y = y
		self.radius = radius
		super().__init__(x, y, radius)
	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, width = 2)

	def update(self, dt):
		self.position += (self.velocity * dt)

	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		else:
			angle = random.uniform(20, 50)
			new1 = self.velocity.rotate(angle)
			new2 = self.velocity.rotate(-angle)
			new_radius = self.radius - ASTEROID_MIN_RADIUS
			new_as_1 = Asteroid(self.position.x, self.position.y, new_radius)
			new_as_2 = Asteroid(self.position.x, self.position.y, new_radius)
			new_as_1.velocity = new1 * 1.2
			new_as_2.velocity = new2 * 1.2
