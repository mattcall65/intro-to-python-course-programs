#Matt Callahan 2319373

#start of program
#create 4 functions that perform the basic operations of
# +,-,%, and * to two numbers originally inputted from our main function on 5_3
#the first two will print to one decimal place while the last 2...
#...will return the result back to main in 5_3 to print to 2 decimal places
#end of program
    

#function for our total. We will print inside this function, rather than
#back in main
def total(n1,n2):
    total = n1 + n2
    print('The total is ',total)
    
#function for the difference. We will print in main

#we are required to return the difference as a positive value no matter the actual outcome.
#In algebra, we would see an instance of this in the form of absolute value bars around a number (i.e. |-5| = 5)
#As it turns out, we're able to do this in python,
#by using its built in 'abs' ability. We can apply it in a similar fashion as we would see in an algebra problem,
#as seen below    

def difference(n1,n2):
    difference = n2 - n1
    print('The difference is ', abs(difference))
    
    
#function for the product. We will return the result back to main and print there
def product(n1,n2):
    product = n1 * n2
    return n1 * n2

#function for the quotient. We will return and print in main
def quotient(n1,n2):
    quotient = n1 / n2
    return n1 / n2

    

