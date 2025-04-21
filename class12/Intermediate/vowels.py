def count_vowels(sentence: str) -> int:
    vowels = ['a','e','i','o','u']
    count = 0
    for char in sentence.lower():  
        if char in vowels:
            count += 1
    return count        
sentence = input("Enter Sentence: ")   
print(count_vowels(sentence))
