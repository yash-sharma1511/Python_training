with open('story.txt', 'r') as file:
    text = file.read()
words = text.lower().split()
import string
words = [word.strip(string.punctuation) for word in words]
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
with open('frequency.txt', 'w') as outfile:
    for word, count in sorted(word_count.items()):
        outfile.write(f"{word}: {count}\n")

print("Word frequencies written to 'frequency.txt'.")
