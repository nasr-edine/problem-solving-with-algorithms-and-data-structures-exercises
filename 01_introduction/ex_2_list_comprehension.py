# This script uses a list comprehension to flatten a list of words into a list of letters,
# ensuring each letter appears only once (removes duplicates).

word_list = ['cat', 'dog', 'rabbit']
seen = set()  # Track seen letters
# Add letter only if it hasn't been seen before
letter_list = [a_letter for a_word in word_list for a_letter in a_word if not (a_letter in seen or seen.add(a_letter))]
print(letter_list)  # Output: ['c', 'a', 't', 'd', 'o', 'g', 'r', 'b', 'i']