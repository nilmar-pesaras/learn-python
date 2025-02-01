import string


# Basic Problem
# 1. Write a program that reverses a string.
# 2. Create a function that counts vowels in a string.
# 3. Write a program that checks if a string is a palindrome.


def reverse_string(string_input) -> str:
    return string_input[::-1]


def count_vowels(
    string_input,
) -> int:  # this function counts the number of vowels in a string
    vowels = "aeiouAEIOU"
    return sum(1 for char in string_input if char in vowels)


def is_palindrome(
    string_input,
) -> bool:  # this function checks if a string is a palindrome
    return string_input == string_input[::-1]


input_string: str = "The quick brown fox jumps over the lazy dog"

print(f"reverse_string: {reverse_string(input_string)}")
print(f"count_vowels: {count_vowels(input_string)}")
print(f"is_palindrome: {is_palindrome(input_string)}")


# Intermediate Problem

# 1. Write a program that counts words in a string
# 2. Create a function that removes all punctuation from a string
# 3. Write a program that converts a string to "Pig latin"


def count_words(
    string_input,
) -> int:  # this function counts the number of words in a string
    return len(string_input.split())


def remove_punctuation(
    string_input,
) -> str:  # this function removes all punctuation from a string
    return string_input.translate(str.maketrans("", "", string.punctuation))


def convert_to_pig_latin(
    string_input,
) -> str:  # this function converts a string to "Pig latin"
    return string_input[1:] + string_input[0] + "ay"


print(f"count_words: {count_words(input_string)}")
print(f"remove_punctuation: {remove_punctuation(input_string)}")
print(f"convert_to_pig_latin: {convert_to_pig_latin(input_string)}")
