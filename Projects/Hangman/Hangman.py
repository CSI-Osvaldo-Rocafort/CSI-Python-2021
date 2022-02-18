import ssl
import urllib,json
from Colors import Colors
import urllib.request

def get_color():
    # This is discouraged but it will avoid certificate validation (prevents error)
    ssl._create_default_https_context = ssl._create_unverified_context

    # This is the URL from which we will request the data
    colorsURL = "https://random-data-api.com/api/color/random_color"

    req = urllib.request.Request(colorsURL)
    requestData = json.loads(urllib.request.urlopen(req).read())

    color:Colors = Colors(**requestData)
    
    return (color.hex_value)


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
    
