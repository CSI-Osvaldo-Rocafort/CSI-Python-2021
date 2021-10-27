import math

Gunname = ("DVL-10")
Cartridgecalibre = ("7.62x51mm NATO")
Round = ( "7.62x51mm M61")
Roundvelocity = 849

# I was searching for a sniperrifle that shoots far and chose this one

Building = ("Burj Khalifa")
Buildingheight = 555
gravity = 9.8

# I searched for the tallest building in the world and chose the Burj Khalifa

time = (math.sqrt(2 * Buildingheight/gravity))
DeltaX = (Roundvelocity/time)