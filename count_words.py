text = "python is fun and python is powerful"

words_list = text.split(" ")
words_dict = {}

for word in words_list:
    if word in words_dict:
        words_dict[word] += 1
    else:
        words_dict[word] = 1


for word, count in words_dict.items():
    print(f"{word}: {count}")