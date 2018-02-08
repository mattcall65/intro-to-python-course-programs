#Matt Callahan 2319373

#start of program
#enter value for kennys estate to a variable
#begin doing mathematical arithmetic to find everyone else slice of the pie
#check ending values with example to ensure the arithmitic code is accurate
#print values with stings of words to give context. Make sure they are in
#currency format

def main ():

    #here I constructed the expressions to correctly figure out the values
    #of everyones share of the estate
    kenny_estate = float(input("Enter value of Kenny's estate here --> "))
    stan_estate = kenny_estate / 2
    kyle_estate = stan_estate / 1/3 * 2
    intStep = stan_estate - kyle_estate
    butterWendy_estate = intStep / 2
    
    #all I did here was print the values with a string of words to go along
    #with them. All in currency format of course.
    print("Stan gets... $",format(stan_estate,'.2f')," of Kenny's estate",sep='')
    print("Kyle gets... $",format(kyle_estate,'.2f')," of Kenny's estate",sep='')
    print("Butters and Wendy both get... $",format(butterWendy_estate,'.2f')," of Kenny's estate",sep='')

main()
