# 1. Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
"""def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False
# Check1
print(has_33([1, 3, 3]))
# Check2
print(has_33([1, 3, 1, 3]))
# Check3
print(has_33([3, 1, 3]))"""

# 2. Return a string where for every character in the original there are three characters.
"""def paper_doll(text):
    tripled_string = ''
    for char in text:
        tripled_string += char * 3
    return tripled_string
# Check1
print(paper_doll('Hello'))
# Check2
print(paper_doll('Mississippi'))"""

# 3. Return the sum of the numbers in the array,
# except ignore sections of numbers starting with a 6 and extending to the next 9
# (every 6 will be followed by at least one 9). Return 0 for no numbers.

"""
summer_69([1, 3, 5]) --> 9
summer_69([4, 5, 6, 7, 8, 9]) --> 9
summer_69([2, 1, 6, 9, 11]) --> 14
"""
def summer_69(arr):
    ignore_section = False
    total_sum = 0

    for num in arr:
        if num == 6:
            ignore_section = True
        elif num == 9 and ignore_section:
            ignore_section = False
        elif not ignore_section:
            total_sum += num

    return total_sum

# Check1
print(summer_69([1, 3, 5]))
# Check2
print(summer_69([4, 5, 6, 7, 8, 9]))
# Check3
print(summer_69([2, 1, 6, 9, 11]))