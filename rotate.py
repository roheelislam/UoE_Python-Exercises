def print_rotate(text,print_direction):
    #prining new line
    print("\n")
    print("\n")

    #It will rotate in North South direction 
    if print_direction==0: 
        print("***Rotating text in N-S***")

        #Printing each and every charater one by one
        for i in range (len(text)):
            print("     ", end="")
            #iterating on each character
            print (text[i])
        print("\n")



    #It will rotate in North East South West direction 
    elif print_direction==1: 
        print("***Rotating NE-SW***")
        #Printing each and every charater one by one
        
        for i in range (len(text)):
            #this loop is used to print spaces
            for b in range (i+1, len(text)):  
                print(" ", end="")
            print (text[i])
        print("\n")



    #It will rotate in West and East direction and print in reverse direction
    elif print_direction==2:  
        print("***Reverse Printing W-E***")
        #Double colon is used for indexing/slicing and -1 is used to completely reverse the string.
        # :: is from start to end and taking the word from backwards by -1
        text_reverse = text[::-1] 
        print (text[::-1])
        print("\n")



     #It will rotate in North West and South East direction and print in reverse direction
    elif print_direction==3: 
        print("***Reverse Rotating NW-SE***")
        # :: is from start to end and taking the word from backwards by -1
        text_reverse = text[::-1] 
        for i in range (len(text)):
            for b in range (0, i):
                print(" ", end="")
            print (text_reverse[i])
        print("\n")



     #It will rotate in North and South direction and print in reverse direction
    elif print_direction==4: 
        print("***Reverse Printing N-S***")
        # :: is from start to end and taking the word from backwards by -1
        text_reverse = text[::-1]    
        for i in range (len(text)):
            print("     ", end="")
            print(text_reverse[i])
        print("\n")



    #It will rotate in North East and South West direction and print in reverse direction
    elif print_direction==5:
        print("***Reverse Printing NE-SW***")
        # :: is from start to end and taking the word from backwards by -1
        text_reverse = text[::-1]    
        for i in range(len(text)):
            for b in range(i+1, len(text)):
                print(" ", end="")
            print(text_reverse[i])
        print("\n")



    #It will simply print the word in West & East direction
    elif print_direction==6: 
        print("***Printing W-E***")
        print(text)
        print("\n")



    #It will rotate in North West and South East direction
    elif print_direction==7: 
        print("***Printing NW-SE***")
        for i in range (len(text)):
            for b in range (0, i):
                print (" ", end="")    
            print (text[i])
        print("\n")
    #Else is printing if the values is not 0-7
    else:  
        print("***You have entered invalid value, Type Values 0-7***" + "\n" + "\n" + "\n")


#Driver code
print_rotate("rotate",0)


