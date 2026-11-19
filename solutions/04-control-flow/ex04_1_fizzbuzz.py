"""Reference solution for exercise 04-1 (Control flow)."""


def fizzbuzz(limit: int = 20) -> None:
    """FizzBuzz from 1 to 20: print "Fizz" for multiples of 3, "Buzz" for multiples
    of 5, "FizzBuzz" for both, otherwise the number.

    fizzbuzz() prints 1 to 20, one value per line. fizzbuzz(5) stops at 5.
    """
    for n in range(1, limit + 1):
        if n % 15 == 0:
            print("FizzBuzz")
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        else:
            print(n)
