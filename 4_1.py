#Matt Callahan 2319373

#start of program
#use a while loop to display integers in increments of 25 up to 200 starting from 0
#do the same with a for loop, but descending from 200 by 25
#make sure both are printed on seperate lines and seperated by a single space
#end of program

def main():

    #we use num as a variable so we can effectively use our boolean expressions
    num = 0

    #since ive specified num will be incrememnted by 25 for every cycle,
    #the while loop will run until it hits 200 as instructed by the boolean expression
    
    while num <= 200:
        print(num,end = " ")
        num += 25
    print()

    #we have a simlar situation here, but the for loop allow us to be more specific.
    #the first 2 numbers in range specify our end and starting pt, while the third
    #indicates by what increment
    for num in range(200,-1,-25):
        
        print(num, end = ' ')

        #end =  is what allows us to seperate by a single space

main()


    

