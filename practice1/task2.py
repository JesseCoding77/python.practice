'''
•Write a program that converts €, $ and £ into one another.
•The program should ask the user to choose the currency to convert from,
and the currency to convert into, then should ask for the amount to convert,
and return the result of the conversion onto the screen.
'''

while True:
    
    From_Currency = input("choose the currency to convert from: you can choose '€' '£' '$'")
    Into_Currency = input("currency to convert into: you can choose '€' '£' '$'")
    Amount = float(input("chose the amount of currency to convert from"))
    
    if From_Currency == "€" and Into_Currency == "$":
      print('the amount of currency converted into is')
      print(Amount*1.15)
    elif From_Currency == "€"and Into_Currency == "£":
      print('the amount of currency converted into is')
      print(Amount*0.89)
    elif From_Currency == "£" and Into_Currency == "€":
      print('the amount of currency converted into is')
      print(Amount*1.13)
    elif From_Currency == "£"and Into_Currency == "$":
      print('the amount of currency converted into is')
      print(Amount*1.30)
    elif From_Currency == "$"and Into_Currency == "€":
      print('the amount of currency converted into is')
      print(Amount*0.87)
    elif From_Currency == "$"and Into_Currency == "£":
      print('the amount of currency converted into is')
      print(Amount*0.77)
    else:
      print("please do it again")
   
    Continue = input("\n\nDo you want to continue?.'yes'or'no'")
    if Continue =="yes":
        continue
    else:
        break 
  




