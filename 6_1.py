#Matt Callahan 2319373

#start of program
#prompt the user to enter six test names with their respective scores
#write them to a seperate text file
#make sure each input is on its own line
#include a confirmation message at the end
#end of program

def main():

    #This myFile variable allows us to open the document to begin writing it
    myFile = open('tests.txt', 'w')

    #This informs the user what the program is intended for
    print('Entering six tests and scores')
    tests = input('Enter test name (or press Enter to quit) ')
    
    #Our while loop allows us to to prompt the user multiple times for a test
    #name and score. We then have the write expressions below so that we can
    #write onto the text file
    while tests != '':
        score = int(input('Enter % score on this test '))
        myFile.write(tests + '\n')
        myFile.write(str(score) + '\n')
        tests = input("Enter test name (or press Enter to quit) ")
            
            #this closes the file after we are done writing it
            #paired with a success message
    myFile.close()
    print('File was created successfully')
                  

                  


main()
