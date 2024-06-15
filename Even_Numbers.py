# 1. Print even numbers from given range


"""Most basic solution

for x in range(0,11,2):
    print(x)
"""

#More advanced solution:

nums = [i for i in range(0,11) if i % 2 == 0]
print(nums)

"""
It is a comprehension for

for i in range(0,11):
    if i % 2 == 0:
        print(i)
"""


"""
            ***************

*** Similar problem: numbers divided by 3 ***

nums = [i for i in range(1,51) if i % 3 == 0]
print(nums)

"""