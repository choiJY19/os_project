import pygame  # 1. pygame 선언
import random
import os

pygame.init()  # 2. pygame 초기화

# 3. pygame에 사용되는 전역변수 선언

BLACK = (0, 0, 0)
size = [600, 800] 
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()

def runGame():
    garlic_image = pygame.image.load('garlic.png')
    garlic_image = pygame.transform.scale(garlic_image, (50, 50))
    garlic = []

    for i in range(5):
        rect = pygame.Rect(garlic_image.get_rect())
        rect.left = random.randint(0, size[0])
        rect.top = -100
        dy = random.randint(3, 9)
        garlic.append({'rect': rect, 'dy': dy})

    tiger_image = pygame.image.load('tiger.png')
    tiger_image = pygame.transform.scale(tiger_image, (100, 100))
    tiger = pygame.Rect(tiger_image.get_rect())
    tiger.left = size[0] // 2 - tiger.width // 2
    tiger.top = size[1] - tiger.height
    tiger_dx = 0
    tiger_dy = 0

    global done
    while not done:
        clock.tick(30)
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tiger_dx = -5
                elif event.key == pygame.K_RIGHT:
                    tiger_dx = 5

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    tiger_dx = 0
                elif event.key == pygame.K_RIGHT:
                    tiger_dx = 0

        for ga in garlic:
            ga['rect'].top += ga['dy']
            if ga['rect'].top > size[1]:
                garlic.remove(bomb)
                rect = pygame.Rect(garlic_image.get_rect())
                rect.left = random.randint(0, size[0])
                rect.top = -100
                dy = random.randint(3, 9)
                garlic.append({'rect': rect, 'dy': dy})

        tiger.left = tiger.left + tiger_dx

        if tiger.left < 0 :
            tiger.left = 0
        elif tiger.left > size[0] - tiger.width :
            tiger.left = size[0] - tiger.width

        screen.blit(tiger_image, tiger)

        for ga in garlic:
            if ga['rect'].colliderect(tiger):
                done = True
            screen.blit(garlic_image, ga['rect'])

        pygame.display.update()


runGame()
pygame.quit()
