import pygame,sys
import os
import random
from pygame import mixer   #import for music
from pygame.locals import*
pygame.mixer.pre_init(44100, -16,2,512)
mixer.init()


pygame.init()

x=0
y=0

os.environ['SDL_VIDEO_WINDOW_POS']="%d,%d"%(x,y) # set position of window 

mainClock=pygame.time.Clock()

pygame.display.set_caption("Python Game Menu")
screen=pygame.display.set_mode((1550,850),0,0)

# set font
font=pygame.font.SysFont(None,50)
font_help=pygame.font.SysFont(None,30)

#load sounds
pygame.mixer.music.load('img/music.wav')  #all over game music
pygame.mixer.music.play(-1,0.0,200)

click=False

def draw_text(text,font,color,surface,x,y):
    textobj=font.render(text,1,color)
    textrect=textobj.get_rect()
    textrect.topleft=(x,y)
    surface.blit(textobj,textrect)

def main_menu():
    click=False
    while True:
        screen.fill((0,0,100))
        draw_text("MY PYGAME MENU",font,(20,20,255),screen,630,30)
        note="NOTE:-To Exit press SPACE_BAR on the keyboard."
        draw_text(note,font,(20,20,255),screen,280,700)
        
        mx,my=pygame.mouse.get_pos()

        
        
        draw_text("SNAKE GAME",font,(255,255,255),screen,630,110)
        draw_text("TILE SLIDING GAME",font,(255,255,255),screen,630,210)
        draw_text("FLAPPY BIRD GAME",font,(255,255,255),screen,630,310)
        draw_text("PLATFORM GAME",font,(255,255,255),screen,630,410)
        draw_text("HOW TO PLAY",font,(255,255,255),screen,630,510)

        button0=pygame.Rect(520,10 ,500,90)
        button1=pygame.Rect(520,100,500,50)
        button2=pygame.Rect(520,200,500,50)
        button3=pygame.Rect(520,300,500,50)
        button4=pygame.Rect(520,400,500,50)
        button5=pygame.Rect(520,500,500,50)
        
        if button1.collidepoint((mx,my)):
            if click:
                Snake_game() #game()
            
        if button2.collidepoint((mx,my)):
            if click:
                Tile_Sliding_game()
        if button3.collidepoint((mx,my)):
            if click:
                Flappy_Bird_game()
        if button4.collidepoint((mx,my)):
            if click:
                Platform_game()
        if button5.collidepoint((mx,my)):
            if click:
                help_menu()
        pygame.draw.rect(screen,(255,20,255),button1,7)
        pygame.draw.rect(screen,(255,20,255),button2,7)
        pygame.draw.rect(screen,(255,20,255),button3,7)
        pygame.draw.rect(screen,(255,20,255),button4,7)
        pygame.draw.rect(screen,(255,20,255),button5,7)
        
        click=False
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_SPACE:
                    pygame.quit()
                    sys.exit()
            if event.type==MOUSEBUTTONDOWN: #use for button click
                if event.button==1:
                    click=True
        pygame.display.update()
        mainClock.tick(60)

def game():  # demo function for menu
    running=True
    while running:
        screen.fill((30,0,0))
        
        draw_text("game",font,(255,20,25),screen,20,20)
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_SPACE:
                    running=False

        pygame.display.update()
        mainClock.tick(60)


def Snake_game():
    import snake_game

def Tile_Sliding_game():
    import tile_sliding_game

def Flappy_Bird_game():
    import flappy_bird_game    

def Platform_game():
    import platform_game


def help_menu():
    running=1 #True
    while running:
        screen.fill((30,60,70))
        
        help_text1="* SNACK GAME:-  Play with help of UP, DOWN, LEFT and RIGHT button of keyboard."
        help_text2="* FLAPPY BIRD GAME:-  Play with help of button of MOUSE."
        help_text3="* PLATFORM GAME:-  Play with help of SPACE_BAR, LEFT and RIGHT button of keyboard."
        help_text4="* TILE SLIDING GAME:-  Play with help of button of mouse."
        note="NOTE:- For Exit to press SPACE_BAR on the keyboard."
      
        
        draw_text(help_text1,font_help,(25,20,255),screen,20,50)
        draw_text(help_text2,font_help,(25,20,255),screen,20,100)
        draw_text(help_text3,font_help,(25,20,255),screen,20,150)
        draw_text(help_text4,font_help,(25,20,255),screen,20,200)
        draw_text(note,font,(25,20,255),screen,0,400)
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_SPACE:
                    running=0 #False

        pygame.display.update()
        mainClock.tick(60)  
main_menu()
