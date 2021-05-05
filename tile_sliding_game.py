import pygame,sys,os,random
import time
from pygame.locals import*
#grid size =gs
#size of the tile =ts
#size of the margin =ms

# define colour
white =(255,255,255)
black=(0,0,0)
red =(255,0,0)
brown=(100,40,0)

from pygame import mixer   #import for music

pygame.mixer.pre_init(44100, -16,2,512)
mixer.init()

#load sounds
pygame.mixer.music.load('img/music.wav')  #background music
pygame.mixer.music.play(-1,0.0,200)

def Main_loop():
    pygame.init()
    os.environ["SLIDING PUZZLE GAME"]='1'
    pygame.display.set_caption('sliding puzzle')
    screen=pygame.display.set_mode((1550,850))#(1000,600))
    fpsclock =pygame.time.Clock()

    class SlidePuzzle:
        speed=600
        prev =None
        def __init__(self,gs,ts,ms):
            self.gs,self.ts,self.ms =gs,ts,ms

            self.tiles_len =gs[0]* gs[1]-1   #how many tiles we have
            

            self.tiles =[(x,y) for y in range(gs[1]) for x in range(gs[0])]

            self.tilepos = [(x*(ts+ms)+ms,y*(ts+ms)+ms) for y in range(gs[1]) for x in range(gs[0])] #actual pos on screen
            self.tilePOS = {(x,y): (x*(ts+ms)+ms,y*(ts+ms)+ms) for y in range(gs[1]) for x in range(gs[0])}  # the place they slide to
            #............................in above section create grid......
            
            self.rect =pygame.Rect(0,0,gs[0]*(ts+ms)+ms,gs[1]*(ts+ms)+ms)
            pic=pygame.transform.scale(pygame.image.load('img/images(6).jpeg'),self.rect.size) 
            
            #w,h =gs[0]*(ts+ms)+ms ,gs[1]*(ts+ms)+ms   #image height and width
            
            self.images=[];   font=pygame.font.Font(None,0)
            
            for i in range(self.tiles_len):
                x,y=self.tilepos[i]  #pos of tile in image  self.tilepos[i]

                image=pic.subsurface(x,y,ts,ts)
                text=font.render(str(i+1),2,(10,10,10));
                w,h=text.get_size()    #(10,10,10) use text color
                
                image.blit(text,((ts-w)/2,(ts-h)/2));  self.images+=[image]
              
            

        def getBlank(self): return self.tiles[-1]
        def setBlank(self,pos): self.tiles[-1] =pos
        opentile =property(getBlank,setBlank)

        def switch(self,tile):
            if self.sliding(): return
            self.tiles[self.tiles.index(tile)],self.opentile=self.opentile,tile

        def in_grid(self,tile): return tile[0]>=0 and tile[0]<self.gs[0] and tile[1]>=0 and tile[1]<self.gs[1]
        def adjacent(self): x,y =self.opentile;  return(x-1,y),(x+1,y),(x,y-1),(x,y+1)
        def random(self):
            adj=self.adjacent()
            self.switch(random.choice([pos for pos in adj if self.in_grid(pos) and pos!=self.prev]))

        def update(self,dt):
            
            mouse=pygame.mouse.get_pressed()
            mpos=pygame.mouse.get_pos()
            if mouse[0]:
                x ,y =mpos[0]%(self.ts+self.ms), mpos[1]%(self.ts+self.ms)
                if x > self.ms and y > self.ms:
                    tile=mpos[0]//self.ts,mpos[1]//self.ts
                    if self.in_grid(tile) and tile in self.adjacent(): self.switch(tile)
           
                        # find tile mouse is on
                        # if held, switch, as long as the blank is adjacent
            s=self.speed*dt
            for i in range(self.tiles_len):
                x,y =self.tilepos[i]   # current pos
                X,Y =self.tilePOS[self.tiles[i]]   # target pos
                dx=X-x ;  dy=Y-y
                self.tilepos[i]=(X if abs(dx)<s else x+s if dx>0 else x-s),(Y if abs(dy)<s else y+s if dy>0 else y-s),  #movement of slid
                    

        def draw(self,screen):
            for i in range(self.tiles_len):  
                            x,y =self.tilepos[i]   # self.tilepos[i]
                            screen.blit(self.images[i],(x,y))  # set position of the text x,y
                           

        def sliding(self):
            for i in range(self.tiles_len):
                x,y=self.tilepos[i]; X,Y =self.tilePOS[self.tiles[i]]  #pos, target
                if x!=X and y!=Y: return True

        
        def events(self,event):   #keyboard interface
            if event.type ==pygame.KEYDOWN:
                for key,dx,dy in ((pygame.K_w,0,-1),(pygame.K_s,0,1),(pygame.K_a,-1,0),(pygame.K_d,1,0)):   # work with w,s,a,d, key in keyboard
                    if event.key == key:
                        x,y =self.opentile; tile =x+dx,y+dy
                        if self.in_grid(tile): self.switch(tile)

                if event.key ==pygame.K_UP:#press up button to mix the slide
                    for i in range(100):
                        self.random()
                if event.key ==pygame.K_SPACE:#press space bar to quit the game
                    pygame.quit()
                    sys.exit()


       
    #............................level of game..............................
    def draw_text(display,text,x,y):
            font=pygame.font.Font(None,40)
            text_surface=font.render(text,True,brown)
            text_rect=text_surface.get_rect()
            text_rect.midtop=(x,y)
            screen.blit(text_surface,(10,550))

    def makeText(text,color,bgcolo,top,left):
            font=pygame.font.Font(None,40)
            textSurf=font.render(text,True,(0,0,255),(255,0,0))
            textRect=textSurf.get_rect()
            textRect.topleft=(top,left)
            return(textSurf,textRect)
    def level_screen():
        L1,L1_RECT=makeText('Level 1',red,True,30,600)
        L2,L2_RECT=makeText('Level 2',red,True,210,600)
        L3,L3_RECT=makeText('Level 3',red,True,420,600)
        L4,L4_RECT=makeText('Level 4',red,True,630,600)
       
        screen.blit(L1,L1_RECT)
        screen.blit(L2,L2_RECT)
        screen.blit(L3,L3_RECT)
        screen.blit(L4,L4_RECT)
       
        mpos=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if L1_RECT.collidepoint(mpos):
                level1()
            elif L2_RECT.collidepoint(mpos):
                level2()
                
                
            elif L3_RECT.collidepoint(mpos):
                    level3()
                    
            elif L4_RECT.collidepoint(mpos):
                level4()
               
                




    def level1():
        color=(255,0,0)
        program=SlidePuzzle((3,3),140,5)
        while True:
            dt=fpsclock.tick()/1000
            screen.blit(screen,(0,0))
            draw_text(screen,'PRESS UP_BUTTON MANY TIME TO MIX THE SLIDE ANY!',300,500)
            program.draw(screen)
            pygame.display.flip()
            screen.fill(color,(0,0,500,600))  # set right hand side image size
            #level_screen()
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT: pygame.quit(); sys.exit()
                program.events(event)
            
            program.update(dt)


    def level2():
        color=(255,0,0)
        program=SlidePuzzle((4,4),90,5)
        while True:
            dt=fpsclock.tick()/1000
            screen.blit(screen,(0,0))
            draw_text(screen,'PRESS UP_BUTTON MANY TIME TO MIX THE SLIDE ANY!',300,500)
            program.draw(screen)
            pygame.display.flip()
            screen.fill(color,(0,0,500,600))  # set right hand side image size
            #level_screen()
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT: pygame.quit(); sys.exit()
                program.events(event)
            
            program.update(dt)

    def level3():
        color=(255,0,0)
        program=SlidePuzzle((5,5),80,5)
        while True:
            dt=fpsclock.tick()/1000
            screen.blit(screen,(0,0))
            draw_text(screen,'PRESS UP_BUTTON MANY TIME TO MIX THE SLIDE ANY!',300,500)
            program.draw(screen)
            pygame.display.flip()
            screen.fill(color,(0,0,500,600))  # set right hand side image size
            #level_screen()
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT: pygame.quit(); sys.exit()
                program.events(event)
            
            program.update(dt)

    def level4():
        color=(255,0,0)
        program=SlidePuzzle((6,6),60,5)
        while True:
            dt=fpsclock.tick()/1000
            screen.blit(screen,(0,0))
            draw_text(screen,'PRESS UP_BUTTON MANY TIME TO MIX THE SLIDE ANY!',300,500)
            program.draw(screen)
            pygame.display.flip()
            screen.fill(color,(0,0,500,600))  # set right hand side image size
            #level_screen()
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT: pygame.quit(); sys.exit()
                program.events(event)
            
            program.update(dt)    

    def main():
        
        program=SlidePuzzle((3,3),140,5)   # we can change this value to tough the game
        game_over=True
        game_running=True
        run=True
        while run:
            for i in range(100):   #call random function
                program.random()
            dt=fpsclock.tick()/1000
            program.draw(screen)
            pygame.display.flip()
            

            screen.fill(red,(0,0,790,690))  # set left hand side image size
            img=pygame.image.load('img/images(6).jpeg')

            font=pygame.font.Font('freesansbold.ttf',30)
            text=font.render("SLIDING PUZZLE GAME !",True,(255,255,255))
            textRect=text.get_rect()
            textRect=(1000,50)  # set position of text
            screen.blit(text,textRect)
            
            IMAGE_RIGHT=screen.blit(pygame.transform.scale(img,(600,600)),(900,80)) #set right hand side image

            text=font.render("QUIT: SPACE_BAR'",True,(255,255,255))
            textRect=text.get_rect()
            textRect=(200,750)  # set position of text
            screen.blit(text,textRect)
            
           

            for event in pygame.event.get():
                if event.type==QUIT: #quit the game to use of mouse across cross section
                    pygame.quit()
                    sys.exit()
                if event.type ==pygame.KEYDOWN:
                    if event.key ==pygame.K_SPACE:#press space bar to quit the game
                        pygame.quit()
                        sys.exit()

            level_screen()
            program.update(dt)


        
            

    #if __name__=='__main__':
    main()
        

Main_loop()
