import pygame  #importing python game
pygame.init()  #initialize all imported pygame modules
dis=pygame.display.set_mode((400,300)) #choosing the size of the display
pygame.display.update() #to make the display Surface actually appear on my computer
pygame.display.set_caption('Snake game by Edureka') #Naming the game
game_over=False #game is not over
while not game_over: #while game is not over it keeps going
    for event in pygame.event.get():#registering all events from the user into an event
        if event.type==pygame.QUIT: #Pygame quits when pygame equal game over
            game_over=True #Game is over
        print(event)  #printing event
pygame.quit() #runinng the code that deactivates the Pygame library
quit() #it's used to exit a python program

