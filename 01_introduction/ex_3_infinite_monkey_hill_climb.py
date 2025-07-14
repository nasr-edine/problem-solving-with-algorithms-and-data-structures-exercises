# This script improves the infinite monkey simulation using a hill climbing algorithm:
# It only changes one incorrect character at a time, keeping correct letters.

import random
import string


def score(candidate, target):
    """Return the number of matching characters between candidate and target."""
    return sum(a == b for a, b in zip(candidate, target))


def main():
    target = "methinks it is like a weasel"
    chars = string.ascii_lowercase + " "
    candidate = [random.choice(chars) for _ in range(len(target))]
    best_score = score(candidate, target)
    tries = 0

    while best_score < len(target):
        tries += 1
        # Pick a random position to mutate if it's incorrect
        indices = [i for i, (c, t) in enumerate(zip(candidate, target)) if c != t]
        if indices:
            idx = random.choice(indices)
            candidate[idx] = random.choice(chars)
        current_score = score(candidate, target)
        if current_score > best_score:
            best_score = current_score
        if tries % 1000 == 0 or best_score == len(target):
            print(f"Try {tries}: Best so far: {''.join(candidate)} ({best_score}/{len(target)})")
        if best_score == len(target):
            break


if __name__ == "__main__":
    main()