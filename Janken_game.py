import tkinter
import random
import tkinter.font as tkfont


root = tkinter.Tk()
root.title("Rock, paper, scissor, spock, lizard")
root.geometry('600x400')


random_number = random.randint(1,5)
if random_number == 1:
    comp_choice = "rock"
elif random_number == 2:
    comp_choice = "paper"
elif random_number ==3:
    comp_choice = "scissor"
elif random_number == 4:
    comp_choice = "lizard"
elif random_number == 5:
    comp_choice = "spock"

#characters
lizard_img = '''🤏🏾'''

paper_img = '''🖐🏾'''

rock_img = '''✊🏾'''

spock_img = '''🖖🏾'''

scissor_img = '''✌🏾'''


#create functions----------

    
def rock():
    label_user_choice['text'] = rock_img
    
    
    if comp_choice == 'rock':
        label_comp_choice["text"] = rock_img
        label_result["text"] = "Tie"                  # If two values are equal, declare a tie!
    if comp_choice == 'lizard':
        label_result["text"] = "User Wins!"
        label_comp_choice["text"] = lizard_img
    elif comp_choice == 'scissor':
        label_result["text"] = "User Wins!"
        label_comp_choice["text"] = scissor_img
    elif comp_choice=='spock':
        label_result["text"] = "Comp wins!"
        label_comp_choice["text"] = spock_img
    elif comp_choice=='paper':
        label_result["text"] = "Comp wins!"
        label_comp_choice["text"] = paper_img

def paper():
    label_user_choice['text'] = paper_img


    if comp_choice == 'paper':
        label_comp_choice["text"] = paper_img
        label_result["text"] = "Tie"
    if comp_choice=='rock':
        label_result["text"] = "User Wins!"
        label_comp_choice["text"] = rock_img
    elif comp_choice == 'spock':
        label_result["text"] = "User Wins!"
        label_comp_choice["text"] = spock_img
    elif comp_choice=='scissor':
        label_result["text"] = "Comp wins!"
        label_comp_choice["text"] = scissor_img
    elif comp_choice == 'lizard':
        label_result["text"] = "Comp wins!"
        label_comp_choice["text"] = lizard_img

def scissor():
    label_user_choice['text'] = scissor_img


    if comp_choice == 'scissor':
        label_comp_choice["text"] = scissor_img
        label_result["text"] = "Tie"
    if comp_choice =='spock':
        label_result["text"] = "Comp Wins!"
        label_comp_choice["text"] = spock_img
    elif comp_choice =='paper':
        label_result["text"] = "User Wins!"
        label_comp_choice["text"] = paper_img
    elif comp_choice =='rock':
        label_result["text"] = "Comp Wins!"
        label_comp_choice["text"] = rock_img
    elif comp_choice =='lizard':
        label_result["text"] = "User Wins!"
        label_comp_choice["text"] = lizard_img

def lizard():
    label_user_choice['text'] = lizard_img


    if comp_choice == 'lizard':
        label_comp_choice["text"] = lizard_img
        label_result["text"] = "Tie"
    if comp_choice == 'paper':
        label_result["text"] = "User Wins!"
        label_comp_choice["text"] = paper_img
    elif comp_choice == 'spock':
        label_result["text"] = "User Wins!"
        label_comp_choice["text"] = spock_img
    elif comp_choice == 'scissor':
        label_result["text"] = "Comp Wins!"
        label_comp_choice["text"] = scissor_img
    elif comp_choice == 'rock':
        label_result["text"] = "Comp Wins!"
        label_comp_choice["text"] = rock_img


def spock():
    label_user_choice['text'] = spock_img


    if comp_choice == 'spock':
        label_comp_choice["text"] = spock_img
        label_result["text"] = "Tie"
    if comp_choice == 'rock':
        label_result["text"] = "User Wins!"
        label_comp_choice["text"] = rock_img
    elif comp_choice == 'scissor':
        label_result["text"] = "User Wins!"
        label_comp_choice["text"] = scissor_img
    elif comp_choice == 'paper':
        label_result["text"] = "Comp Wins!"
        label_comp_choice["text"] = paper_img
    elif comp_choice == 'lizard':
        label_result["text"] = "Comp Wins!"
        label_comp_choice["text"] = lizard_img

def reset():
    global comp_choice
    random_number = random.randint(1,5)
    if random_number == 1:
        comp_choice = "rock"
    elif random_number == 2:
        comp_choice = "paper"
    elif random_number ==3:
        comp_choice = "scissor"
    elif random_number == 4:
        comp_choice = "lizard"
    elif random_number == 5:
        comp_choice = "spock"

    label_comp_choice["text"] = ""
    label_user_choice["text"] = ""
    label_result["text"] = "choose...."




#create widgets------------
label_result = tkinter.Label(root, text = "choose one....", font = 'bold')
label_result.pack()

button_rock = tkinter.Button(root, text ="Rock", command = rock, fg='yellow', bg='black', height = 2, width = 4)
button_rock.pack()

button_paper = tkinter.Button(root, text ="paper", command = paper, fg='yellow', bg='black', height = 2, width = 4)
button_paper.pack()

button_scissor = tkinter.Button(root, text ="scissor", command = scissor, fg='yellow', bg='black', height = 2, width = 4)
button_scissor.pack()

button_lizard = tkinter.Button(root, text ="lizard", command = lizard, fg='yellow', bg='black', height = 2, width = 4)
button_lizard.pack()

button_spock = tkinter.Button(root, text ="spock", command = spock, fg='yellow', bg='black', height = 2, width = 4)
button_spock.pack()

label_comp_choice = tkinter.Label(root, text = "")
label_comp_choice.pack()

label_user_choice = tkinter.Label(root, text = "") 
label_user_choice.pack()

button_reset = tkinter.Button(root, text ="reset", command = reset, fg='green', bg='black', height = 3, width = 5)
button_reset.pack()





root.mainloop() 