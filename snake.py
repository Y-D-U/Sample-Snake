import pygame
import random 

pygame.init()
W,H=600,600



screen=pygame.display.set_mode((W,H))
pygame.display.set_caption("MERENAMAZZ SNAKE")
body_position=[]



class Food():
    def __init__(self,r):
        self.x=150
        self.y=160
        self.r=r
        self.special=False
    def draw(self):
        while True:
            self.x,self.y=random.randint(1,W-self.r),random.randint(1,H-self.r)
            if (self.x,self.y) in body_position:
                continue
            else:
                break
        pygame.draw.circle(screen,(255,0,0),(self.x,self.y),self.r)
        if len(body_position)>0:
            body_position.pop(0)
food=Food(5)

    

    


class Snake():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.right=True
        self.left=False
        self.up=False
        self.down=False
        self.dimension=(self.x,self.y,15,15)


snake_body=[Snake(20,20)]
head=snake_body[0]
body_coor=[(head.x,head.y),0,0,0]
redraw=False

def move():
    if head.right or head.up:
        ph=1
    elif head.left or head.up:
        ph=-1
    i=1
    length=len(snake_body)

    while i < length:
        try:

            body_coor[i]=(snake_body[i].x,snake_body[i].y)            
            snake_body[i].x=body_coor[i-1][0]
            snake_body[i].y=body_coor[i-1][1]
            body_position.append((snake_body[i].x,snake_body[i].y))
            i+=1
            
        except AttributeError:
            break

def draw():
    for body in snake_body:
        body.dimension=(body.x,body.y,15,15)
        
        pygame.draw.rect(screen,(0,255,0),body.dimension)
moove=True

def drawgamewindow():
    global redraw,moove

    screen.fill((0,0,0))
    fnt=pygame.font.SysFont("comicsans",30)
    txt=fnt.render("SCORE: "+str(score),1,(0,0,220))
    screen.blit(txt,(5,2))
 
    if redraw:
        food.draw()
        redraw=False
    else:
      pygame.draw.circle(screen,(255,0,0),(food.x,food.y),food.r)  
    if moove:
        move()
    
    moove=True    
    draw()
    pygame.display.update()
run=True   

def checkselfhit():
    font=pygame.font.SysFont("comicsans",50)
    text=font.render("GAME OVER MWONA",1,(255,0,0))
    global run
    for body in snake_body[1:]:
        if head.x+15>body.x and head.x<body.x+15:
            
            if head.y+15>body.y and head.y<body.y+15:
                if not(snake_body.index(body)==1 or snake_body.index(body)==2):
                    screen.blit(text,(W//2-text.get_width()//2,H//2))
                    pygame.display.update()
                    pygame.time.delay(2000)
                    run=False
                    

    
score,start=12,0

#MAINLOOP
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    
    keys=pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_DOWN] or keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] :
        moove=True
    else:
        moove=False

    #check for movements
    if head.right==True:
        if keys[pygame.K_RIGHT] and not(keys[pygame.K_UP] or keys[pygame.K_DOWN]):
            head.left,head.up,head.down=False,True,True
            body_coor[0]=(head.x,head.y)
            head.x+=15

    if head.left :
        if keys[pygame.K_LEFT] and not(keys[pygame.K_UP] or keys[pygame.K_DOWN]):
            head.right,head.up,head.down=False,True,True
            body_coor[0]=(head.x,head.y)
            head.x-=15
    if head.down :
        if keys[pygame.K_DOWN] and not(keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
            head.up,head.left,head.right=False,True,True
            body_coor[0]=(head.x,head.y)
            head.y+=15
    if  head.up :
        if keys[pygame.K_UP] and not(keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
            head.down,head.left,head.right=False,True,True
            body_coor[0]=(head.x,head.y)
            head.y-=15


     

    #htting self
    checkselfhit()

    #Eating food
    if head.x+15>=food.x-food.r and head.x<=food.x+food.r:
        if head.y+15>=food.y-food.r and head.y<=food.y+food.r:
            body_coor.append(0)
            redraw=True
            snake_body.append(Snake(head.x,head.y))
            score+=1
            
  
    drawgamewindow()

pygame.quit()



        


    

"""game bugs :
   * Snake goes out of the screen 
   *Snake shrinks when pressed the key opposite to the direction we are moving (any solution?)
   *food appears on the snake (any solution ?) """
   







