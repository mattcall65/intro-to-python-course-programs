#Matt Callahan 2319373

#start of program
#create an input expression that will prompt user for an integer that satisfies the requirements
#create an if else tree that will bounce the input to different outputs depending on the input given
#provide informative outputs for every possible answer
#end of program

def main():

    #input expression that starts our if/else tree
    num1 = int(input("Enter an even multiple of 13 or 19 --> "))
    
     #if/else that determines if int is divisible evenly by 13 or 19
     #and checks if its even
    if (num1 % 13 == 0 or num1 % 19 == 0) and num1 % 2 == 0:

        #if it is divisble by 13, it will output this
        if num1%13==0:
            print('Good', num1, 'is 13*'+ str(num1/13))

        #if not, it will output this
        else:
            print('Good', num1, 'is 19*' + str(num1/19))
            
    #if input doesn't fit into above parameters, it will hit this next
    #printing the statement if it does
    elif num1 % 13 != 0 and num1 % 19 != 0 and num1 % 2 == 0:
        print('The number entered is even, but not divisble by 13 or 19')
        
    #Same idea with these two bottom lines of code. If the input doesn't satisfy
    #the boolean expressions, it will keep bouncing down to next if/else    
    elif (num1 % 13 == 0 or num1 % 19 == 0) and num1 % 2 != 0:
        print("No. Multiple okay but not EVEN")

        #until eventually you'll end up with this if it falls all the way through
    else:
        print("No. Not EVEN and misses muultiple requiremment")
    

        
main()  
