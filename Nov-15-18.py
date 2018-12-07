

def print_table():
    print(" "+my_list[0]+" | "+my_list[1]+" | "+my_list[2])
    print("____________")
    print(" "+my_list[3]+" | "+my_list[4]+" | "+my_list[5])
    print("____________")
    print(" "+my_list[6]+" | "+my_list[7]+" | "+my_list[8])


def A_input():
    while True:
        
        positionA = input("player A chose a place to put your chess")
        if positionA not in ['1','2','3','4','5','6','7','8','9']:
            print("sorry you put the chess on the wrong spot,please do it again!")
        elif my_list[int(positionA)-1]=="X" or my_list[int(positionA)-1]=="O":
            print("sorry this place is occupied,please do it again!")     
        else:
            my_list[int(positionA)-1]="X"
            break
    

def B_input():
    while True:
            
        positionB = input("player B chose a place to put your chess")
        if positionB not in ['1','2','3','4','5','6','7','8','9']:
            print("sorry you put the chess on the wrong spot,please do it again!")
        elif my_list[int(positionB)-1]=="X" or my_list[int(positionB)-1]=="O":
            print("sorry this place is occupied,please do it again!")     
        else:
            my_list[int(positionB)-1]="O"
            break
        
            
def pend_table():
    if  (my_list[0]==my_list[1]==my_list[2]=="X"or
        my_list[3]==my_list[4]==my_list[5]=="X"or 
        my_list[6]==my_list[7]==my_list[8]=="X"or 
        my_list[0]==my_list[3]==my_list[6]=="X"or
        my_list[1]==my_list[4]==my_list[7]=="X"or 
        my_list[2]==my_list[5]==my_list[8]=="X"or
        my_list[1]==my_list[4]==my_list[7]=="X"or 
        my_list[0]==my_list[4]==my_list[8]=="X"or 
        my_list[2]==my_list[4]==my_list[6]=="X"):
        print("PlayerA win the game!")
        win = True
        return win
        
    
    elif (my_list[0]==my_list[1]==my_list[2]=="O"or
        my_list[3]==my_list[4]==my_list[5]=="O"or 
        my_list[6]==my_list[7]==my_list[8]=="O"or 
        my_list[0]==my_list[3]==my_list[6]=="O"or
        my_list[1]==my_list[4]==my_list[7]=="O"or 
        my_list[2]==my_list[5]==my_list[8]=="O"or
        my_list[1]==my_list[4]==my_list[7]=="O"or 
        my_list[0]==my_list[4]==my_list[8]=="O"or 
        my_list[2]==my_list[4]==my_list[6]=="O"):
        print_table()
        print("PlayerB win the game!")
        win = True
        return win

    elif (my_list[0] in ["X","O"]and
          my_list[1] in ["X","O"]and
          my_list[2] in ["X","O"]and
          my_list[3] in ["X","O"]and
          my_list[4] in ["X","O"]and
          my_list[5] in ["X","O"]and
          my_list[6] in ["X","O"]and
          my_list[7] in ["X","O"]and
          my_list[8] in ["X","O"]):
        print("this game is a draw!")
        win = True
        return win
          
    
        
    
print("hi, I am the game designer Jesse, I just made a tic-tac-toe game")    
continuegame = input("do you want to start a new game?'YES' or 'NO'") 

while continuegame.lower() == "yes":
    my_list = ["①","②","③","④","⑤","⑥","⑦","⑧","⑨"]
    win = False
    while not win:
        print_table()
        A_input()
        print_table()
        win = pend_table()
        if win == True:
            break
        B_input()
        win = pend_table()
        if win == True:
            break
        
    continuegame = input("do you want to start a new game?'YES' or 'NO'")
print("thanks for playing my game!")

#value inside the list reassignment happens on the global scale under the defined function
#not for win(it is the reassignment of another value)


