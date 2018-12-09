'''
•Write a program in which:
–the user is asked to input a number N;
–the sum of the squared *even* numbers between 1 and N (inclusive)
is computed and output to the screen;
–the user is asked if they want to compute a new sum of squared numbers,
and if yes the program goes back to 1.
'''

continuesum = True
while continuesum:
    print("please add a number N")
    N = int(input( "what is your number?"))
    PEND = input("do you want to compute a new sum of squared even numbers? yes or no")
    if PEND.lower() == "yes":
        addnum = 0
        for i in range(N+1):
            if i % 2 == 0:
                addnum = addnum + i*i
            else:
                continue
        print("the sum of the squared even number is:", addnum)
        
        PEND2 = input("do you want to stop? yes or no")
        if PEND2.lower() == "yes":
            continuesum = False
            
        elif PEND2.lower() == "no":
            continue
            
        else:
            print("Hey dude, I dont know what are you talking about")
            continue
        
    elif PEND.lower() == "no":
        PEND2 = input("do you want to stop? yes or no")
        if PEND2.lower() == "yes":
            continuesum = False
            
        elif PEND2.lower() == "no":
            continue
        
        else:
            print("Hey dude, I dont know what are you talking about")
            continue
            
    else:
        print("Hey dude, I don't know what are you talking about")
        continue




