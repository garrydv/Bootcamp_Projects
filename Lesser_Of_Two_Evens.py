# 1. Returns the lesser of two given numbers if both numbers are even,
# but returns the greater if one or both numbers are odd


"""
lesser_of_two_evens(2,4) --> 2
lesser_of_two_evens(2,5) --> 5
"""
def lesser_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 == 0:  # both numbers are even
        return min(a, b)
    else:  # at least one number is odd
        return max(a, b)

# Testing function:
print(lesser_of_two_evens(2,5))