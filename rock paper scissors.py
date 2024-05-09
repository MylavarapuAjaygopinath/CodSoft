import random
game_list=['Rock','Paper','Scissors']
computer=c=0
command=p=0
print("Score: Computer " + str(c) + " Player " + str(p))
run=True
while run:
    computer_choice=random.choice(game_list)
    command=input("Rock,Paper,Scissors")
    if(command==computer_choice):
        print("Tie")
    elif command=='Rock':
        if computer_choice == "Scissors":
            print("player won!")
            p+=1
        else:
            print("Computer won!")
            c+=1
    elif command=='Paper':
        if computer_choice == "Rock":
            print("player won!")
            p+=1
        else:
            print("Computer won!")
            c+=1
    elif command=="Scissors":
        if computer_choice=="Paper":
            print("player won!")
            p+=1
        else:
            print("Computer won!")
            c+=1
    else:
        print("Wrong input")
    a=int(input("Enter 1 to play again 0 to stop"))
    if a==1:
        run=True
    else:
        run=False
    print("Player: "+ command)
    print("computer: "+computer_choice)
    print(" Score: Computer "+str(c) + " player "+str(p))
