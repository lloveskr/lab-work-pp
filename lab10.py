import random
import pygame
import time

pygame.init()

WIDTH, HEIGHT = 400, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

SCORE = 0

clock = pygame.time.Clock()
background = pygame.image.load('road.jpg')
score_font = pygame.font.SysFont("Verdana", 30)
font_end = pygame.font.SysFont('Arial', 66, bold=True)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 7
        self.image = pygame.image.load('enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (
            random.randint(self.rect.width, WIDTH - self.rect.width),
            0,
        )

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        global SCORE
        self.rect.move_ip(0, self.speed)
        if self.rect.y > HEIGHT:
            SCORE += 1
            self.rect.center = (
                random.randint(self.rect.width, WIDTH - self.rect.width),
                0,
            )


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 5
        self.image = pygame.image.load('coin.png')
        self.rect = self.image.get_rect()
        self.rect.center = (
            random.randint(self.rect.width, WIDTH - self.rect.width),
            0,
        )

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.y > HEIGHT:
            self.rect.center = (
                random.randint(self.rect.width, WIDTH - self.rect.width),
                0,
            )
    def lost(self):
        self.rect.center = (1000,1000)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 5
        self.image = pygame.image.load('player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - self.rect.height // 2 - 20)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] and self.rect.x - self.speed >= 0:
            self.rect.move_ip(-self.speed, 0)
        elif pressed[pygame.K_RIGHT] and self.rect.x + self.speed + self.rect.width <= WIDTH:
            self.rect.move_ip(self.speed, 0)


def main():
    running = True

    player = Player()
    enemy = Enemy()
    coin = Coin()

    coinss = pygame.sprite.Group()
    coinss.add(coin)

    enemies = pygame.sprite.Group()
    enemies.add(enemy)

    coins = 0
    check = True
    check2 = True

    while running:

        SCREEN.blit(background, (0, 0))
    
        score = score_font.render(f" Your score: {SCORE}", True, (0, 0, 0))
        SCREEN.blit(score, (0, 0))

        score2 = score_font.render(f" Your coins: {coins}", True, (0, 0, 0))
        SCREEN.blit(score2, (0, 30))

        score3 = score_font.render(f" Enemy's speed: {enemy.speed}", True, (0, 0, 0))
        SCREEN.blit(score3, (0, 60))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.update()
        enemy.update()
        coin.update()

        player.draw(SCREEN)
        enemy.draw(SCREEN)
        coin.draw(SCREEN)

        if pygame.sprite.spritecollideany(player, enemies):
            render_end = font_end.render('GAME OVER', 1, pygame.Color('red'))
            SCREEN.blit(render_end, (30, 150))
            pygame.display.flip()
            time.sleep(1)
            running = False

        if pygame.sprite.spritecollideany(player, coinss) and check:
            coins += random.randint(1, 5)
            coin.lost()
            check = False

        if not pygame.sprite.spritecollideany(player, coinss):
            check = True

        if coins % 10 == 0 and coins > 0 and check2:
            enemy.speed += 1
            check2 = False
        elif coins % 10 == 1:
            check2 = True
    
        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()
