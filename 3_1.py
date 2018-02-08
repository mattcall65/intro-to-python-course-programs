#Matt Callahan 2319373
#start of program
#add bracket style if/else statements to guide user input to the correct output
#use boolean expressions to clearly define different age groups and make sure
#they utilize "equal to" operators minimize error
#end of program

def main ():

    #input reqired by user and the code behind it
    age = int(input("Enter your age as a whole number here --> "))

    #our if/else tree with corresponding boolean expressions and strings
    if age >= 55:
        print("Based on your inputed age, you are considered a senior!")
    elif age >= 20:
        print("Based on your inputed age, you are considered an adult!")
    elif age >= 13:
        print("Based on your inputed age, your are considered a teenager!")
    elif age <= 12:
        print("Based on your inputed age, you are considered a minor!")
    
main()
