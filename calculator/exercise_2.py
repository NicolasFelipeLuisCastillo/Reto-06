word: str = input("Enter a word: ")

def reverse_word(word):
    try:
        if not word.strip():
            raise ValueError("You must enter a non-empty word.")

        word = word.lower()
        result: str = ""

        if not word.isalpha():
            raise ValueError("The word must contain only letters.")

        for letter in word:
            result: str = letter + result
            print(letter)
            print(result)

        if word == result:
            print("The word is a palindrome")
        else:
            print("The word is not a palindrome")

    except ValueError:
        print(f"ValueError: {ValueError}")

    except TypeError:
        print("TypeError: Input must be a string.")

reverse_word(word)
