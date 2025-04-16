import os
if os.path.exists('poems.txt'):
    with open('poems.txt', 'r') as file:
        content = file.read()
        print("File content:\n", content)
else:
    print("The file 'poems.txt' does not exist.")
