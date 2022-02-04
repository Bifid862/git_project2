import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):
        """пуля"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 12)
        self.color = 213, 0, 0
        self.speed = 7.25
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """перемещение по оси у"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """рисуе пулю"""
        pygame.draw.rect(self.screen, self.color, self.rect)



