# string_fun.py
# Practicing string operations

# user input any word
word = input("Enter a word: ")

# --- String Length ---
print(f"The length of the word '{word}' is {len(word)} characters.")

# print the word in all uppercase
print(f"The word in uppercase: {word.upper()}")

# print the word repeated 3 times on the same line
print(f"The word repeated 3 times: {word * 3}")

#print the word repeated 3 times, each on a new line
print(f"The word repeated 3 times on new lines:\n{word}\n{word}\n{word}")
