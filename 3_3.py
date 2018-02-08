#Matt Callahan 2319373

#start of program
#we will have to structure this quiz into another if/else tree
#we will also have to prompt the user 3 times for an answer and create
#a corrrect/incorrect (if/else) response
#additionaly, we will have to use expressions to keep score of the quiz and
#display the result at the end.
#end of program

def main():

    #we have to start at 0 to count/grade the score
    score = 0

    #first input for first question
    q1 = input("What color is the sun? ")
    
    #if correct, youll get this response
    if q1 == "yellow":
        print('You are correct!', 'Your current score is...')
        score += 1
    #if Q1 is wrong, it will print this. notice we use an expression in the if
    #statement to ring the score up 1 (for 1 correct answer)
    else:
            print('Sorry, the correct answer is yellow')


    #we will repeat the process for question 2 and 3

    q2 = input('Dog is to land, as fish is to...? ')

    if q2 == "water":
        print('You are correct!', 'Your current score is...',)
        score += 1
    else:
        print('Sorry, the correct answer is water')

    q3 = int(input('What is the smallest positive integer (enter as a number)'))

    if q3 == 1:
        print('You are correct', 'Your current score is...')
        score += 1
        print(score)

        #at the very end, we will print the score, which is accrued 1 point
        #per correct answer (via the if statements)
        
    else:
        print('Sorry, the correct answer is 1')
    print('Your final score is',score)
main()
