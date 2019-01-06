def beak_words(stuff):
    """ This function will break up words for us."""
    words = stuff.split(' ')
    return words
def sort_words(words):
    """sort the words."""
    return sorted(words)
def print_first_words(words):
    """ printst he first word after possping it iff."""
    word = words.pop(0)
    print(word)
def print_last_words(words):
    """ Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)
def sort_sentence(sentence):
    """take full sentence and returns the sorted words. """
    words = beak_words(sentece)
    return sort_words(words)
def print_first_and_last(sentece):
    """ print the first and last sentence """
    words = break_words(sentece)
    print_first_word(words)
    print_last_words(words)
def print_first_and_last_sorted(sentense):
    """soret the words then """
    words = sort_sentense(sentense)
    print_first_word(words)
    print_last_word(words)
