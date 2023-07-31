import pygame 
import time 
import random

pygame.init()

#declaring all the colors 
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
grennish = (153,255,51)
yellow = (255,255,51)
blue = (0,0,255)
cyan = (224,255,255)
cyan_pure = (187,255,238,255)
test = (74, 24, 168)
brown = (58.8,29.4,0)

#declaring the size of display window 
display_width = 600
display_height = 400

#creating a display 
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Snake Game")

#declaring a variable related to to create a boundary 
snake_block = 10 

#declaring a variable to create snake speed 
snake_speed = 20

clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 20)
def score(score):
    value = font.render("score: " + str(score),True,test)
    display.blit(value, [0,0])

def big_snake(snake_block, list_snake):
    for x in list_snake:
        pygame.draw.rect(display,black, [x[0],x[1],snake_block,snake_block]) 

def gameLoop():
    game_over = False 
    game_close = False 
    game_start = False 
    
    x1 = display_width / 2
    y1 = display_height / 2
    
    x1_change = 0 
    y1_change = 0 
    
    snake_list = []
    length_of_snake = 1 
    
    foodx = round(random.randrange(0,display_width - (1.5*snake_block))/ 10.0)*10.0
    foody = round(random.randrange(0, display_height - (3*snake_block)) / 10.0)*10.0 
    
    
    while not game_over:
         #loading music 
        pygame.mixer.music.load("game-start.mp3")
        #setting volume
        pygame.mixer.music.set_volume(0.2)
        #Play the music
        pygame.mixer.music.play()
        while game_start == False and game_over == False : 
            display.fill(cyan_pure)
            myfont = pygame.font.SysFont("Britannic Bold",40)
            myfont2 = pygame.font.SysFont("Britannic Bold",25)
            text = myfont.render("Welcome " + "Start Screen",True, red )
            text2 = myfont2.render("Press any key to start",True,black)
            image = pygame.image.load("snake_final.jpg").convert()
            width = image.get_rect().width
            height = image.get_rect().height
            image = pygame.transform.scale(image,(width/8,height/12))
            display.blit(text, (150,200))
            display.blit(text2, (210, 235))
            display.blit(image,(175,30))
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    game_start = True 
                    #stopping music after game is over 
                    pygame.mixer.music.stop()
        #loading music 
        pygame.mixer.music.load("game_over.mp3")
        #setting volume
        pygame.mixer.music.set_volume(0.2)
        #Play the music
        pygame.mixer.music.play()  
        while game_close == True :
            
            bg = pygame.image.load("background_end.jpeg")
            width = bg.get_rect().width
            height = bg.get_rect().height
            bg = pygame.transform.scale(bg,(width,height*1.25))
            display.blit(bg,(-10,0))
            myfont3 = pygame.font.SysFont("inkfree",25)
            text3 = myfont.render("Press Q - Quit or P - Play Again",True ,cyan)
            display.blit(text3,(80,50))
            score(length_of_snake - 1)
            pygame.display.update()
            
            for event in pygame.event.get():        
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True 
                        game_close = False
                        game_start = True 
                    if event.key == pygame.K_p:
                        gameLoop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True 
            if event.type == pygame.KEYDOWN:    
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0 
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0 
                elif event.key == pygame.K_UP:
                    x1_change = 0 
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0 
                    y1_change = snake_block
                
        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True 
            
        x1 += x1_change
        y1 += y1_change
        
        #putting a bg image 
        bg = pygame.image.load("background.png")
        width = bg.get_rect().width
        height = bg.get_rect().height
        bg = pygame.transform.scale(bg,(width*2,height*2))
        display.blit(bg,(0,0))
        
        pygame.draw.rect(display,red,[foodx, foody, snake_block, snake_block])   
                           
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        
        if len(snake_list) > length_of_snake:
            del snake_list[0]
            
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True 
                
        big_snake(snake_block, snake_list)
        score(length_of_snake - 1 )
        pygame.display.update()
        
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - (1.5*snake_block))/ 10.0) * 10.0
            foody = round(random.randrange(0, display_height - (3*snake_block))/ 10.0) * 10.0
            length_of_snake += 1        
        
        clock.tick(snake_speed)
        
    pygame.quit()
    quit()
    
        
gameLoop()
