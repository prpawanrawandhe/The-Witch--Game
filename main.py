import pygame
import random

pygame.init()


bk_sound =  pygame.mixer.Sound("sounds/bk.wav")
front_sound = pygame.mixer.Sound("sounds/front.wav")
score_sound =  pygame.mixer.Sound("sounds/score.wav")

screen = pygame.display.set_mode((800, 450))
pygame.display.set_caption("The Witch")

wel_image = pygame.image.load("images/wel.jpg").convert()
screen_size = screen.get_size()
wel = pygame.transform.scale(wel_image, screen_size)

bc = pygame.image.load("images/bkg.jpg").convert()
f_bc = pygame.transform.scale(bc, screen_size)


witch_img = pygame.image.load("images/chudail2.png").convert_alpha()
witch = pygame.transform.smoothscale(witch_img, (115, 115))
clock = pygame.time.Clock()

crow_img = pygame.image.load("images/crow.png").convert_alpha()
crow = pygame.transform.smoothscale(crow_img, (55, 45))
 

def text(text,x,y,size,color):
    font = pygame.font.SysFont(None, size)
    go_text = font.render(text, True, color)  
    screen.blit(go_text, (x, y))


def main_game():
    gravity = 0.05
    jump_strength = -2.5
    velocity = 0
    witch_y = 100
    witch_x = 150

    crow_speed = 1
    crow_x = 800
    crow_y = 100

    crow_x1 = 1300
    crow_y1 = 150

    crow_x2 = 1400
    crow_y2 = 50

    running = True
    pause = False
    state = 'wel'
    f_play = True
    bk_play = True
    end_play = True
    score = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    state = "playing"

                if event.key == pygame.K_UP:
                    velocity = jump_strength

                if pause == True:
                    if event.key == pygame.K_SPACE:
                        main_game()
                    else:
                        running = False

        if state == 'wel':
            screen.blit(wel, (0, 0))
            text("Press Space to start the game ", 275,10,25,'white')
            if f_play == True:
                front_sound.play()
                front_sound.set_volume(0.3)
                f_play = False

        else:
            front_sound.stop()
            if bk_play == True:
                bk_sound.play()
                bk_sound.set_volume(0.3)
                bk_play = False

            if pause == False:
                velocity += gravity                 
                witch_y += velocity  

            screen.blit(f_bc, (0, 0))
            screen.blit(witch,(witch_x, witch_y))
            witch_rect = witch.get_rect(topleft=(witch_x, witch_y))

            if crow_x < -65:
                score+=10
                crow_x = random.randint(800,850)
                crow_y = random.randint(20,350)
            if pause == False:
                crow_x -= crow_speed
            screen.blit(crow,(crow_x,crow_y))
            crow_rect = crow.get_rect(topleft=(crow_x, crow_y))

            if crow_x1 < -65:
                score+=10
                crow_x1 = random.randint(800,850)
                crow_y1 = random.randint(20,350)
            if pause == False:
                crow_x -= crow_speed
            screen.blit(crow,(crow_x1,crow_y1))
            crow_rect1 = crow.get_rect(topleft=(crow_x1, crow_y1))

            if crow_x2 < -65:
                score+=10
                crow_x2 = random.randint(800,850)
                crow_y2 = random.randint(20,350)
            if pause == False:
                crow_x -= crow_speed
            screen.blit(crow,(crow_x2,crow_y2))
            crow_rect2 = crow.get_rect(topleft=(crow_x2, crow_y2))

            if witch_rect.colliderect(crow_rect) or witch_rect.colliderect(crow_rect1) or witch_rect.colliderect(crow_rect2):
                pause = True
                if end_play == True:
                    bk_sound.stop()
                    score_sound.play()
                    score_sound.set_volume(0.3)
                    end_play = False
                text("Game Over",235,270,80,"white")
                text("Press space for continue and e for exit", 465,425,25,'red')
            text(f"Score {score}",10,10,30,"white")


        pygame.display.flip()
        clock.tick(60)

main_game()

pygame.quit()