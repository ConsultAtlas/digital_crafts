#name = raw_input('What is your name? ')
#print('Your name is %s.' % name)
#print(('Here is your name %s in all caps.' % name).upper())
#name_count = len(name)
#print('Your name has %d in it.' % name_count )

#sport = raw_input('What sport do you like to play?')
#week_day = raw_input('What day of the week to you practice?')
#print('%s likes to play %s on %s\'s.') % (name, sport, week_day)

#day_of_the_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
#user_choice = int(raw_input('I am thinking of a day 0-6. What do you think it is?'))
#if user_choice == 0 or user_choice == 6:
#    print 'Sleep in.'
#else:
#    print 'Go to work.'

#user_choice = int(raw_input('Temperature in C is? '))
#fahrenheit = (user_choice * 1.82) + 32
#print('That is %d degrees.' % fahrenheit)

total = int(raw_input('What was your total bill? '))
service = raw_input('Was your service good, fair, or bad? ')
party_size = int(raw_input('What is the size of your party? '))
tip = 1
if service == 'good':
    tip = .20
if service == 'fair':
    tip = .15
if service == 'bad':
    tip = .10
calculated_tip = total * tip
total_w_tip = total + calculated_tip
print('You should leave $%d as a tip making your total bill $%d.' % (calculated_tip, total_w_tip))
bill_per_party_member = float(total_w_tip / party_size)
print('You should should split the bill %d ways and each person should pay $%d' % (party_size, bill_per_party_member))
