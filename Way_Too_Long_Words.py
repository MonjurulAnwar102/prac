n = int(input())  # Read the number of words

# Process each word
for _ in range(n):
    word = input()  # Read the word
    length = len(word)  # Get the length of the word
    
    # Check if the word is too long (length > 10)
    if length > 10:
        # Abbreviate the word as described
        abbreviated_word = word[0] + str(length - 2) + word[-1]
        print(abbreviated_word)
    else:
        # Word is not too long, print it as is
        print(word)
