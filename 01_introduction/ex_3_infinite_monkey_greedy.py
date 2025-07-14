# This script is a greedy variant of the infinite monkey hill climbing algorithm:
# It changes all incorrect characters at once in each generation.

import random
import string


def score(candidate, target):
    """Return the number of matching characters between candidate and target."""
    return sum(a == b for a, b in zip(candidate, target))


def main():
    # target = "methinks it is like a weasel"
    target = "to be or not to be that is the question whether tis nobler in the mind"
    chars = string.ascii_lowercase + " "
    candidate = [random.choice(chars) for _ in range(len(target))]
    best_score = score(candidate, target)
    tries = 0

    while best_score < len(target):
        tries += 1
        # Change all incorrect characters at once
        candidate = [
            c if c == t else random.choice(chars)
            for c, t in zip(candidate, target)
        ]
        current_score = score(candidate, target)
        if current_score > best_score:
            best_score = current_score
        if tries % 1000 == 0 or best_score == len(target):
            print(f"Try {tries}: Best so far: {''.join(candidate)} ({best_score}/{len(target)})")
        if best_score == len(target):
            break


if __name__ == "__main__":
    main()