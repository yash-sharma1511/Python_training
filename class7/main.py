# For Loop Basics:
for i in range(11):
    print(i)

# String Iteration:
def count(str):
   return sum(1 for char in str if char in vowels )
vowels="aeiouAEIOU"
str=input()
print(count(str))

# Accumulator Pattern:
print(sum(i*i for i in range(101)))

# Nested Loops:
for i in range(1,11):
    for j in range(1,11):
        print(f"{i*j:4}",end=" ")
    print()

# Image Processing:
from PIL import Image
import PIL.ImageOps  
img = Image.open("./img.jpg")

inverted_img =  PIL.ImageOps.invert(img)
inverted_img.save("inverted_image.jpg")

