

def print_board():
    print(' ' + "0" + ' | ' + "1" + ' | ' + "2" +" | " + "3" + ' | ' + "4" + " | "+
       "5" + ' | ' + "6" + ' | ' + "7" +" | " + "8" + ' | ' + "9" + " | ")
    print('----------------------------------------')
    
    for i in range(1,10):
        print(' ' + str(i) + ' | ' + lst[i-1][0] + ' | ' + lst[i-1][1] +
              " | " + lst[i-1][2] + ' | ' + lst[i-1][3] + " | "+
              lst[i-1][4] + ' | ' + lst[i-1][5] + ' | ' + lst[i-1][6] +
              " | " + lst[i-1][7] + ' | ' + lst[i-1][8] + " | " )
        print('----------------------------------------')
    

def A_input():
    
    continueA = True
    while continueA:
    
        while True:
            positionARow = input("player A chose a row to put your chess.")
            if positionARow not in ['1','2','3','4','5','6','7','8','9']:
                print("sorry you put the chess on the wrong spot,please do it again!")
            else:
                break
        while True:
            positionACol = input("player A chose a column to put your chess.")
            if positionACol not in ['1','2','3','4','5','6','7','8','9']:
                print("sorry you put the chess on the wrong spot,please do it again!") 
            elif (lst[int(positionARow)-1][int(positionACol)-1]=="X" 
                  or lst[int(positionARow)-1][int(positionACol)-1]=="O"):
                print("sorry this place is occupied, please do it again")
                break
            else:
                lst[int(positionARow)-1][int(positionACol)-1] = "X"
                continueA = False
                break
            

def B_input():
    
    continueB = True
    while continueB:
    
        while True:
            positionBRow = input("player B chose a row to put your chess.")
            if positionBRow not in ['1','2','3','4','5','6','7','8','9']:
                print("sorry you put the chess on the wrong spot,please do it again!")  
            else:
                break
        while True:
            positionBCol = input("player B chose a column to put your chess.")
            if positionBCol not in ['1','2','3','4','5','6','7','8','9']:
                print("sorry you put the chess on the wrong spot,please do it again!")  
            elif (lst[int(positionBRow)-1][int(positionBCol)-1]=="X" 
                  or lst[int(positionBRow)-1][int(positionBCol)-1]=="O"):
                print("sorry this place is occupied, please do it again")
                break
            else:
                lst[int(positionBRow)-1][int(positionBCol)-1] = "O"
                continueB = False
                break
                
def pend_table():
    for i in lst:
        for j in range(5):
            if i[j]==i[j+1]==i[j+2]==i[j+3]==i[j+4]=="X":
                print("PlayerA win the game!")
                finish = True
                return finish
            
    for i in lst:
        for j in range(5):
            if i[j]==i[j+1]==i[j+2]==i[j+3]==i[j+4]=="O":
                print_board()
                print("PlayerB win the game!")
                finish = True
                return finish                
            
            
    for j in range(9):
        for i in range(5):
            if lst[i][j]==lst[i+1][j]==lst[i+2][j]==lst[i+3][j]==lst[i+4][j]=="X":
                print("PlayerA win the game!")
                finish = True
                return finish
    
    for j in range(9):
        for i in range(5):
            if lst[i][j]==lst[i+1][j]==lst[i+2][j]==lst[i+3][j]==lst[i+4][j]=="O":
                print_board()
                print("PlayerB win the game!")
                finish = True 
                return finish
    
    for i in range(5):
        for j in range(5):
            if lst[i][j]==lst[i+1][j+1]==lst[i+2][j+2]==lst[i+3][j+3]==lst[i+4][j+4]=="X":
                print("PlayerA win the game!")
                finish = True
                return finish
            
    for i in range(5):
        for j in range(5):
            if lst[i][j]==lst[i+1][j+1]==lst[i+2][j+2]==lst[i+3][j+3]==lst[i+4][j+4]=="O":
                print_board()
                print("PlayerB win the game!")
                finish = True
                return finish        
    
    for i in range(4,9):
        for j in range(5):
            if lst[i][j]==lst[i-1][j+1]==lst[i-2][j+2]==lst[i-3][j+3]==lst[i-4][j+4]=="X":
                print("PlayerA win the game!")
                finish = True
                return finish
            
    for i in range(4,9):
        for j in range(5):
            if lst[i][j]==lst[i-1][j+1]==lst[i-2][j+2]==lst[i-3][j+3]==lst[i-4][j+4]=="O":
                print_board()
                print("PlayerB win the game!")
                finish = True
                return finish
            
    notdraw = []        
    for i in range(9):
        for j in range(9):
            if lst[i][j]==" ":
                notdraw.append("$")
                      
    
    if not notdraw:
        print("this game is a draw")
        finish = True
        return finish
        
                
print("hi, I am the game designer Jesse, I just made a five-in-a-row game")    
continuegame = input("do you want to start a new game?'YES' or 'NO'") 

while continuegame.lower()[0] == "y":
    lst = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    finish = False
    while not finish:
        print_board()


        A_input()
        print_board()
        finish = pend_table()
        if finish == True:
            break
        B_input()
        finish = pend_table()
        if finish == True:
            break
        
    continuegame = input("do you want to start a new game?'YES' or 'NO'")
print("thanks for playing my game!")                
             

