import random

Osvaldochoice=input("rock","paper","scissors")
Computerchoice:random.choice("scissors","rock","paper")
print(f"Computer selected: {Computerchoice}")
x = 45

if(x == 0):
    print("The value of x is 0")
elif(x > 50):
  print("The value of x is more than 50")
else:
    print("The value of x is lower than 50, and is not 0")

    import random

foo = ['rock', 'paper', 'scissors']
computerChoice = random.choice(foo)
print(f"Computer selected: {computerChoice}")

if(computerChoice == Osvaldochoice):
     print("tied")
elif(computerChoice == "scissors" and Osvaldochoice == "rock"):
     print("Iwin")
elif(computerChoice == "paper" and Osvaldochoice == "rock"):
     print("computerwon")
elif(computerChoice == "rock" and Osvaldochoice == "paper"):
    print("Iwin")
elif(computerChoice == "paper" and Osvaldochoice == "scissors"):
    print("Iwin")