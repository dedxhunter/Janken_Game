import random

# Snake Water Gun or Rock Paper Scissors
def gameWin(comp, you):
    # If two values are equal, declare a tie!
    if comp == you:
        return None

    # Check for all possibilities when computer chose rock
    elif comp == 'rock':
        if you == 'lizard':
            return False
        elif you == 'scissor':
            return False
        elif you=='spock':
            return True
        elif you=='paper':
            return True
        
    
    # Check for all possibilities when computer chose paper
    elif comp == 'paper':
        if you=='rock':
            return False
        elif you == 'spock':
            return False
        elif you=='scissor':
            return True
        elif you == 'lizard':
            return True
    
    # Check for all possibilities when computer chose scissor
    elif comp == 'scissor':
        if you=='spock':
            return False
        elif you=='paper':
            return False
        elif you=='rock':
            return True
        elif you=='lizard':
            return True
    
    #check for all possibilities when computer chose lizard
    elif comp == 'lizard':
        if you == 'paper':
            return False
        elif you == 'spock':
            return False
        elif you == 'scissor':
            return True
        elif you == 'rock':
            return True
        

    #check for all possibilities when computer chose spock
    elif comp == 'spock':
        if you == 'rock':
            return False
        elif you == 'scissor':
            return False
        elif you == 'paper':
            return True
        elif you == 'lizard':
            return True
       
print("Comp Turn: rock(r) paper(p) Scissor(s) lizard(l) or spock(sp)?")
randNo = random.randint(1, 5) 
if randNo == 1:
    comp = 'rock'
elif randNo == 2:
    comp = 'paper'
elif randNo == 3:
    comp = 'scissor'
elif randNo == 4:
    comp = 'lizard'
elif randNo == 5:
    comp = 'spock'

you = input("Your Turn: rock(r) paper(p) Scissor(s) lizard(l) or spock(sp)?")
a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")