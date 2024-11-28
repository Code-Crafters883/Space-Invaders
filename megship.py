import pygame
import random
import math
from pyarray import*
from Stacks import*
from pygame import mixer
pygame.init()
screen = pygame.display.set_mode((800, 600))
bg=pygame.image.load("background.png")
pygame.display.set_caption('Space Invaders')
image = pygame.image.load('ship.png')
monstership=pygame.image.load('monster.png')
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
monster_changeX=int(8)
monster_changeY=int(40)
monsterX=200
monsterY=100

bulletX = int(0)
bulletY = int(550)
bullet_changeX=int(0)
bullet_changeY=int(25)
bullet_state="ready"
high_score=stack()
counterB=0
for i in range(no_of_enemies):
    enemy_image.append(pygame.image.load('enemy1_2.png'))
    enemy_image.append(pygame.image.load('enemy.png'))
    enemy_image.append(pygame.image.load('enemy2.png'))
    enemyX.append(random.randint(0,200))
    enemyY.append((random.randint(50,300)))
    enemy_changeX.append(8)
    enemy_changeY.append(40)

score_val=int(0)
font=pygame.font.Font("freesansbold.ttf",32)
font1=pygame.font.Font("freesansbold.ttf",50)
over_font=pygame.font.Font("freesansbold.ttf",64)
won_font=pygame.font.Font("freesansbold.ttf",64)
textX=int(10)
textY=int(10)
def next1(x,y):
    nextl=font.render("LEVEL :2",True,(255,255,255))
    screen.blit(nextl,(int(x),int(y)))
def show_score(x,y):
    score=font.render("Score :"+str(score_val),True,(255,255,255))
    screen.blit(score,(int(x),int(y)))
def final_score(x,y):
    score=font1.render("Your Score:"+str(high_score.pop()),True,(255,255,255))
    screen.blit(score,(int(x),int(y)))
def game_over_text():
    over_text=over_font.render("GAME OVER",True,(255,255,255))
    screen.blit(over_text,(200,250))
def won():
    won=won_font.render("YOU WON",True,(255,255,255))
    screen.blit(won,(250,250))
    

def player(x, y):                                                       
    screen.blit(image, (int(x), int(y)))
def enemy(x, y,i):                                                    
    screen.blit(enemy_image[i], (int(x), int(y)))
def monster(x,y):
    screen.blit(monstership,(x,y))
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
def iscollisionBM(monsterX,monsterY,bulletX,bulletY):
    dis3=math.sqrt((math.pow(monsterX-bulletX,2))+(math.pow(monsterY-bulletY,2)))
    if dis3<70:
        return True
    else:
        return False
def iscollisionM(playerX,playerY,monsterX,monsterY):
    dis2=math.sqrt((math.pow(playerX-monsterX,2))+(math.pow(playerY-monsterY,2)))
    if dis2<108:
        return True
    else:
        return False
def level2():
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
    global monster_changeX
    global monster_changeY
    global monsterX
    global monsterY
    global counterB
    
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(bg,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    player_changeX=-7
                if event.key==pygame.K_RIGHT:
                    player_changeX=7
                if event.key==pygame.K_DOWN:
                    player_changeY=7
                if event.key==pygame.K_UP:
                    player_changeY=-7
                if event.key==pygame.K_SPACE:
                    if bullet_state=="ready":
                        bullet_sound=mixer.Sound("laser.wav")
                        bullet_sound.play()
                        bulletX=playerX
                        bulletY=playerY
                        fire_bullet(bulletX,bulletY)
                    
                    
                
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT or event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                    player_changeX=0
                    player_changeY=0
            if playerX <= 0:                                              
                playerX = 0                                                 
            if playerX >= 734:                                           
                playerX = 734                                                
            if playerY <= 0:                                                
                playerY = 0
            if playerY>=536:
                playerY = 536
        for i in range(no_of_enemies):
              if enemyY[i]>500:
                  for j in range(no_of_enemies):
                      enemyY[j]=2000

                  
            
              enemyX[i]+=enemy_changeX[i]
              if enemyX[i] <= 0:
                    enemy_changeX[i]=8
                    enemyY[i]+=enemy_changeY[i]
              elif enemyX[i] >= 736:
                    enemy_changeX[i]=-8
                    enemyY[i]+=enemy_changeY[i]
              collision=iscollision(enemyX[i],enemyY[i],bulletX,bulletY)
              collisionb=iscollisionB(playerX,playerY,enemyX[i],enemyY[i])
              if collision:
                    exp_sound=mixer.Sound("explosion.wav")
                    exp_sound.play()
                    bulletY=550
                    bullet_state="ready"
                    score_val+=5
                    high_score.push(score_val)
                    enemyX[i]=random.randint(0, 735) 
                    enemyY[i]=random.randint(50, 100)
              enemy(enemyX[i],enemyY[i],i)
              if collisionb:
                  game_over_text()
                  final_score(230,320)
                  running=False
                  
               
        if bullet_state=="fired":
            fire_bullet(bulletX,bulletY)
            bulletY-=bullet_changeY
        if bulletY<=0:
            bulletY=550
            bullet_state="ready"
        if score_val>50:
            for i in range(no_of_enemies):
                  for j in range(no_of_enemies):
                      enemyY[j]=1000
            monsterX+=monster_changeX
            if monsterX<= 0:
                    monster_changeX=7
                    monsterY+=monster_changeY
            elif monsterX >= 736:
                    monster_changeX=-7
                    monsterY+=monster_changeY
            collisionM=iscollisionM(playerX,playerY,monsterX,monsterY)
            collisionBM=iscollisionBM(monsterX,monsterY,bulletX,bulletY)
            if collisionBM:
                exp_sound=mixer.Sound("explosion.wav")
                exp_sound.play()
                bulletY=550
                bullet_state="ready"
                score_val+=5
                high_score.push(score_val)
                counterB=counterB+1
                if counterB==30:
                    won()
                    running=False
                    
                
                
            
            if collisionM:
                  game_over_text()
                  final_score(230,320)
                  running=False
            monster(monsterX,monsterY)
                
            
            
            

                            
        playerX+=player_changeX
        playerY+=player_changeY
        player(playerX,playerY)
        show_score(textX,textY)
        next1(650,10)
        pygame.display.update()
            
           

