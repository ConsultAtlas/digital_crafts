#day = int(raw_input('Day(0-6)?'))
#week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
#print(week[day])

day = int(raw_input('Day(0-6)?'))
if day == 0 or day == 6:
    print 'Sleep in.'
else:
    print "Go to work."
