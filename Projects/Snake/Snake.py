import pygame  #importing python game
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
 
font_style = pygame.font.SysFont(None, 50) #font style and measure

def message(msg,color): #type a message depending on the color
    mesg = font_style.render(msg, True, color) #the font style of the messages in the game
    dis.blit(mesg, [dis_width/2, dis_height/2]) #the width andheight divide by 2
 
 
while not game_over: #while game is not over it keeps going
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
                
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0: #
 
    x1 += x1_change #update of the x coordinate
    y1 += y1_change #update of the y cordinate
    dis.fill(white) #filling in information for the color white
pygame.draw.rect(dis, black, [x1, y1, 10, 10]) #putting the numbers and coordinates for the color black
pygame.draw.rect(dis,blue,[200,150,10,10]) #putting the numbers of the color in a code
message("You lost",red) #putting the words "you lost" when you lose the game.
pygame.display.update()# a portion of the area get's updated
clock.tick(30) #the clock ticking with 30 seconds (helps track time)
print(event)  #printing event
pygame.quit() #runinng the code that deactivates the Pygame library (updates the screen)
quit() #it's used to exit a python program

