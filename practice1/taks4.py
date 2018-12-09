'''
•Write a function that checks if a string is a palindrome.
A palindrome is a string (can be a single word or a phrase)
that reads the same way backward as it does forward
(not considering capital letters), e.g.: Malayalam.
•Now write a program that asks the user to input a word,
using the function you built checks whether the word is a palindrome
and tells the user so.
•The program should carry on asking the user for words
and checking if they are palindromes until the user wants to stop.
'''
def check_palindrome(word):
    
    continue_check = True
    while continue_check:
        print("the result of this word is a")
        print(word.lower() == word[::-1].lower(),"palindrom")
        pend = input("do you want to check a new word?'yes'or'no'")
        if pend.lower() == 'yes':
            word = input("what is your new word")
        else:
            continue_check = False
    input("press any key to stop")


# an alternative solution:

def check_palindrome2(word):

    continue_check2 = True
    while continue_check2:
          word_old = word
          word_new = ""
          while word:
              word_new += word[-1]
              word = word[:len(word)-1]
          if word_old.lower() == word_new.lower():
              print("it is a palindrome word")
          else:
              print("it is not a palindrome word")

          pend1 = input("do you want to check a new word?'yes'or'no'")      
          if pend1.lower() == "yes":
            word = input("what is your new word")
          else:
            continue_check2 = False

    input("press any key to stop")

# an another solution:

continue_count = False

while continue_count:
    
    def check_palindrome3(word):
         print(word.lower() == word[::-1].lower(),"palindrom")

    pend2 = input("do you want to check a new word?'yes'or'no'")      
          if pend2.lower() == "yes":
              continue
          else:
              continue_count = False

            

              

    

    

    



