#Matt Callahan 2319373

#start of program
#ask user to input amount in US dollars
#create a function that does the conversion formula and assigns it to a variable
#print out the new amount in Euros (including the format of decimals, and commas

def main ():

    #basic math solving to get out euro amount
    userAmount = float(input("Enter amount in US dollars "))
    convRateAmt = userAmount / 1.152

    #printing our desired result on screen
    print("Amount in Euros is... ",format(convRateAmt,',.3f'),sep='')

main()
    
    
