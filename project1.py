# Imports
import os
import re
import csv
from collections import OrderedDict
from collections import Counter

# Initializations
no_of_words = 0
no_of_sentences = 0
the_count = 0
all_words = 0
wordcount = dict()

# Read file
location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname('war_and_peace.txt')))
file_open = open(os.path.join(location, 'war_and_peace.txt'))
file_read = file_open.readlines()

# 0. Total number of words and sentences
for line in file_read:
    all_words = line.split()
    no_of_words += len(all_words)  # Number of words
    no_of_sentences += line.count('.')  # Number of sentences

    # 2. Number of sentences where the first word in the sentence is 'The'
    the_count += (line.count('. The ') + line.count('! The ') + line.count('? The ') + line.count('* The ')
                    + line.count('. "The ') + line.count('? "The') + line.count('! "The ') + line.count('* "The ')
                    + line.count(". 'The ") + line.count("? 'The ") + line.count("! 'The ") + line.count("* 'The "))
the_frequency = (the_count / no_of_sentences) * 100   # the/The frequency

# 1.Occurrences of each word and the frequency
for word in file_read:
    word = re.sub("-", ' ', word.lower())  # Substituted hyphens with blanks
    for w in word.split():
        rem = re.sub("[^A-Za-z0-9]+", '', w)  # Removed special characters
        if rem not in wordcount:
            wordcount[rem] = 1
        else:
            wordcount[rem] += 1
        all_words.append(rem)  # Updated
sorted_count = OrderedDict(reversed(sorted(wordcount.items(), key = lambda t : t[1])))

with open('result.csv', "w+") as result:  # Writing CSV
    q = csv.writer(result)
    q.writerow(['Word', 'Occurrence', '% Frequency'])
    for c in sorted_count:  # Frequency of each word
        word_frequency = (wordcount[c] / no_of_words) * 100
        q.writerow([c, wordcount[c], word_frequency])

# Outputs
print("Number of words : ")
print(no_of_words)
print("Number of sentences : ")
print(no_of_sentences)
print("Number of sentences, frequency where the first word in the sentence is 'The' : ")
print(the_count, the_frequency)

# 3. Most frequent two word combination
print("Most frequent two word combination : ")
two_words = zip(all_words, all_words[1:])
print(Counter(two_words).most_common(3))    # First three Pairs

result.close()
file_open.close()
