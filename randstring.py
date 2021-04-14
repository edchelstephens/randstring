import random
import string

UPPERCASE_LETTERS = string.ascii_uppercase
LOWERCASE_LETTERS = string.ascii_lowercase
ASCII_LETTERS = string.ascii_letters
DIGITS = string.digits
PUNCTUATION = string.punctuation


def randstring(length, selection_string):
    """Generate a random string with each character selected randomly from the selection_string."""
    return "".join(random.choice(selection_string) for i in range(length))

def random_uppercase(length):
    """Return a random uppercased letter string with given length."""
    return randstring(length, UPPERCASE_LETTERS)

def random_lowercase(length):
    """Return a random lowercase lettered string with given length."""
    return randstring(length, LOWERCASE_LETTERS)

def random_mixcase(length):
    """Return a random lettered string with mixed lowercase and uppercase."""
    return randstring(length, ASCII_LETTERS)

def random_mix_letter_uppercase_digit(length):
    """Return a random string with mixed uppercase and with numbers."""
    return randstring(length, UPPERCASE_LETTERS + DIGITS)

def random_mix_letter_lowercase_digit(length):
    """Return a random string with mixed lowercase and numbers."""
    return randstring(length, UPPERCASE_LETTERS + DIGITS)

def random_mix_letter_digit(length):
    """Return a random string with mixed lowercase and uppercase with numbers."""
    return randstring(length, ASCII_LETTERS + DIGITS)

def random_string(length):
    """Return a random string with mixed lowercase uppercase, numbers and symbol."""
    return randstring(length, ASCII_LETTERS + DIGITS + PUNCTUATION)

