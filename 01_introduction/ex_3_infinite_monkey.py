# This script simulates the infinite monkey theorem:
# It generates random strings and checks if they match the target sentence.

import random
import string

def generate_random_string(length):
    """Generate a random string of given length from lowercase letters and space."""
    chars = string.ascii_lowercase + " "
    return ''.join(random.choice(chars) for _ in range(length))

def score(random_str, target):
    """Count the number of characters that match the target."""
    return sum(a == b for a, b in zip(random_str, target))

def main():
    target = "methinks it is like a weasel"
    best_score = 0
    best_string = ""
    tries = 0

    while best_score < len(target):
        tries += 1
        attempt = generate_random_string(len(target))
        attempt_score = score(attempt, target)
        if attempt_score > best_score:
            best_score = attempt_score
            best_string = attempt
        if tries % 1000 == 0:
            print(f"Try {tries}: Best so far: '{best_string}' ({best_score}/{len(target)})")

if __name__ == "__main__":
    main()