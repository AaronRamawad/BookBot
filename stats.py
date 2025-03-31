import string

def count_words(text):
    words = text.split(" ")
    return len(words)

def count_characters(text):
    characters = {}
    alphabet = string.ascii_lowercase + "æâêëô"

    for char in text.lower():
        try:
            int(char)
        except ValueError:
            pass
        else:
            continue

        if char != " " and char in alphabet: 
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1

    return characters

def sort_characters(e):
    return e[1]

def sort_by_characters(char_dict):
    character_list = []
    characters = char_dict.keys()
    for key in characters:
        character_list.append((key, char_dict[key]))
    character_list.sort(key=sort_characters)
    character_list.reverse()
    return character_list


