"""Lesson 24 · Debugging · exercise 1.

Check your work with: uv run course.py
"""


def to_cents(price: str) -> int:
    """Convert a price like "24.50" to cents (2450)."""
    return int(price) * 100


def parse_line(line: str) -> int:
    """Turn "Lamp,24.50,2" into the line total in cents."""
    _name, price, qty = line.split(",")
    return to_cents(price) * int(qty)


def order_total(csv_text: str) -> int:
    """Fix the bug behind this traceback. Running the file prints it:

        Traceback (most recent call last):
          File "ex24_1_fix_the_bug.py", line 53, in <module>
            print(order_total("Lamp,24.50,2\\nDesk,150,1"))
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          File "ex24_1_fix_the_bug.py", line 49, in order_total
            return sum(parse_line(line) for line in csv_text.splitlines())
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          File "ex24_1_fix_the_bug.py", line 49, in <genexpr>
            return sum(parse_line(line) for line in csv_text.splitlines())
                       ^^^^^^^^^^^^^^^^
          File "ex24_1_fix_the_bug.py", line 15, in parse_line
            return to_cents(price) * int(qty)
                   ^^^^^^^^^^^^^^^
          File "ex24_1_fix_the_bug.py", line 9, in to_cents
            return int(price) * 100
                   ^^^^^^^^^^
        ValueError: invalid literal for int() with base 10: '24.50'

    Read it from the bottom up: the last line is the error, and the frame just
    above it is where it happened. The frames above that show how the program
    got there, with the oldest call at the top.

    order_total("Lamp,24.50,2\\nDesk,150,1") must return 19900 (cents).
    Prices can have up to two decimals: "0.10" is 10 cents.

    Optional: put breakpoint() as the first line of to_cents, run the file
    with uv run, and try p price, w, u, d and c at the (Pdb) prompt.
    """
    return sum(parse_line(line) for line in csv_text.splitlines())


if __name__ == "__main__":
    print(order_total("Lamp,24.50,2\nDesk,150,1"))
