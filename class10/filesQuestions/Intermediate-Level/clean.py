with open('input.txt', 'r') as infile:
    lines = infile.readlines()
with open('cleaned.txt', 'w') as outfile:
    for line in lines:
        if line.strip():  
            outfile.write(line)

print("Empty lines removed. Cleaned data saved to 'cleaned.txt'.")
