# Exercise 1 to 10
#numbers = [1,2,3,4,5,6,7,8,9,10]
#for number in numbers:
    #print number

#Exercise n to m
#numbers = range(11)
#user_input_start = int(raw_input('Where do we start counting from? '))
#user_input_end = int(raw_input('Where do we stop counting? '))

#for number in numbers[user_input_start:user_input_end + 1]:
    #print number

#Exercise Odd numbers
#for i in range(1,11,2):
    #print i

#numbers = range(11)
#for number in numbers:
    #if number%2 != 0:
        #print number

#Exercise Print a Square
#square_range = range(5)
#for numbers in square_range:
#    print '#####'

#Exercise Print a Square 2
#HARD WAY - trying to use lists and arrays
#square_range_2 = range(int(raw_input('How big is the square?')))
#row = []
#for numbers in square_range_2:
#    row.append('#')
#print row[0:]

#EASY WAY - just multiply
#get the width of the box.

width = int(raw_input('How wide?')) #get the width of the box.
height = int(raw_input('how high?')) #get the height of the box.
for lines in range(height): #iterate lines height times.
    if lines == 0: #1st line of the box, begining of range(height)
        print width * '#' #multiply # by the width
    elif lines == height - 1:
        print width * '#'
    else:
        print '#' + ' ' * (width-2) + "#"
