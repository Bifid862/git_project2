import pygame

class Ino(pygame.sprite.Sprite):
    """класс одного пришельца"""

    def __init__(self, screen):
        """инцилизая и задём начальную и позицию"""
        super(Ino, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/pixil-frame-0 (1).png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """рисуем пришельца"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """движение пришельцев"""
        self.y += 0.3
        self.rect.y = self.y





