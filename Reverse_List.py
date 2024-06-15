# Return a sentence with the words reversed

"""
master_yoda('I am home') --> 'home am I'
master_yoda('We are ready') --> 'ready are We'
"""

def master_yoda(text):
    print(f'Original text: {text}')
    # Split the sentence into words
    words = text.split()
    print(f'Split words organized in a list are: {words}')
    # Reverse the list of words
    rev = words[::-1]
    print(f'Reversed list: {rev}')
    # Join the reversed words to form a new sentence
    master = ' '.join(rev)
    print(f'Master Yoda says: {master}')
    return master


# Check1
print(master_yoda('I am home'))
# Check2
print(master_yoda('We are ready'))