from turtle import *
import celtic as cs
import celtic.stats as stats
import celtic.parser as parser
import celtic.viz as viz
import pprint

# *************************************************
# Do not modify this script. I will modify it myself when grading, by introducing
# my own tests code.
# Your team will be modifying and using test_student_1.py and test_student_2.py
# for running and testing your code.
# *************************************************

# to see a help for this package type help('celtic') in the python interpreter
# These are the variables for storing data to be read from text files.
# Initially they are empty

corpus_data = {}
doc_word_index = {}
global_count_index = {}
word_count_index = {}
weighted_word_count_index = {}
doc_inverted_index = {}
doc_dictionary = {}
adjusted_index = {}

print('***************************************************')
print('building dictionaries')
print('***************************************************')

# change the value of test_type to try with the different corpus data
# 1 = for fake_corpus.txt
# 2 = for text_corpus.txt
# 3 = for text_corpus_large.txt
# 4 = for text_corpus_larger.txt
test_type = 1
input_file_name = 'fake_corpus.txt'

if test_type == 2:
    input_file_name = 'text_corpus.txt'
elif test_type == 3:
    input_file_name = 'text_corpus_large.txt'
elif test_type == 4:
    input_file_name = 'text_corpus_larger.txt'

# invokes the function parser.read_file() passing as argument
# the name of the text file containing the data, by default
# uses fake_corpus
corpus_data = cs.parser.read_file(input_file_name)
pprint.pprint(corpus_data)

# using the dictionary corpus_data built in the previous step
# builds a new dictionary and stores it in the variable doc_word_index

# Note: as you implement the other functions that populate the rest
# of the dictionaries, look at the output of the previously populated
# dictionaries to decide which is the best suited to be passed as
# argument to each function. In this example, corpus_data is used
# but most likely you have to use different containers for each
# invocation of the functions.

doc_word_index = parser.build_doc_word_index(corpus_data)
pprint.pprint(doc_word_index)

global_count_index = cs.parser.build_global_count_index(corpus_data)
pprint.pprint(global_count_index)

word_count_index = cs.parser.build_word_count_index(corpus_data)
pprint.pprint(word_count_index)

weighted_word_count_index = cs.parser.build_weighted_word_count_index(corpus_data)
pprint.pprint(weighted_word_count_index)

doc_inverted_index = cs.parser.build_doc_inverted_index(corpus_data)
pprint.pprint(doc_inverted_index)

doc_dictionary = cs.parser.build_doc_dictionary(corpus_data)
pprint.pprint(doc_dictionary)

adjusted_index = cs.parser.build_adjusted_index(corpus_data)
pprint.pprint(adjusted_index)

print('***************************************************')
print('computing stats')
print('***************************************************')

# You have to implement the functions in stats, then depending on what
# dictionaries you built before, you have to decide which one to pass as
# argument to these stats functions.
# Presently these functions are returning empty results because
# the dictionaries are empty
print(stats.most_common_word(parser.fake_corpus_data))
print(stats.get_largest_document(parser.fake_corpus_data))
print(stats.avg_length(parser.fake_corpus_data, 'document1'))
print(stats.get_words_letter_end(parser.fake_corpus_data, 'a'))
print(stats.get_words_letter_begin(parser.fake_corpus_data, 'n'))
print(stats.get_words_size(parser.fake_corpus_data, 4))
print(stats.compute_avg(parser.fake_corpus_data))
print(stats.get_words_grater_avg(parser.fake_corpus_data, 4))

# Implementing the functions below is optional and a bonus for the project
# they are not required
print('***************************************************')
print('vizualization')
print('***************************************************')

# plots a bar chart defined in celtic.viz
# viz.plot_top_k_freq_words_doc(doc_word_index, 'document2', 5)
# viz.plot_bottom_k_freq_words_doc(doc_word_index, 'document3', 3)
# viz.plot_freq_word_doc(corpus_data, ['document1', 'document2'], "the")

# makes the the plot stop, uncomment this line when working on your code
# to test the functions in the viz module
#viz.render()
