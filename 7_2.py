#Matt Callahan 2319373

#start of program
#end of program

#Matt Callahan 2319373

#start of program
#end of program

def main():

    print('Celebreties known by one name:')
    
    #We put 4 celeberity names into the list and set counters to move...
    #through loops and if/else statements
    celeb = ['Brady','Manning','Lebron','Durant']
    count2 = 0
    count = 0
    for n in celeb:
        print(celeb,end=' ')
        count += 1
        print()

        if count == 1:
            count2 = 0
            for x in celeb:
                
                #well choose ironman
                add_celeb = (input('Enter another one name celebrity ', ))
                celeb.append(add_celeb)
                
                #lets choose spiderman
                add_celeb2 = (input('Enter another one name celebrity ', ))
                celeb.append(add_celeb2)

                #lets choose superman
                add_celeb3 = (input('Enter another one name celebrity ', ))
                celeb.append(add_celeb3)

                count2 += 1
                if count2 == 1:

                    second_function(celeb)

def second_function(celeb):
    celeb.sort()
    celeb.reverse()
    print(celeb,'\n')
    
                    

main()
