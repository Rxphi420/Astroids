import pygame
from circleshape import CircleShape
from constants import *
class Shot(CircleShape):
	def __init__(self, x, y, radius, velocity):
		self.speed = velocity
		self.radius = radius
		super().__init__(x, y, radius)
	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, width = 2)

	def update(self, dt):
		self.position += (self.speed * dt)
