#Matt Callahan 2319373

#start of program
#create our empty nums list
#create a loop to display 10 random integers in the range of 1 to 25
#print them out on a line, with a space between them
#sort those same numbers on the next line.
#make a new list and slice out the first 4 elements of the nums list
#do the same, but with the last 5 elemtents of the nums list
#execute odd_even function
#end of program

#we have to import the random module to use randomized numbers
import random

def main():
    
    #our empty list
    nums = []

    #the loop that takes 10 random integers in the range of 1 to 25
    for n in range(10):
        nums.append(random.randint(1,25))
    #this prints our random integers.
    for num in nums:
        print(num, end =' ')

    #we sort the integers here
    nums.sort()
    print()

    #we print the sorted integers here   
    for num in nums:
        print(num, end = ' ')
        
    #Our modified lists that slice out starting/ending numbers and printing
    #them out as we go along
    print()
    start = nums[:4]
    print(start)

    finish = nums[-5:]
    print(finish)
    
    #here we execute the odd_even function
    odd_even(nums)

#our odd_even function that executes last in our program
def odd_even(nums):

    #odd/even counters that allow us to keep track of how many there are of each
    odds = 0
    evens = 0
 
    #this loop will run through the list and classify the integers as even or odd
    #while keeping track of the count of each
    for num in nums:
        
        #if integer is divisble by 2 with no remainder...
        if num % 2 == 0:
            evens = evens + 1
            
        #if not, it will be counted as odd
        else:
            odds = odds + 1
            
    #prrints our result and the 6th element in our new list
    print('List had',evens,'evens and',odds,'odds')
    print('The 6th element in sorted nums is',nums[5])
        
main()
