# *************************************************
# Functions
# *************************************************
# Builds the doc_word_index dictionary by using another container as
# argument on the parameter data
# Don't modify this function
def build_doc_word_index(data):
    temp_dictionary = {}
    for document, words_list in data.items():
        inner_dictionary = {}

        for word in words_list:
            if word in inner_dictionary:
                inner_dictionary[word] += 1
            else:
                inner_dictionary[word] = 1

        temp_dictionary[document] = inner_dictionary

    return temp_dictionary


# Builds the global_count_index dictionary by using another container as
# argument on the parameter data
# Don't modify this function
def build_global_count_index(data):
    temp_dictionary = {}
    for document,words_list in data.items():
        for word in words_list:
            if word in temp_dictionary:
                temp_dictionary[word] += 1
            else:
                temp_dictionary[word] = 1
    return temp_dictionary

# ***********************
# You have to implement the functions that follow. Originally they are simple
# placeholders, indicating what are the parameters in the difinition of the function
# and the data type to be returned to the caller
# ***********************


# Builds the word_count_index dictionary by using another container as
# argument on the parameter data
def build_word_count_index(data):
    temp_dictionary = {}

    return temp_dictionary


# Builds the weighted_word_count_index dictionary by using another container as
# argument on the parameter data
def build_weighted_word_count_index(data):
    temp_dictionary = {}

    return temp_dictionary


# Builds the doc_inverted_index dictionary by using another container as
# argument on the parameter data
def build_doc_inverted_index(data):
    temp_dictionary = {}

    return temp_dictionary


# Builds the doc_dictionary dictionary by using another container as
# argument on the parameter data
def build_doc_dictionary(data):
    temp_dictionary = {}

    return temp_dictionary


# Builds the adjusted_index dictionary by using another container as
# argument on the parameter data
def build_adjusted_index(data):
    temp_dictionary = {}

    return temp_dictionary

