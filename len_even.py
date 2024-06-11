st = 'Print every word in this sentence that has an even number of letters'
words = st.split()
for word in words:
    if len(word) % 2 == 0:
        print(f' {word} has even number of letters.')