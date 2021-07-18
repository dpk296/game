#collision concept when bullet hit enemy then ther eit will do some affect
import pygame
import random
import math
pygame.init()
screen=pygame.display.set_mode((612,612))
pygame.display.set_caption("pk gamming")
background=pygame.image.load("background.jpg")

#player image
playerimage=pygame.image.load("player.png")
playerx=300
playery=542
playerx_chainge=0


#enemy image
enemyimage=[]
enemyx=[]
enemyy=[]
enemyx_chainge=[]
enemyy_chainge=[]

no_of_enemys=6
for i in range(no_of_enemys):

	enemyimage.append(pygame.image.load("enemy2.png"))
	enemyx.append(random.randint(0,409))
	enemyy.append(random.randint(25,100))
	enemyx_chainge.append(0.3)
	enemyy_chainge.append(30)

#bullet image
# ready- you caunt see bulet on the screen
#fire-the bullet is currently moving
bulletimage=pygame.image.load("bullet.png")
bulletx=318
bullety=542

#bullet doesent move in x direction so it is zero
bulletx_chainge=0
bullety_chainge=2
bullet_state="ready"

score=0

def player(x,y):
	screen.blit(playerimage,(x,y))

def enemy(x,y,i):
	screen.blit(enemyimage[i],(x,y))

def fire_bullet(x,y):
	global bullet_state
	bullet_state="fire"
	screen.blit(bulletimage,(x,y))

def iscollision(enemyx,enemyy,bulletx,bullety):
	distance=math.sqrt(math.pow(enemyx-bulletx,2)+(math.pow(enemyy-bullety,2)))
	if distance<50:
		return True
	else:
		return False


close=True
while close:
	screen.fill((0,0,0))
	#background image
	screen.blit(background,(0,0))
	for event in pygame.event.get():
		#print(event)
		if event.type==pygame.QUIT:
			close=False
	
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_LEFT:
				playerx_chainge=-0.9

			if event.key==pygame.K_RIGHT:
				playerx_chainge=0.9

			if event.key==pygame.K_SPACE:
				if bullet_state is "ready":
					bulletx=playerx
					fire_bullet(bulletx,playery)

		if event.type==pygame.KEYUP:
			if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
				playerx_chainge=0
		
	playerx += playerx_chainge
	
	if playerx <=0:
		playerx=0
	elif playerx >=542:
		playerx=542

#enemy movment
	for i in range(no_of_enemys):
		enemyx[i] += enemyx_chainge[i]
		if enemyx[i] <=0:
			enemyx_chainge[i]=0.3
			enemyy[i]+=enemyy_chainge[i]
		elif enemyx[i] >=497:
			enemyx_chainge[i]=-0.3
			enemyy[i]+=enemyy_chainge[i]

		#collision
		collision=iscollision(enemyx[i],enemyy[i],bulletx,bullety)
		if collision:
			bullety=542
			bullet_state="ready"
			score+=1
			print(score)
			enemyx[i]=random.randint(0,409)
			enemyy[i]=random.randint(50,100)

		enemy(enemyx[i],enemyy[i],i)


#bullet movment
	if bullety<=0:
		bullety=542
		bullet_state="ready"
	
	if bullet_state is "fire":
		fire_bullet(bulletx+20,bullety)
		bullety-=bullety_chainge
   
	#collision
	collision=iscollision(enemyx[i],enemyy[i],bulletx,bullety)
	if collision:
		bullety=542
		bullet_state="ready"
		score+=1
		print(score)
		enemyx[i]=random.randint(0,409)
		enemyy[i]=random.randint(50,100)

	player(playerx,playery)
	pygame.display.update()


