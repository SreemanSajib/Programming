DELIMITER = ','

def collectWords(): 
    words = []

    while True: 
        word = input("Insert word(empty stops): ")
        if word == "":
            break
        words.append(word)
    
    return DELIMITER.join(words)

def analysewords(words_string): 
    words = words_string.split(DELIMITER)
    

    word_count = len(words)
    char_count = sum(len(word) for word in words)

    if word_count > 0:
        average_length = char_count / word_count
    else:
        average_length = 0.0

    print(f"- {word_count} words")
    print(f"- {char_count} characters")
    print(f"- {average_length:.2f} average length")

def main():
    print("Program starting.")

    collected_words = collectWords()
    analysewords(collected_words)
    print("Program ending.")

if __name__ == "__main__":
    main()