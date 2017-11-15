# This will be a demo of functions


def break_words(stuff):
    """This function takes a sentence and splits the words based on empty space in it"""
    words = stuff.split(" ")
    return words


def sort_words(words):
    """ sorts the words"""
    sorted_words = sorted(words)
    print(sorted_words)


def print_first_word(words):
    """This functions takes the array of words and prints the very first word from the list"""
    word = words.pop(0)
    print("First word from the list is : {}".format(word))


def print_last_words(words):
    """This function takes the word array and prints the last word from the list"""
    last = words.pop(-1)
    print("The last word from the list is : {}".format(last))


def sort_sentence(sentence):
    """This method takes a sentence, breaks it into an array of words and the sorts em"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_words(words)
    return sort_words(words)


sentence = "I had a bad day"
sort_sentence(sentence)


