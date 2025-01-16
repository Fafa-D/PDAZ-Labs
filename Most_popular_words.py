#open file

story = open("beatrix.txt", "r")


#Read the file, remove punctuation using join() function and convert to lowercase using.lower()

import string
clean_story = ''.join([char.lower() for char in story.read() if char not in string.punctuation])


#convert text into a list of words using split() method

word_list = clean_story.split()


#create a dictionary from the list which counts the occurrence of each word using a for loop

word_dict = {}
for word in word_list:
    if word not in word_dict:
        word_dict[word] = 1
    else:
        word_dict[word] = word_dict[word] + 1



#sort the dictionary from word with highest occurence using the key parameter - converts dictionary to a list of tuples

dict_sort = sorted(word_dict.items(), key=lambda item: item[1], reverse = True)

#shorten the tuple list to the first 10, then only append the first item of each tuple to a list

word_sort = dict_sort[0:11]

popular_words = []
for x in word_sort:
    popular_words.append(x[0])

print(popular_words)
