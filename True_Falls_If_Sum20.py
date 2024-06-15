# 1. Returns True if the sum of the integers is 20 or if one of the integers is 20. If not, returns False

"""
makes_twenty(20,10) --> True
makes_twenty(12,8) --> True
makes_twenty(2,3) --> False

def makes_twenty(n1,n2):
    if n1 + n2 == 20:
        return True
    elif n1 == 20:
        return True
    elif n2 == 20:
        return True
    else:
        return False
# Check1
print (makes_twenty(20,10))
# Check2
print(makes_twenty(2,3))
# Check3
print (makes_twenty(15,5))
"""
# Comprehension:

def makes_twenty(n1, n2):
    return n1 == 20 or n2 == 20 or n1 + n2 == 20