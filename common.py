from random import choice
from string import ascii_letters, digits

# Generic utility functions


def randint_length(length):
    return ''.join(choice(digits) for i in range(0, length))


def randstring_length(length):
    return ''.join(choice(ascii_letters) for i in range(0, length))