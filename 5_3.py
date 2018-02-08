#Matt Callahan 2319373

#start of program
#import the arithmetic file
#prompt the user for 2 number inputs
#call the first 2 functions from the arithmetic file
#make sure the product and quotient are printed here in the main function
#end of program

#this imports our arithmetic file/module
import arithmetic

#our main function
def main():

    #the user inputs that we require the user
    n1 = float(input('Enter a number ', ))
    n2= float(input('Enter another number ', ))
    
#these fetch the functions from the arithmetic file and exectues them
    arithmetic.total(n1,n2)
    arithmetic.difference(n1,n2)

    #these next 2 take advantage of the return utilized in the arithmetic file.
    #since, the prouct and quotient are already stored, we just set our vairables,..
    #..and print the answer out to 2 decimal places.
    AP = arithmetic.product(n1,n2)
    print('The product is',format(AP,'.2f'))

    AQ = arithmetic.quotient(n1,n2)
    print('The quotient is',format(AQ,'.2f'))

main()
