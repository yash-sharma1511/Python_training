with open('article.txt', 'r') as file:
    content = file.read()
updated_content = content.replace("Python", "PYTHON")
with open('article.txt', 'w') as file:
    file.write(updated_content)

print('All occurrences of "Python" have been replaced with "PYTHON".')
