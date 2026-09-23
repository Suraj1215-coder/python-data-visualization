"""String and Boolean operations demonstration.

Run this file with Python 3.  The last section asks for login credentials.
"""


def count_text_items(text):
    """Return counts for vowels, consonants, words, and all characters."""
    vowels = sum(character.lower() in "aeiou" for character in text)
    consonants = sum(
        character.isalpha() and character.lower() not in "aeiou"
        for character in text
    )
    words = len(text.split())
    characters = len(text)  # Includes spaces and punctuation.
    return vowels, consonants, words, characters


def is_palindrome(text):
    """Check a string while ignoring letter case, spaces, and punctuation."""
    cleaned_text = "".join(
        character.lower() for character in text if character.isalnum()
    )
    return cleaned_text == cleaned_text[::-1]


def compare_strings(first, second):
    """Return a human-readable lexicographic comparison."""
    if first == second:
        return f'"{first}" is equal to "{second}".'
    if first < second:
        return f'"{first}" comes before "{second}".'
    return f'"{first}" comes after "{second}".'


def login(username, password):
    """Return True only when both credentials match."""
    valid_username = username == "admin"
    valid_password = password == "Python@123"
    return valid_username and valid_password


def show_evaluation(name, value):
    """Print when an expression is evaluated; useful for short-circuit examples."""
    print(f"  Evaluated: {name}")
    return value


def main():
    print("1. Creating strings")
    single_quoted = 'This string uses single quotes.'
    double_quoted = "This string uses double quotes."
    triple_quoted = """This is a triple-quoted string.
It can span multiple lines."""
    print(single_quoted)
    print(double_quoted)
    print(triple_quoted)

    print("\n2. Indexing and negative indexing")
    text = "Python Programming"
    print(f"Text: {text}")
    print(f"text[0] = {text[0]}")
    print(f"text[7] = {text[7]}")
    print(f"text[-1] = {text[-1]}")
    print(f"text[-5] = {text[-5]}")

    print("\n3. Reversing a string with slicing")
    print(f"Original: {text}")
    print(f"Reversed: {text[::-1]}")

    print("\n4. Counting vowels, consonants, words, and characters")
    sample_text = "Hello, Python World!"
    vowels, consonants, words, characters = count_text_items(sample_text)
    print(f"Text: {sample_text}")
    print(
        f"Vowels: {vowels}, Consonants: {consonants}, "
        f"Words: {words}, Characters: {characters}"
    )

    print("\n5. Palindrome check")
    palindrome_text = "Never odd or even"
    print(f'"{palindrome_text}" is a palindrome: {is_palindrome(palindrome_text)}')

    print("\n6. Lexicographic comparison")
    first_string = "apple"
    second_string = "banana"
    print(compare_strings(first_string, second_string))

    print("\n7. replace(), split(), join(), and strip()")
    sentence = "Python is easy to learn"
    colors = "red,green,blue"
    padded_text = "   remove extra spaces   "
    color_list = colors.split(",")
    print(f"replace(): {sentence.replace('easy', 'powerful')}")
    print(f"split(): {color_list}")
    print(f"join(): {' | '.join(color_list)}")
    print(f"strip(): '{padded_text.strip()}'")

    print("\n8. Formatting output with f-strings")
    name = "Aarav"
    score = 92.5
    print(f"{name} scored {score:.1f}% in Python.")

    print("\n9. Boolean expressions")
    age = 20
    has_id = True
    is_raining = False
    print(f"Age is at least 18 and has ID: {age >= 18 and has_id}")
    print(f"Age is under 18 or it is raining: {age < 18 or is_raining}")
    print(f"It is not raining: {not is_raining}")
    print(f"'Python' is in text: {'Python' in text}")

    print("\n10. Truth-value testing")
    values = {
        "number 0": 0,
        "number 42": 42,
        "empty string": "",
        "non-empty string": "Python",
        "empty list": [],
        "non-empty list": [1, 2],
        "empty dictionary": {},
        "non-empty dictionary": {"language": "Python"},
    }
    for description, value in values.items():
        print(f"{description}: bool({value!r}) = {bool(value)}")

    print("\n11. Login program using Boolean logic")
    print("Test credentials: username = admin, password = Python@123")
    try:
        username = input("Username: ")
        password = input("Password: ")
    except EOFError:
        print("No input was provided; login demonstration skipped.")
    else:
        if login(username, password):
            print("Login successful.")
        else:
            print("Invalid username or password.")

    print("\n12. Short-circuit evaluation")
    print("Using and (the second expression is skipped when the first is False):")
    and_result = show_evaluation("first False value", False) and show_evaluation(
        "second True value", True
    )
    print(f"  Result: {and_result}")

    print("Using or (the second expression is skipped when the first is True):")
    or_result = show_evaluation("first True value", True) or show_evaluation(
        "second False value", False
    )
    print(f"  Result: {or_result}")


if __name__ == "__main__":
    main()
