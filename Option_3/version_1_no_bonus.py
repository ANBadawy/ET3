import re

"""
This script meets all the specified requirements.

It processes the entire file in memory, which is fine for small to moderately sized files,
but may be inefficient for very large files.
"""


file_path = input("Enter .txt File Path: ")
# File path example: D:\Ze_Env\ET3\Option_3\file_1.txt

with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:

    content = file.read()

    # remove numbers
    cleaned = re.sub(r"\d+", "", content)

    # remove all punc
    cleaned = re.sub(r"[^\w\s]", "", cleaned)

    # remove extra spaces
    cleaned = re.sub(r"\s+", " ", cleaned).strip()

    # convert to lowercase and split into words
    cleaned = cleaned.lower().split()
    
    # print the new list of words
    # print(cleaned)


# function to count each word
def count_words(word_list):
    word_count = {}
    for word in word_list:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count


word_count = count_words(cleaned)
# print(word_count)

# list compehenshion to get the top 10 words
top_10_keys = [{k: v} for k, v in sorted(word_count.items(), key=lambda item: item[1], reverse=True)[:10]]
print(top_10_keys)