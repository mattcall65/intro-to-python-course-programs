#Matt Callahan 2319373

#start of program
#prompt user for an integer under 20
#produce a second function that will produce as many random numbers as the original integer
#return total to main for printing
#create a corrective message if the original input is over 20
#end of program

import random



def main():

    #original user input 20 or under
    num1 = int(input('How many random integers (max 20)? ', ))

    
    
    #Our if statement that kicks everything off. It starts off by running
    #our second function

    #we print our returned total variable below
    if num1 <= 20:
        
        total = randnums(num1)
        print()
        print('Integers total is...',total)
        
    #The corrective/error message if the original input is over 20
    else:
         print('Bad input. Maximum input is 20')
         
#Our second function. Since we have random imported, we can use the random
#function calls to get as many random numbers as the original integer

#we reassign the total variable to reflect the actual total of the random numbers.
#we print the individual integers here, and return the total to main for printing.         
def randnums(num1):
    total = 0
    for count in range(num1):
        x = random.randint(1,9)
        total = total + x
        print(x,end = " ")
    return total
        
        
        
        
        
    

main()
