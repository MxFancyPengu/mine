"""stats functions

This module computes some statistics from the text corpus
"""


# Returns the number of times the most common word appears in the corpus, the parameter
# data is a container to be used for such task
# do not modify this function it has already been completed and is intended to serve as
# example for you to complete the rest!
def most_common_word(data):
    print('most_common_word: ', end='')

    most_common_word = ''
    most_common_count = 0

    for word, count in data.items():
        if count > most_common_count:
            most_common_count = count
            most_common_word = word

    return (most_common_word, most_common_count)


# Returns the document with the highest number of words
# If the second parameter is not given (the default)
# returns the document with the highest number of unique words
# Here unique words means a word that appears only once in a
# document.
# data is a container to be used for such task
def get_largest_document(data, unique=False):
    print('get_largest_document: ', end='')

    size = 0
    document = ''
    return document


# Returns the average length of the words in a document
# the parameter data is a container to be used for such task
# the parameter document is the name of the document (string)
def avg_length(data, document):
    print('avg_length: ' + document + ': ',  end='')

    count = 1
    total = 0

    return total / count


# Returns a list with all words in the corpus that end with a given letter
# the parameter data is a container to be used for such task
# the parameter letter is a string, indicating the letter
def get_words_letter_end(data, letter):
    print('get_word_letter_end: ' + letter + ': ', end='')
    words = []

    return words


# Returns a list with all words in the corpus that begin with a given letter
# the parameter data is a container to be used for such task
# the parameter letter is a string, indicating the letter
def get_words_letter_begin(data, letter):
    print('get_word_letter_begin: ' + letter + ': ', end='')
    words = []

    return words


# Returns a list with all words in the corpus of a given size
# the parameter data is a container to be used for such task
# the parameter size is an integer, indicating the size
def get_words_size(data, size):
    print('get_word_size: ' + str(size) + ': ', end='')
    words = []

    return words


# computes the average size of words in the corpus
# the parameter data is a container to be used for such task
def compute_avg(data):
    print('compute_avg: ', end='')
    avg = 0.0

    return avg


# Returns a list with all words in the corpus whose size is greater than
# the corpus words average size
def get_words_grater_avg(data, avg_size):
    print('get_words_grater_avg: ', end='')
    words = []

    return words

