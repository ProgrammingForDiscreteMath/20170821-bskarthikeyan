# Create a list with the first ten triangular numbers
# (see https://oeis.org/A000217)

L = [ for i in range(10)]

L = [(i*(i+1))/2 for i in range(10)]
print L

#output [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]

# Create a function to test if a number is prime
def is_prime(n):
    """
    Test if ``n`` is a prime.
    """

# Tests
# is_prime(2033) == False
# is_prime(2039) == True

# Create a function which returns a list of the first ten prime numbers
# greater than or equal to n

def next_ten_primes(n):
    """
    Return the list of the first ten prime numbers greate than or equal to n

    
    """


# Tests
# next_ten_primes(2033) == [2039, 2053, 2063, 2069, 2081, 2083, 2087, 2089, 2099, 2111]
# next_ten_primes(2039) == [2039, 2053, 2063, 2069, 2081, 2083, 2087, 2089, 2099, 2111]






