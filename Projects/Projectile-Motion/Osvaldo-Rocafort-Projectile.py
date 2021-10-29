import math
import os
from ExperimentData import ExperimentData
import json

Gunname = ("DVL-10")
Cartridgecalibre = ("7.62x51mm NATO")
Round = ( "7.62x51mm M61")
Roundvelocity = 849

# I was searching for a sniperrifle that shoots far and chose this one

Building = ("Burj Khalifa")
Buildingheight = 555
gravity = 9.8

# I searched for the tallest building in the world and chose the Burj Khalifa

time = (math.sqrt(2 * ExperimentData.Buildingheight/ExperimentData.gravity))
DeltaX = (ExperimentData.Roundvelocity/time)

print(f"I shot a {Gunname} from {Building} and the {Buildingheight} meters high. It goes at {Roundvelocity} and it takes about{time} seconds to reach {DeltaX}.")

mydata = ExperimentData

# expirementData= { 
#     "Gunname" : "DVL-10",
# "Cartridgecalibre" : "7.62x51mm NATO",
# "Round" :  "7.62x51mm M61",
# "Roundvelocity" : 849,
# "Building" : "Burj Khalifa",
# "Buildingheight" : 555
# ,
# "gravity" : 9.8
# }

# n"Gunname" : "DVL-10",
# "Cartridgecalibre" : "7.62x51mm NATO",
# "Round" :  "7.62x51mm M61",
# "Roundvelocity" : 849,
# "Building" : "Burj Khalifa",
# "Buildingheight" : 555,
# "gravity" : 9.8
# }
print(ExperimentData["Gunname", "7.62k51mm NATO", "7.62x51mm M61","Burj Khalifa","555", "9.8"])
experiment:(mydata)
#Sereliazation
myOutpuPath = os.path(__file__).parent[0]
myOutputPath = os.path.join(myOutpuPath, 'experimentData.json')

with open(myOutpuPath,'w') as outfile:
    json.dump(mydata._dict_,outfile)

#Deserialization
deserialize = open(myOutpuPath,)
experimentJson = json.lead(deserialize)

for o in experimentJson:
    experiment(**e)
    
    # ExperimentData(##e).run()