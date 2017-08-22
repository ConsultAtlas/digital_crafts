# Exercise 1 to 10
#numbers = range(11)
#for number in numbers:
    #print number

#numbers = range(11)
#def printOneToTen():
#    for number in numbers:
#        print number

#printOneToTen()

#Exercise n to m
#numbers = range(11)
#user_input_start = int(raw_input('Where do we start counting from? '))
#user_input_end = int(raw_input('Where do we stop counting? '))

#for number in numbers[user_input_start:user_input_end + 1]:
#    print number

#def printRangeYouPick(start, end):
#    for number in range(start, end):
#        print number


#user_input_start = int(raw_input('Where do we start counting from? '))
#user_input_end = int(raw_input('Where do we stop counting? '))

#printRangeYouPick(user_input_start, user_input_end)

#numbers = range(11)
#for number in numbers:
    #if number%2 != 0:
        #print number

#def printOddNums(nums):
#    for number in range(nums):
#        if number%2 != 0:
#            print number
#user_input_odds = int(raw_input('What is the length of the range you want? '))

#printOddNums(user_input_odds)

#width = int(raw_input('How wide?')) #get the width of the box.
#height = int(raw_input('how high?')) #get the height of the box.
#for lines in range(height): #iterate lines height times.
#    if lines == 0: #1st line of the box, begining of range(height)
#        print width * '#' #multiply # by the width
#    elif lines == height - 1:
#        print width * '#'
#    else:
#        print '#' + ' ' * (width-2) + "#"

#def printASquare(width, height):
#    for lines in range(height): #iterate lines height times.
#        if lines == 0: #1st line of the box, begining of range(height)
#            print width * '#' #multiply # by the width
#        elif lines == height - 1:
#            print width * '#'
#        else:
#            print '#' + ' ' * (width-2) + "#"

#user_width = int(raw_input('How wide?')) #get the width of the box.
#user_height = int(raw_input('how high?')) #get the height of the box.

#printASquare(user_width, user_height)

#def printNSquare(n):
#    for lines in range(n):
#        print '#' * n

#user_input_n = int(raw_input('How big you want it? '))

#printNSquare(user_input_n)

#width = int(raw_input('Width? '))
#height = int(raw_input('Height? '))

# draw the top border
#print '*' * width

# draw the middle
#num_spaces = width - 2
#spaces = ' ' * num_spaces
#for i in range(height - 2):
#    print '*' + spaces + '*'

# draw the bottom border
#print '*' * width

#def drawABox(width, height):
    # draw the top border
#    print '*' * width

    # draw the middle
#    num_spaces = width - 2
#    spaces = ' ' * num_spaces
#    for i in range(height - 2):
#        print '*' + spaces + '*'

    # draw the bottom border
#    print '*' * width

#width = int(raw_input('Width? '))
#height = int(raw_input('Height? '))

#drawABox(width, height)

#xr = 10

#for x in xrange (0,xr):
#    spaces = xr - x - 1
#    stars = x * 2 + 1
#    for y in xrange (0, spaces):
#         print(" ")
#    for z in xrange(0, stars):
#        print("*")
#    print ""

#xylo = range(10)
#yolo = range(10)

#for x in range(10):
#    number = (x * range(x))
#    print number

#for x in xylo:

#    print('%d X %d') % (x, xylo)

#for x in range(1, 10):
#    for y in range(1, 10):
#        z = x * y
#        print('%d X %d = %d' % (x, y, z))

#def printYourTimes():
#    for x in range(t):
#        for y in range(p):
#            z = x * y
#            print('%d X %d = %d' % (x, y, z))

#t = (int(raw_input('How long is your table? '))+1)
#p = (int(raw_input('How many times do you want? '))+1)

#printYourTimes()

#user_string = raw_input('Give me a string! ')
#print user_string
#how_long = len(user_string)
#print how_long

# Exercise Banner!
#def drawABanner(width):
     #draw the top border
#    print '*' * width

     #draw the middle
#    num_spaces = width - 2
#    spaces = ' ' * num_spaces
    #for i in range(height - 2):
    #    print '*' + spaces + '*'
#    print '*' + ' ' + user_banner_string + ' ' + '*'


    # draw the bottom border
#    print '*' * width
#user_banner_string = raw_input('Give me a string! ')
#width = (len(user_banner_string)+4)
#height = int(raw_input('Height? '))

#drawABanner(width)

#def create_pyramid(rows):
#    for i in range(rows):
#        print((' ' * ( rows- i - 1 ) + '*' * ( 2 * i + 1)))
#rows = int(raw_input('How many rows? '))
#create_pyramid(rows)

#rows = int(raw_input('How many rows?'))
#for i in range(rows):
#    print((' '* (rows - i - 1) + '*' * (2 * i + 1)))

#string = 'this is a string uppercase.'
#string2 = 'this is a string capitalized.'
#print(string.upper())
#print(string2.capitalize())

# Leet Speak Exercise

#word = raw_input('The word: ').upper()

# A => 4
# E => 3
# G => 6
# I => 1
# O => 0
# S => 5
# T => 7

#word = word.replace('A', '4')
#word = word.replace('E', '3')
#word = word.replace('G', '6')
#word = word.replace('I', '1')
#word = word.replace('O', '0')
#word = word.replace('S', '5')
#word = word.replace('T', '7')

#print word

#leet_word = raw_input('what word would you like to translate? ').upper()

# A => 9
# E => 3
# I => 6
# O => 4
# U => 1
# S => 2
# T => 7

#leet_word = leet_word.replace( 'A' , '9' )
#leet_word = leet_word.replace( 'E' , '3' )
#leet_word = leet_word.replace( 'I' , '6' )
#leet_word = leet_word.replace( 'O' , '4' )
#leet_word = leet_word.replace( 'U' , '1' )
#leet_word = leet_word.replace( 'S' , '2' )
#leet_word = leet_word.replace( 'T' , '7' )

#print leet_word

#def makeYourWordsLeet():
#    leet_word = leet_word.replace( 'A' , '9' )
#    leet_word = leet_word.replace( 'E' , '3' )
#    leet_word = leet_word.replace( 'I' , '6' )
#    leet_word = leet_word.replace( 'O' , '4' )
#    leet_word = leet_word.replace( 'U' , '1' )
#    leet_word = leet_word.replace( 'S' , '2' )
#    leet_word = leet_word.replace( 'T' , '7' )

#    print leet_word

#leet_word = raw_input('what word would you like to translate? ').upper()

#makeYourWordsLeet()

#long_word = raw_input('What is the word? ').upper()

#def longVowels():
#    long_word = raw_input('What is the word? ')
#    long_word = long_word.replace('oo', 'ooooo')
#    long_word = long_word.replace('ee', 'eeeee')
#    print(long_word)

#Slong_word = raw_input('What is the word? ').upper()

#longVowels()

# Ceaser Cipher Exercise

#secret = "Lbh zhfg hayrnea, jung lbh unir yrnearq."
# secret = "hello"
#offset = 13
#alphabet = 'abcdefghijklmnopqrstuvwxyz'
#result = ''

def caeserBringsYou():
    secret = "Lbh zhfg hayrnea, jung lbh unir yrnearq."
    offset = 13
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for char in secret:
        ascii_code = ord(char)
        is_uppercase = ascii_code >= 65 and ascii_code <= 90
        char = char.lower()
        if char not in alphabet:
            new_char = char
        else:
            idx = alphabet.find(char)
            new_idx = idx + offset
            if new_idx > 25:
                new_idx = new_idx - 26
            new_char = alphabet[new_idx]
            if is_uppercase:
                new_char = new_char.upper()
        result += new_char

    print result

caeserBringsYou()
