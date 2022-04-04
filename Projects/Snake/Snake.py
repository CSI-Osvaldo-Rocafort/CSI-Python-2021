import pygame  #importing python game
import time #importing the time
import random #importing random
 
pygame.init()  #initialize all imported pygame modules

white = (255, 255, 255) #code fr the color white
black = (0, 0, 0) #code for the color black
red = (255, 0, 0) #code for the color red

dis_width = 800 #the width
dis_height  = 600 #the height

dis=pygame.display.set_mode((400,300)) #choosing the size of the display
dis = pygame.display.set_mode((800, 600)) #choosing the size of the display

pygame.display.update() #to make the display Surface actually appear on my computer
pygame.display.set_caption('Snake game by Edureka') #Will set the caption text on the top of the screen display
blue=(0,0,255) #code of the color blue
red=(255,0,0) #code of the color red
game_over=False #game is not over

x1 = dis_width/2 #width divided by 2
y1 = dis_height/2 #height divided by 2
 
snake_block=10 #the snake block equals 10

x1 = 300 #value of x1
y1 = 300 #value of y1 
 
x1_change = 0  #value if x1 changes
y1_change = 0  #value if y1 changes
 
clock = pygame.time.Clock() # time of the game
snake_speed=30 #the speed of the snake
snake_block = 10 #the  amount of the block that the snake moves around in the game
 
font_style = pygame.font.SysFont(None, 50) #putting the font style and measure
font_style = pygame.font.SysFont(None, 30) #putting the font style and measure 
 
 
def message(msg, color): #type a message depending on the color
    mesg = font_style.render(msg, True, color) #the font style of the messages in the game
    dis.blit(mesg, [dis_width/3, dis_height/3]) #the width andheight divide by 3

def message(msg,color): #type a message depending on the color
    mesg = font_style.render(msg, True, color) #the font style of the messages in the game
    dis.blit(mesg, [dis_width/2, dis_height/2]) #the width andheight divide by 2
 
 def gameLoop():  # creating a function
    game_over = False #game is not over
    game_close = False #game is not closed
 
    x1 = dis_width / 2 #dividing x1 width by 2
    y1 = dis_height / 2 #dividing y1 height by 2
 
    x1_change = 0 #the change x1 did
    y1_change = 0 #the change y1 did
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0 #calculating foodx
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0 #calculating foody
 
while not game_over: #while game is not over it keeps going
    
    while game_close == True: #while game is closing
            dis.fill(white) #making the background white
            message("You Lost! Press Q-Quit or C-Play Again", red) #putting the messsage you lost hen you lose
            pygame.display.update() #displaying update in the game
    
    for event in pygame.event.get():#registering all events from the user into an event
        if event.type==pygame.QUIT: #Pygame quits when pygame equal game over
            if event.type == pygame.QUIT:#The game resets
                game_over=True #Game is over
            if event.type == pygame.KEYDOWN: #keys to change the motion of the snake
                if event.key == pygame.K_LEFT: #pressing key to the left so the snake moves left
                    x1_change = -10 #value if x1 changes
                y1_change = 0 #value if y1 changes
            elif event.key == pygame.K_RIGHT: #pressing key to the right so the snake moves right
                x1_change = 10 #value if x1 changes
                y1_change = 0 #value if y1 changes
            elif event.key == pygame.K_UP: #pressing key upwards so the snake moves upward
                y1_change = -10 #value if y1 changes
                x1_change = 0 #value if x1 changes
            elif event.key == pygame.K_DOWN: #pressing key downwords so the snake moves downward
                y1_change = 10 #value if y1 changes
                x1_change = 0 #value if x1 changes
                
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0: #calculating if x1 is greater than y1
 
    x1 += x1_change #update of the x coordinate
    y1 += y1_change #update of the y cordinate
    dis.fill(white) #filling in information for the color white
    
    pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block]) #putting the snake blocks and foodx and y
    pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block]) #putting x1, y1 and snake block
    pygame.draw.rect(dis, black, [x1, y1, 10, 10]) #putting the numbers and coordinates for the color black
pygame.draw.rect(dis,blue,[200,150,10,10]) #putting the numbers of the color in a code
message("You lost",red) #putting the words "you lost" when you lose the game.
pygame.display.update()# a portion of the area get's updated
clock.tick(30) #the clock ticking with 30 seconds (helps track time)

print(event)  #printing event

   if x1 == foodx and y1 == foody: #x1 is equal to foodx and y1 is equal to foody
            print("Yummy!!") #printing yummy
        clock.tick(snake_speed) #clock ticking and shwoing snake's speed
 
pygame.quit() #runinng the code that deactivates the Pygame library (updates the screen)
quit() #it's used to exit a python program

gameLoop()

import pygame
import time
import random
 
pygame.init()
 
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
 
dis_width = 800
dis_height = 600
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Edureka')
 
clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 30
 
font_style = pygame.font.SysFont(None, 30)
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/3, dis_height/3])
 
 
def gameLoop():  # creating a function
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            dis.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
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
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
 
        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
        pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            print("Yummy!!")
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()


