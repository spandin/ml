text = "python is fun and python is powerful"

words_list = text.split(" ")
words_dict = {}
indices = []

for word in words_list:
    if word not in words_dict:
        words_dict[word] = len(words_dict)
    indices.append(words_dict[word])


print(f"Словарь: {words_dict}")
print(f"Текст в индексах: {indices}")
