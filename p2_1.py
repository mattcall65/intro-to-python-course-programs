#Matt Callahan 2319373

#start of program
#prompt user for weekly hours worked and hourly pay rate
#create a variable that  multiplys both together
#print out the result that gives us the answer with the 2 decimal places
#and no space between the number and dollar sign.

def main ():
    
    #math/input functions that are the basis of our program
    hours_worked = float(input("Enter hours worked here"))
    hourly_rate = float(input ("Enter hourly rate here"))
    weekly_pay = hours_worked * hourly_rate

    #how we show result on screen with a dollar sign and 2 decimal places
    print ("Your weekly pay is... $" ,format(weekly_pay,'.2f'),sep='')
    
    
main()
