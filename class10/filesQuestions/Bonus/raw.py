with open("raw_text.txt", "r") as f:
    lines = [line.strip().replace("\t", " ") for line in f]
with open("raw_text.txt", "w") as f:
    f.write("\n".join(lines))

print("Text formatted: leading/trailing spaces removed, tabs converted to spaces.")