# A leap year:
#
# Every year that is divisible by 4 with no remainder
# % 4 = 0 = Leap
# Except every year that is evenly divisible by 100 with no remainder
# % 100 = o = NO Leap
# Unless the year is also divisible by 400 with no remainder
# % 100 = 0 = NO Leap, but if also % 400 = 0 then Leap
year = int(input('Enter your year to check: \n'))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('Leap year')
        else:
            print('Not leap year')
    else:
        print('Leap year')
else:
    print('Not leap year')

