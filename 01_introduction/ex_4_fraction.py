def gcd(m, n):
    """Compute the greatest common divisor of m and n."""
    while n != 0:
        (m, n) = (n, m % n)
    return m

class Fraction:
    def __init__(self, top, bottom):
        """Initialize a fraction with numerator and denominator."""
        common = gcd(top, bottom)
        self.num = top // common
        self.den = bottom // common

    def __str__(self):
        """Return string representation of the fraction."""
        return f"{self.num}/{self.den}"

    def show(self):
        """Print the fraction."""
        print(self)

    def __add__(self, other_fraction):
        """Add two fractions and return the result as a new Fraction."""
        new_num = self.num * other_fraction.den + other_fraction.num * self.den
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)

    def __eq__(self, other):
        """Check if two fractions are equal."""
        return self.num * other.den == other.num * self.den

    def __mul__(self, other):
        """Multiply two fractions and return the result as a new Fraction."""
        new_num = self.num * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        """Subtract other fraction from self and return the result as a new Fraction."""
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __truediv__(self, other):
        """Divide self by other fraction and return the result as a new Fraction."""
        if other.num == 0:
            raise ZeroDivisionError("Cannot divide by a fraction with numerator 0.")
        new_num = self.num * other.den
        new_den = self.den * other.num
        return Fraction(new_num, new_den)


    def __lt__(self, other):
        """Check if self is less than other fraction."""
        return self.num * other.den < other.num * self.den

    def __gt__(self, other):
        """Check if self is greater than other fraction."""
        return self.num * other.den > other.num * self.den

    def get_num(self):
        """Return the numerator of the fraction."""
        return self.num

    def get_den(self):
        """Return the denominator of the fraction."""
        return self.den

if __name__ == "__main__":
    # Create some fractions
    a = Fraction(1, 2)
    b = Fraction(3, 4)
    c = Fraction(2, 4)
    d = Fraction(5, 8)

    # Addition
    print(f"{a} + {b} = {a + b}")  # 1/2 + 3/4 = 5/4
    print(f"{a} + {c} = {a + c}")  # 1/2 + 2/4 = 1/1

    # Subtraction
    print(f"{b} - {a} = {b - a}")  # 3/4 - 1/2 = 1/4

    # Multiplication
    print(f"{a} * {b} = {a * b}")  # 1/2 * 3/4 = 3/8

    # Division
    print(f"{a} / {b} = {a / b}")  # 1/2 / 3/4 = 2/3

    # Equality
    print(f"{a} == {c} -> {a == c}")  # 1/2 == 2/4 -> True
    print(f"{a} == {b} -> {a == b}")  # 1/2 == 3/4 -> False

    # Comparison
    print(f"{a} < {b} -> {a < b}")   # True
    print(f"{b} > {d} -> {b > d}")   # True
    print(f"{a} < {d} -> {a < d}")   # False

    # Show method
    print("Show method output:")
    a.show()

    f = Fraction(7, 3)
    print(f"Numerator of {f}: {f.get_num()}")      # Should print 7
    print(f"Denominator of {f}: {f.get_den()}")    # Should print 3

    g = Fraction(10, 4)
    print(f"Numerator of {g}: {g.get_num()}")      # Should print 5 (after reduction)
    print(f"Denominator of {g}: {g.get_den()}")    # Should print 2 (after reduction)
