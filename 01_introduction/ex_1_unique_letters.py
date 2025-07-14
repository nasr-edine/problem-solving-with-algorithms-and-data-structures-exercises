# This script creates a list of unique letters from a list of words (no duplicates).

word_list = ['cat', 'dog', 'rabbit']
letter_list = []
for a_word in word_list:
    for a_letter in a_word:
        if a_letter not in letter_list:  # Only add if not already in the list
            letter_list.append(a_letter)
print(letter_list)  # Output: ['c', 'a', 't', 'd', 'o', 'g', 'r', 'b', 'i']