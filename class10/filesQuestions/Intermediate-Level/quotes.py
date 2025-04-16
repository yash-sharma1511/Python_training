with open('quotes.txt', 'r') as infile:
    lines = infile.readlines()
lines.reverse()
with open('reversed_quotes.txt', 'w') as outfile:
    outfile.writelines(lines)

print("Lines reversed and saved to 'reversed_quotes.txt'.")
