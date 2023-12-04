from turtle import *
import celtic.stats as stats
import celtic.parser as parser
import celtic.viz as viz
import pprint

# The student working on the parser (populating the dictionaries) should modify this
# script.

# change the value of this variable as you complete each function
# the values go from 3 to 7
working_on = 3

# change this value to True for displaying the viz plots only if you decide
# to work on the bonus functions in the visualization module
display_plots = False

# which_dataset indicates the dataset to use as input
#   1 is for the fake_corpus.txt (3 documents small)
#   2 is for the text_corpus.txt (3 documents)
#   3 is for the text_corpus_large.txt (1000 documents)
#   4 is for the text_corpus_larger.txt (2000 documents)
# To test your script with a different dataset change the value of this
# variable, by default use 1, which corresponds to fake_corpus.txt file
which_dataset = 1

datasets = {
    1: 'fake_corpus.txt',
    2: 'text_corpus.txt',
    3: 'text_corpus_large.txt',
    4: 'text_corpus_larger.txt'
}

if which_dataset < 1 or which_dataset > 4:
    print('----> use a value between 1 and 4 for which_dataset')
    exit()

# ************************************************
# Dictionary variables
# ************************************************

# These are the variables for storing or referencing the dictionaries
# that will be built when invoking the different functions below.
# Initially they are empty.

corpus_data = {}
doc_word_index = {}
global_count_index = {}
word_count_index = {}
weighted_word_count_index = {}
doc_inverted_index = {}
doc_dictionary = {}
adjusted_index = {}

# ************************************************
# Invoking functions to build and populate the
# dictionaries.
# ************************************************

print('***************************************************')
print('building dictionaries')
print('***************************************************')

# builds a dictionary with documents and words in each document
# using one of the text files passed as argument to the function
# parser.read_file().
# the variable corpus_data will reference that dictionary

if working_on >= 1:
    print('******* Corpus Data *******')
    corpus_data = parser.read_file(datasets[which_dataset])
    pprint.pprint(corpus_data, width=50, compact=False, sort_dicts=False)

# Note: as you implement the other functions that populate the rest
# of the dictionaries, look at the output of the previously populated
# dictionaries to decide which is the best suited to be passed as
# argument to each function. In this example, corpus_data is used
# but most likely you have to use a different dictionary as argument
# for each invocation of the functions.
# As you complete each function, change the value of the variable
# working_on defined in line 12, to the next number 3, 4, 5, 6, or 7

if working_on >= 2:
    print('******* Build Document Word Index *******')
    doc_word_index = parser.build_doc_word_index(corpus_data)
    pprint.pprint(doc_word_index, width=50, compact=False, sort_dicts=False)

    print('******* Build Global Count Index *******')
    global_count_index = parser.build_global_count_index(corpus_data)
    pprint.pprint(global_count_index, width=50, compact=False, sort_dicts=False)

if working_on >= 3:
    print('******* Build Word Count Index *******')
    word_count_index = parser.build_word_count_index(corpus_data)
    pprint.pprint(word_count_index, width=50, compact=False, sort_dicts=False)

if working_on >= 4:
    print('******* Build Weighted Word Count Index *******')
    weighted_word_count_index = parser.build_weighted_word_count_index(corpus_data)
    pprint.pprint(weighted_word_count_index, width=50, compact=False, sort_dicts=False)

if working_on >= 5:
    print('******* Build Document Inverted Index *******')
    doc_inverted_index = parser.build_doc_inverted_index(corpus_data)
    pprint.pprint(doc_inverted_index, width=50, compact=False, sort_dicts=False)

if working_on >= 6:
    print('******* Build Document Dictionary *******')
    doc_dictionary = parser.build_doc_dictionary(corpus_data)
    pprint.pprint(doc_dictionary, width=50, compact=False, sort_dicts=False)

if working_on >= 7:
    print('******* Build Adjusted Index *******')
    adjusted_index = parser.build_adjusted_index(corpus_data)
    pprint.pprint(adjusted_index, width=50, compact=False, sort_dicts=False)

if display_plots == True:
    # Implementing the functions below is optional and a bonus for the project
    # they are not required
    print('***************************************************')
    print('vizualization')
    print('***************************************************')

    # plots a bar chart defined in celtic.viz
    viz.plot_top_k_freq_words_doc(doc_word_index, 'document3', 5)
    # viz.plot_bottom_k_freq_words_doc(doc_word_index, 'document3', 3)
    # viz.plot_freq_word_doc(corpus_data, ['document1', 'document2'], "the")

    # makes the the plot stop, uncomment this line when working on your code
    # to test the functions in the viz module
    viz.render()

