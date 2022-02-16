import random
word_list = ["San Juan","Bayamon","Guayanilla","Loiza","Isabela","Lajas","Quebradillas","Lares","Trujillo Alto","Orocovis","Gurabo","Toa Alta","Guaynabo","Condado","Caguas","San German","Humacao","Aguas Buenas","Arecibo","Culebra"]

random.choice()

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

print(steps[0])