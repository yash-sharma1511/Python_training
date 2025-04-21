def analyze_text(text: str):
    word = text.lower().split()
    count = len(word)
    unique = set(word)
    uni_count = len(unique)

    fre = {}
    for word in word:
        fre[word] = fre.get(word, 0) + 1

    return count, uni_count, fre
text = "This is a test."
count, uni_count, fre = analyze_text(text)
print("word:", count)
print("Unique word:", uni_count)
print("fre:", fre)
