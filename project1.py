# Imports
import os
import re
import csv
from collections import OrderedDict
from collections import Counter

# Initializations
line_count = 0
no_of_words = 0
no_of_sentences = 0
the_count = 0
words = 0
counts = dict()

# Read file
location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname('war_and_peace.txt')))
file_open = open(os.path.join(location, 'war_and_peace.txt'))
file_read = file_open.readlines()

# 0. Total number of words and sentences
for line in file_read:
    words = line.split()
    sent = line.count('.')
    no_of_words += len(words)  # Number of words
    no_of_sentences += sent  # Number of sentences

    # 2. Number of sentences where the first word in the sentence is the/The
    the_count += (line.count('. The ') + line.count('! The ') + line.count('? The ')
                  + line.count('. "The ') + line.count('? "The') + line.count('! "The ')
                  + line.count(". 'The ") + line.count("? 'The ") + line.count("! 'The ")
                  + line.count(' \nThe ') + line.count(' \n"The') + line.count(" \n'The ")
                  + line.count("* The ") + line.count("* 'The ") + line.count('* "The ') + line.count(
                " \n* The ") + line.count(" \n*The "))
the_frequency = (float(the_count) / float(no_of_sentences)) * 100  # the/The frequency

# 1.Occurrences of each word and the frequency
for word in file_read:
    word = word.lower()
    word = re.sub("-", ' ', word)  # Substituted hyphens with blanks
    word = word.split()

    for w in word:
        k = re.sub("[^A-Za-z0-9]+", '', w)  # Removed special characters
        words.append(k)  # Updated
        if k not in counts:
            counts[k] = 1
        else:
            counts[k] += 1

with open('result.csv', "w+") as result:  # Writing CSV
    csv_writer = csv.writer(result, delimiter=',')
    csv_writer.writerow(['Word', 'Occurrence', 'Percent Frequency'])
    sorted_count = OrderedDict(reversed(sorted(counts.items(), key=lambda t: t[1])))

    for c in sorted_count:  # Frequency of each word
        word_frequency = (float(counts[c]) / float(no_of_words)) * 100
        csv_writer.writerow([c, counts[c], word_frequency])

# Outputs
print("Number of words : ")
print(no_of_words)
print("Number of sentences : ")
print(no_of_sentences)
print("Number of sentences, frequency where the first word in the sentence is the/The : ")
print(the_count, the_frequency)
# 3. Most frequent two word combination
print("Most frequent two word combination : ")
print(Counter(zip(words, words[1:])).most_common(3))

result.close()
file_open.close()
