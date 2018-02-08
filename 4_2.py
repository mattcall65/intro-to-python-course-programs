#Matt Callahan 2319373

#start of program
#prompt user for cars sold to start
#then begin a while loop to ask the salling price of car for however many there is
#do this through day 5 and print result
#end of program

def main():

    #we set our vairables so the logic of the problem can be executabale
    #via boolean expressions
    total = 0
    sales = 0
    num1 = 0
    num2 = 0
    num3 = 1
    day = 2
    carnum = 0
    gtotal = sales + num2
    
    #our first input
    num1 = int(input('How many cars were sold on day 1 '))
    total += num1

    #we begin our while loops so that for each car, the user is prompted for
    #the selling price.

    #we then add variable together acccordingly to keep a "tally", so to speak
    while num3 <= num1:
        num2 = float(input('Selling price of car '+ (str)(num3)+'?'))
        sales += num2
        num3 += 1
    while num1 != 0:
        num1 = int(input('How many cars were sold on day ' + (str)(day)))
        total += num1
        sales += num2
        day += 1
        num3 = 1
        while num3 <= num1:
            num2 = float(input('Selling price of car '+ (str)(num3)+'?'))
            num3 += 1

    #Finally, we use this expression to output the number of cars and the final price
            
        if day > 5:

            print( 'You sold',sales,'cars for total sales of', gtotal)
main()
