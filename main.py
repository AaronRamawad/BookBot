import sys
from stats import count_words, count_characters, sort_by_characters

def get_book_text(filepath):
    with open(filepath, "r+", encoding="utf-8") as file:
        file_length = len(file.readlines())
    with open(filepath, "r+", encoding="utf-8") as file:
        text = ""
        for _ in range(file_length):
            line = file.readline().rstrip("\n") + " "
            if line != " " or line != "\n":
                text += line
    return text


def main():
    try:
        path = sys.argv[1]
    except IndexError:
        print("Include book path in flag")
        sys.exit(1)
    except FileNotFoundError:
        print("That File Does Not Exist")
        sys.exit(1)
    text = get_book_text(path)
    print("================BookBOT=============")
    print(f"Analyzing book found at {path}...")
    print("-------------Word Count-------------")
    print(f"Found Word Count: {count_words(text)} Words")
    print("------------Character Count---------")
    character_dictionary = count_characters(text)
    for char in sort_by_characters(character_dictionary):
        print(f"{char[0]}: {char[1]}")
    print("===============END===============")
    
    sys.exit(1)
    

if __name__ == "__main__":
    main()
