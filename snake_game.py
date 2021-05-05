import pygame,os
import sys
from pygame.locals import*
import random
from pygame import mixer   #import for music

pygame.mixer.pre_init(44100, -16,2,512)
mixer.init()

os.environ['SDL_VIDEO_WINDOW_POS']="%d,%d"%(0,0) # set position of window 

#load sounds
pygame.mixer.music.load('img/music.wav')  #background music
pygame.mixer.music.play(-1,0.0,200)
game_over_fx=pygame.mixer.Sound('img/game_over.wav')  
game_over_fx.set_volume(0.5)

#load image
snake_img = pygame.image.load('img/snake.png')


class Snake(object):
    def __init__(self):
        self.length=1
        self.positions=[((screen_width/2),(screen_height/2))]
        self.direction=random.choice([up,down,left,right])
        self.color=(17,24,47)
        self.score=0
    def get_head_position(self):
        return self.positions[0]
    def turn(self,point):
        if self.length>1 and (point[0]* -1,point[1]* -1) ==self.direction:
            return
        else:
            self.direction=point
    def move(self):
        cur=self.get_head_position()
        x,y=self.direction
        new=( (( cur[0]+(x*grid_size))% screen_width ), (cur[1]+(y*grid_size))%screen_height)
        if len(self.positions)>2 and new in self.positions[2:]:
            game_over_fx.play();self.reset()
        else:
            self.positions.insert(0,new)
            if len(self.positions)>self.length:
                self.positions.pop()
    def reset(self):
            self.length=1
            self.positions=[((screen_width/2),(screen_height/2))]
            self.direction=random.choice([up,down,left,right])
            self.score=0
            
    def draw(self,surface):
        for p in self.positions:
            r=pygame.Rect((p[0],p[1]),(grid_size,grid_size)) # size of snake grid
            pygame.draw.rect(surface,self.color,r)
            pygame.draw.rect(surface,(93,216,228),r,1)
            
            
    def handle_keys(self):
            
            for event in pygame.event.get():
                if event.type==QUIT: #quit the game to use of mouse across cross section
                    pygame.quit()
                    sys.exit()
                if event.type ==pygame.KEYDOWN:
                        if event.key==pygame.K_SPACE:#press SPACE_BAR for quit the game
                            pygame.quit()
                            sys.exit()
                                         
                            
                        elif event.key==pygame.K_UP: #press up button
                            self.turn(up)
                        elif event.key==pygame.K_DOWN: #press down button
                            self.turn(down)
                        elif event.key==pygame.K_LEFT: #press left button
                            self.turn(left)
                        elif event.key==pygame.K_RIGHT: #press right button
                            self.turn(right)
                pygame.display.update()
class Food(object):
    def __init__(self):
        self.position=(0,0)
        self.color=(223,163,49)#food color
        self.randomize_Position()
        
    def randomize_Position(self):
        self.position=(random.randint(0,int(grid_width-1))*grid_size,random.randint(0,int(grid_height-1))*grid_size)

    def draw(self,surface):
        r=pygame.Rect((self.position[0],self.position[1]),(grid_size,grid_size))
        pygame.draw.rect(surface,self.color,r)
        pygame.draw.rect(surface,(93,216,228),r,1)


def drawGrid(surface):
    for y in range(0,int(grid_height)): # y co-ordinate of draw grid
        for x in range(0,int(grid_width)): # x co-ordinate of draw grid
                    if (x+y)%2==0:
                        r=pygame.Rect((x*grid_size,y*grid_size),(grid_size,grid_size))
                        pygame.draw.rect(surface,(93,216,228),r)  # color of grid=(93,216,228)
                    else:
                       rr=pygame.Rect((x*grid_size,y*grid_size),(grid_size,grid_size))
                       pygame.draw.rect(surface,(84,194,220),rr)   # color of grid=(84,194,220)
                                     
screen_width=1000#1000
screen_height=600#850 

grid_size=20 
grid_width=screen_width/grid_size
grid_height=screen_height/grid_size
    
up=(0,-1)
down=(0,1)
left=(-1,0)
right=(1,0)



def main():
    pygame.init()
    clock=pygame.time.Clock()
    screen=pygame.display.set_mode((1550,850))
    
    surface=pygame.Surface(screen.get_size())
    surface=surface.convert()
    #drawGrid(surface)
    
    #screen.blit(snake_img, (300, 900))# set snake image

    snake=Snake()
    food=Food()

    score=0
    running=True
    while running:
        clock.tick(8) # set speed of snake 
        snake.handle_keys()
        drawGrid(surface)
        snake.move()
        if snake.get_head_position()==food.position:
            snake.length +=1
            score +=1
            food.randomize_Position()
        snake.draw(surface)
        food.draw(surface)
        #handle events
        
        screen.blit(surface,(0,0))
        
        font_note = pygame.font.SysFont('Bauhaus 93', 40)
        game_name=pygame.font.SysFont('Bauhaus 93', 120).render("Snake Game...",1,(255,255,255))
        score_note=pygame.font.SysFont('Bauhaus 93', 70).render("Score: {0}".format(score),1,(255,255,255))

        text1=font_note.render("MOVE UP: UP_BUTTON",1,(220,20,0))
        text2=font_note.render("MOVE DOWN: DOWN_BUTTON",1,(220,20,0))
        text3=font_note.render("MOVE LEFT: LEFT_BUTTON",1,(220,20,0))
        text4=font_note.render("MOVE RIGHT: RIGHT_BUTTON",1,(220,20,0))
        text5=font_note.render("QUIT: SPACE_BAR",1,(220,20,0))
        
        screen.blit(game_name,(300,screen_height+40)) #set position of game_name
        screen.blit(score_note,(1050,40)) #set position of score

        screen.blit(text1,(1050,120)) #set position of text1
        screen.blit(text2,(1050,200)) #set position of text2
        screen.blit(text3,(1050,280)) #set position of text3
        screen.blit(text4,(1050,360)) #set position of text4
        screen.blit(text5,(1050,440)) #set position of text5

        Snake_img=screen.blit(pygame.transform.scale(snake_img,(80,80)),(150,640)) #set right snake image
        
        
        pygame.display.update()
        
              
main()
