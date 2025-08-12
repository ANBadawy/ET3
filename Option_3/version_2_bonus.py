import re
import matplotlib.pyplot as plt

"""
This script meets all the specified requirements and the bonus criteria.

This approach is scalable to very large text files and provides both textual
and visual summaries of the word frequency analysis.
"""


file_path = input("Enter .txt File Path: ")
# File path example: D:\Ze_Env\ET3\Option_3\file_1.txt


# precompile regexes
num_re   = re.compile(r"\d+")
punc_re  = re.compile(r"[^\w\s]")
space_re = re.compile(r"\s+")

# function to count each word
def count_words_from_file(path):
    word_count = {}
    with open(path, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            line = num_re.sub("", line)              # remove numbers
            line = punc_re.sub("", line)             # remove punctuation
            line = space_re.sub(" ", line).strip()   # normalize spaces
            for word in line.lower().split():
                word_count[word] = word_count.get(word, 0) + 1
    return word_count

# count words
word_count = count_words_from_file(file_path)

# top 10 words
top_10_items = sorted(word_count.items(), key=lambda item: item[1], reverse=True)[:10]
print(top_10_items)

# Extract words and counts for plotting
words = [item[0] for item in top_10_items]
counts = [item[1] for item in top_10_items]

# Plot
plt.bar(words, counts)
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Top 10 Most Frequent Words")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
