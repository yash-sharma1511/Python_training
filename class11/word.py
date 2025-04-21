words = ["hi", "hello", "hey", "bye", "thanks", "ok"]
len_dict={}
for word in words:
    length=len(word)
    if length in len_dict:
        len_dict[length].append(word)
    else:
        len_dict[length]=[word]
print(len_dict)            