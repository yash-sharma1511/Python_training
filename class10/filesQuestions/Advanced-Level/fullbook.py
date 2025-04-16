chapters=["chapter1.txt","chapter2.txt","chapter3.txt"]
with open("full_book.txt",'w') as outfile:
    for chapter in chapters:
        with open(chapter,'r') as infile:
            content=infile.read()
            outfile.write(content+ '\n')
print("chapters combined in full_book.txt")            

