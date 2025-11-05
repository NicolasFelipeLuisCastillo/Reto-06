words: list = ["amor", "roma", "alerta", "ratela", "python", "java", "perro", "vaja"]

def find_anagrams(words):
    try:
        if not isinstance(words, list):
            raise TypeError("Input must be a list of strings.")

        if not words:
            raise ValueError("The list of words cannot be empty.")

        for w in words:
            if not isinstance(w, str):
                raise ValueError(f"Invalid element '{w}' — all elements must be strings.")

        anagrams: list = []

        for previous_word in range(len(words)):
            for next_word in range(previous_word + 1, len(words)):
                if sorted(words[previous_word].lower()) == sorted(words[next_word].lower()):
                    if words[previous_word] not in anagrams:
                        anagrams.append(words[previous_word])
                    if words[next_word] not in anagrams:
                        anagrams.append(words[next_word])

        if not anagrams:
            print("No anagrams found in the list.")
        else:
            print(f"The anagrams are: {anagrams}")

    except TypeError:
        print(f"TypeError: {TypeError}")
    except ValueError:
        print(f"ValueError: {ValueError}")
    except Exception:
        print(f"Unexpected error: {Exception}")

find_anagrams(words)
