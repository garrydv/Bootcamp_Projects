st = 'Print only the words that start with s in this sentence'
# Longer solution:
for word in st.split():
    if word[0].lower() == 's':
        print(word)
