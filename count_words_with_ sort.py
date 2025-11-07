text = "python is fun and python is powerful"

words_list = text.split(" ")
words_dict = {}

for word in words_list:
    if word in words_dict:
        words_dict[word] += 1
    else:
        words_dict[word] = 1


sorted_words = sorted(words_dict.items(), key=lambda x: x[1], reverse=True)

for word, count in sorted_words:
    print(f"{word}: {count}")