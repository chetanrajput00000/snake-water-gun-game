
import random


# function
def winner(computer,your_turn):

    if (computer==your_turn) :
        return None

    elif (computer=='snake'):
        if (your_turn=='water'):
            return False
        else:
            (your_turn=='gun')
            return True

    elif (computer=='water'):
        if (your_turn=='gun'):
            return False
        else:
            (your_turn=='snake')
            return True

    elif (computer=='gun'):
        if (your_turn=='snake'):
            return False
        else:
            (your_turn=='water')
            return True                
                   


# python_random_module

# computer_condition
print("computer turn : snake(s) , water(w) , gun(g)?")
RandNo=random.randint(1,3)
print(RandNo )

if RandNo==1:
    computer='snake'
elif RandNo==2:
    computer='water'
elif RandNo==3:
    computer='gun'   



# your_turn
print("your turn: snake(s) , water(w) , gun(g)")         

your_turn=input("select your option[snake , water , gun ]? \n")

   


# recursion_function
x=winner(computer,your_turn)


# return_result
if (x==None):
    print("the game is a TIE!\n")
elif (x==False):
    print("YOU LOOSE, Do not get angry TRy Again!\n")
else :
    # (x==True)  #optional condition
    print("YOU WIN! Keep PLAying Buddy\n") 


# result_tell_condition
print(f"computer choose : {computer}")
print(f"you choose :{your_turn}")





