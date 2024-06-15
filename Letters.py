# 1. First Letter

"""
st = 'Create a list of the first letters of every word in this string'
first_letters = [word[0] for word in st.split()]
print(first_letters)
"""

# 2. Start with ...

"""
st = 'Print only the words that start with s in this sentence'
# Longer solution:
for word in st.split():
    if word[0].lower() == 's':
        print(word)
"""


# 3. Print words with even number of letters

"""
st = 'Print every word in this sentence that has an even number of letters'
words = st.split()
for word in words:
    if len(word) % 2 == 0:
        print(f' {word} has even number of letters.')
"""

# 4. Takes a two-word string and returns True if both words begin with same letter

"""
ANIMAL CRACKERS: 
animal_crackers('Levelheaded Llama') --> True
animal_crackers('Crazy Kangaroo') --> False
"""
def animal_crackers(text):
    # Split the string into two words
    text1, text2 = text.split()
    # Check if both words start with the same letter
    if text1[0].lower() == text2[0].lower():
        return True
    else:
        return False

# Check 1
print (animal_crackers('Levelheaded Llama'))
# Check 2
print(animal_crackers('Crazy Kangaroo'))