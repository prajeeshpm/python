def break_words(stuff):
    """ This function will break up words for us."""
    words = stuff.split(' ')
    return words
def sort_words(words):
    """sort the words."""
    return sorted(words)
def print_first_word(words):
    """ printst he first word after possping it iff."""
    word = words.pop(0)
    print(word)
def print_last_word(words):
    """ Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)
def sort_sentence(sentence):
    """take full sentence and returns the sorted words. """
    words = break_words(sentence)
    return sort_words(words)
def print_first_and_last(sentece):
    """ print the first and last sentence """
    words = break_words(sentece)
    print_first_word(words)
    print_last_word(words)
def print_first_and_last_sorted(sentense):
    """soret the words th words = ex25.break_words(sentence) en """
    words = sort_sentence(sentense)
    print_first_word(words)
    print_last_word(words)
