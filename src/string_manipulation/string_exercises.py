import string


# Basic Problem

# Problem 1
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


# Problem 2
# Create a function that alternates the case of each character in a string.


def alternate_case(string_input) -> str:
    result: str = ""
    for i, char in enumerate(string_input):
        if i % 2 == 0:
            result += char.upper()
        else:
            result += char.lower()
    return result


print(f"alternate_case: {alternate_case(input_string)}")
