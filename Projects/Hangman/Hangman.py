import ssl
import urllib,json
from Colors import Colors
import urllib.request

used=[]
def get_color():
    # This is discouraged but it will avoid certificate validation (prevents error)
    ssl._create_default_https_context = ssl._create_unverified_context

    # This is the URL from which we will request the data
    colorsURL = "https://random-data-api.com/api/color/random_color"

    req = urllib.request.Request(colorsURL)
    requestData = json.loads(urllib.request.urlopen(req).read())

    color:Colors = Colors(**requestData)
    
    return (color.hex_value)

myColor = get_color()


steps = ["""
    .-------.
    |       |
    |       O
    |      
    |      
    |^^^^^^^^^^^^^   
         """,
        """
    .-------.
    |       |
    |       O
    |       |
    |      
    |^^^^^^^^^^^^^
        """,
        """
    .-------.
    |       |
    |       O
    |      -|
    |
    |^^^^^^^^^^^^^
        """,
        """
    .-------.
    |       |
    |       O
    |      -|-
    |
    |^^^^^^^^^^^^^
        """,
        """
    .-------.
    |       |
    |       O
    |      -|-
    |      /
    |^^^^^^^^^^^^^
        """,
        """
    .-------.
    |       |
    |       O
    |      -|-
    |      / \\
    |^^^^^^^^^^^^^
    """
     
]
# for step in steps:
#     print(steps)
# print(steps[0])

def getInput():
    Invalid_Characters= ("1","2","3","4","5","6","7","8","9","0","10","!","@","#","$","%","^","^","&","*","(",")","-","_","=","+","[","]","{","}",":",";",",","<",".",">","/","?")

    while(True):
        letter = input("Choose letter").upper()
        
        if(len(letter)!=1):
            print("error")
            continue
        
        if(letter in Invalid_Characters):
            print("error")
            continue
        
        return letter
    
print(getInput())

def printword():
    temp:str=""
    
    for letter in myColor:
        
        if letter in used:
            temp=temp + letter
            
        
            print()
        
    
    
    