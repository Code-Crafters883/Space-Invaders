import pygame
import random
import math
from pyarray import*
from Stacks import*
from megship import*
pygame.init()
screen = pygame.display.set_mode((800, 600))
bg=pygame.image.load("background.png")
pygame.display.set_caption('Space Invaders')
image = pygame.image.load('ship.png')
bullet_image = pygame.image.load('laser.png')
enemyX=Array(7)

enemyY=Array(7)
enemy_image=Array(21)
enemy_changeX=Array(7)
enemy_changeY=Array(7)
no_of_enemies=int(7)
playerX = int(350)
playerY = int(550)
player_changeX=int(0)
player_changeY=int(0)
bulletX = int(0)
bulletY = int(550)
bullet_changeX=int(0)
bullet_changeY=int(25)
bullet_state="ready"
high_score=stack()
high_score.push(0)
for i in range(no_of_enemies):
    enemy_image.append(pygame.image.load('enemy1_2.png'))
    enemy_image.append(pygame.image.load('enemy.png'))
    enemy_image.append(pygame.image.load('enemy2.png'))
    enemyX.append(random.randint(0,200))
    enemyY.append((random.randint(50,600)))
    enemy_changeX.append(4)
    enemy_changeY.append(40)

score_val=int(0)
font=pygame.font.Font("freesansbold.ttf",32)
nextl_font=pygame.font.Font("freesansbold.ttf",32)
font1=pygame.font.Font("freesansbold.ttf",50)
over_font=pygame.font.Font("freesansbold.ttf",64)
textX=int(10)
textY=int(10)

def show_score(x,y):
    score=font.render("Score :"+str(score_val),True,(255,255,255))
    screen.blit(score,(int(x),int(y)))
    
def nextl(x,y):
    nextl=nextl_font.render("LEVEL :1",True,(255,255,255))
    screen.blit(nextl,(int(x),int(y)))
    
def final_score(x,y):
    score=font1.render("Your Score:"+str(high_score.pop()),True,(255,255,255))
    screen.blit(score,(int(x),int(y)))

def game_over_text():
    over_text=over_font.render("GAME OVER",True,(255,255,255))
    screen.blit(over_text,(200,250))
    
def player(x, y):                                                       
    screen.blit(image, (int(x), int(y)))
    
def enemy(x, y,i):                                                    
    screen.blit(enemy_image[i], (int(x), int(y)))

def fire_bullet(x,y):
    global bullet_state
    bullet_state="fired"
    screen.blit(bullet_image,(x+30,y+10))

def iscollision(enemyX,enemyY,bulletX,bulletY):
    dis=math.sqrt((math.pow(enemyX-bulletX,2))+(math.pow(enemyY-bulletY,2)))
    if dis<27:
        return True
    else:
        return False

def iscollisionB(playerX,playerY,enemyX,enemyY):
    dis1=math.sqrt((math.pow(playerX-enemyX,2))+(math.pow(playerY-enemyY,2)))
    if dis1<27:
        return True
    else:
        return False

def draw_username(display_surface, username):
    font = pygame.font.SysFont('comicsans', 30)
    
    # Render the label and username
    label = font.render('Player: ', 1, (255, 255, 255))
    username_label = font.render(username, 1, (255, 255, 255))

    # Get the sizes of the label and the username text
    label_width, label_height = label.get_size()
    username_width, username_height = username_label.get_size()

    # Calculate the X and Y positions
    X = 10  # Position label a bit from the left side
    Y = 30  # Position it a bit from the top
    
    # Render the label and username at calculated positions
    display_surface.blit(label, (X, Y))  # Position for "Player: "
    
    # Shift username to the left and down a bit
    display_surface.blit(username_label, (X + label_width + 2, Y + 2))

def level2(username):
    print(f"Level 2 started with username: {username}")  # Debug line
    global enemyX
    global enemyY
    global playerX
    global playerY
    global enemy_changeX
    global enemy_changeY
    global score_val
    global bulletX
    global bulletY
    global bullet_state
    global player_changeX
    global player_changeY

    running2 = True
    while running2:
        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))

        # Display the username at the top-left corner
        draw_username(screen, username)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running2 = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_changeX = -5
                if event.key == pygame.K_RIGHT:
                    player_changeX = 5
                if event.key == pygame.K_DOWN:
                    player_changeY = 5
                if event.key == pygame.K_UP:
                    player_changeY = -5
                if event.key == pygame.K_SPACE:
                    if bullet_state == "ready":
                        bullet_sound = mixer.Sound("laser.wav")
                        bullet_sound.play()
                        bulletX = playerX
                        bulletY = playerY
                        fire_bullet(bulletX, bulletY)
            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                    player_changeX = 0
                    player_changeY = 0

        # Game logic for level 2 (more enemies, increased speed, etc.)
        for i in range(no_of_enemies):
            if enemyY[i] > 500:
                for j in range(no_of_enemies):
                    enemyY[j] = 2000
                game_over_text()
                break

            enemyX[i] += enemy_changeX[i]
            if enemyX[i] <= 0:
                enemy_changeX[i] = 6  # Increase speed for level 2
                enemyY[i] += enemy_changeY[i]
            elif enemyX[i] >= 736:
                enemy_changeX[i] = -6  # Increase speed for level 2
                enemyY[i] += enemy_changeY[i]

            collision = iscollision(enemyX[i], enemyY[i], bulletX, bulletY)
            collisionb = iscollisionB(playerX, playerY, enemyX[i], enemyY[i])

            if collision:
                exp_sound = mixer.Sound("explosion.wav")
                exp_sound.play()
                bulletY = 550
                bullet_state = "ready"
                score_val += 10  # Increase score increment for level 2
                high_score.push(score_val)
                enemyX[i] = random.randint(0, 735)
                enemyY[i] = random.randint(50, 100)

            enemy(enemyX[i], enemyY[i], i)

            if collisionb:
                game_over_text()
                final_score(230, 320)
                running2 = False

        if bullet_state == "fired":
            fire_bullet(bulletX, bulletY)
            bulletY -= bullet_changeY
        if bulletY <= 0:
            bulletY = 550
            bullet_state = "ready"

        # Update player position
        playerX += player_changeX
        playerY += player_changeY
        player(playerX, playerY)

        show_score(textX, textY)
        nextl(650, 10)

        pygame.display.update()
