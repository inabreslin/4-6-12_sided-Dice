import random#this inports random

#the code below means:
#then a subroutine called questions is defined   
#then it asks the user for an imput and calls their input a variable named answer
#then if the user inputs 4 call dice4
#Then if the input is not 4 then it asks is the input 6, if so it calls dice6
#then if the input is not 4 or 6 the it asks is the input 12 if this is true it calls dice12
#then if the user does not enter 4,6 or 12 then it prints invalid answer
#then the user is asked for an input to the question do you want to quit and calls the input a variable called quiting
#if the variable quiting is Y or y it quits the program
#then it asks if the variable is not Y or y then is it N or n if it is then it calls the questions sub routine
#then if anything else is inputed it prints invalid answer.Then it calls the questions subroutine again


def questions():
    answer = input("Do you want to roll a 4  sided,6 sided or 12 sided dice?")
    if answer == ("4"):
        dice4()
    elif answer == ("6"):
        dice6()
    elif answer == ("12"):
        dice12()
    else:
        print ("Invalid Answer")
        quiting = input("Do you want to quit ?")
        if (quiting == ("y")) or (quiting == ("Y")):
            quit()
        elif (quiting == ("n")) or (quiting == ("N")):
            questions()
        else:
            print("Invalid Answer!!!")
            questions()
            
#the below code:
#dice4 is defined as a subroutine
#then a variable called dice4 is created it is a random number between 1 and 4
#then dice: is printed then whatever number is generated by dice4    
#then it prints if odd i win , if even you win
#then it calls the questions sub routine questions()

def dice4():
    dice4 = random.randrange(1,4)
    print("dice4:",dice4)
    print("even = you win!, odd - I win!!!")
    questions()

#the below code:
#dice6 is defined as a subroutine
#then a variable called dice6 is created it is a random number between 1 and 6
#then dice: is printed then whatever number is generated by dice6    
#then it prints if odd i win , if even you win
#then it calls the questions sub routine questions()

def dice6():
    dice6 = random.randrange(1,6)
    print("dice6:",dice6)
    print("even = you win!, odd - I win!!!")
    questions()
#the below code:
#dice12 is defined as a subroutine
#then a variable called dice12 is created it is a random number between 1 and 12
#then dice: is printed then whatever number is generated by dice12    
#then it prints if odd i win , if even you win
#then it calls the questions sub routine questions()

def dice12():
    dice12 = random.randrange(1,12)
    print("dice12:",dice12)
    print("even = you win!, odd - I win!!!")
    questions()

# finaly the subroutine options is called incase the program reaches the end of the code and it calls the options subroutine 

questions()
