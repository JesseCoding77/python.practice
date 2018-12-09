'''
•You are asked to read 1000 integers from a file,
which is provided to you (integers.txt).
The integers have to be read into a list.
I am aware that I have not covered files yet
(I’ll discuss them today and on Thursday),
and because of this I provide a brief discussion about writing and reading
simple files. The deadline for the assignment is also longer than usual
to allow you to digest the material.
•Within your program you need to create a function insertion_sort(int_list)
that takes as argument a list of integers and sorts it in ascending order
(smallest first) using the Insertion Sort algorithm (see below).
•After reading the integers from the file into a list,
your main program should call the insertion_sort function,
then it should:
1) print the now sorted list onto the screen;
2) write the sorted list onto a file (sorted_integers.txt).
'''
def insertion_sort(filename = "integers.txt" ):

    def list_sort(int_list):
            

        for i in range(1,len(int_list)):    

           current = int_list[i]    

           while i>0 and int_list[i-1]>current:
                int_list[i] = int_list[i-1]
                i = i-1
                int_list[i] = current    

        return int_list    

    #open the integers.text file and print the list
            
    with open(filename,mode ="r") as f:
        text_line = f.readlines()
        new_line =[]
        for j in text_line:
            j = int(j[:-1])
            new_line.append(j)
        list_sort(new_line)
        print(new_line)    

    #wirte the list in a new text file as sorted_integers.txt
        
    with open("sorted_integers.txt",mode ="w") as fw:    
        for i in new_line:
            fw.write(str(i)+"\n")    
    

        


