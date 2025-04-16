with open('input.txt', 'r') as infile:
    content = infile.read()
uppercase_content = content.upper()
with open('output.txt', 'w') as outfile:
    outfile.write(uppercase_content)

print("Content written to 'output.txt' in uppercase.")
