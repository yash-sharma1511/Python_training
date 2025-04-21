sentences = ["the quick brown fox", "jumps over the lazy dog", "the dog barked"]
def word_to_sentence_indices(sentences):
    word_dict = {}
    idx = 0  
    for sentence in sentences:
        words = sentence.split()
        for word in words:
            if word in word_dict:
                word_dict[word].append(idx)
            else:
                word_dict[word] = [idx]
        idx += 1  
    return word_dict
result = word_to_sentence_indices(sentences)
print(result)
