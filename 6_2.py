#Matt Callahan 2319373

#start of program
#we have to open up the other file as a read file.
#we have to set 2 counters to keep track of our test score and the number of our tests...
#...so that we can calculate the average at the end.
#we then create a loop to read, process, and format our results from the last document.
#We then close the text file, calculate the average, and print that result to 1 decimal place.
#end of program

def main():

    #here we open the file in read mode
    myFile = open('tests.txt','r')
    
    #we set our counters to 0 so we can tally our scores and the number of our tests.
    tests = 0
    total_scores = 0
    line = myFile.readline()
    
    #we print out this line to label our results as the headings of our table.
    print('TEST','\t','\t','SCORE')
    
    #we set up our loop that will go through the text documents results to read what they are and...
    #...tally them to our counters accordingly. The loop ends when the document ends.
    while line != '':
        n1 = line.rstrip('\n')
        scores = int(myFile.readline())
        total_scores += scores
        print(n1,'\t',scores)
        line = myFile.readline()
        tests += 1
        
    #We close the document and calculate the average.
    myFile.close()
    average_score = total_scores / tests
    
    #Here we print that average and format it to decimal place.
    print('Average is',format(average_score,'.1f'))
    


main()
