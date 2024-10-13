import string
from PIL import Image


img = Image.open("Bliss.png")
pixels = img.load()

alphabet = string.ascii_lowercase + string.digits + ' ' + '\n'
input_str = """example text"""

#0,1,2, corresponds to what r,g,b will be changed
channel = 0
#make this a prime number or else a multiplier will also decode
multiplier = 100

width, height = img.size
point_x, point_y = 0, 0

letter_num = 0

#a for loop is pointless here because we may need extra iterations if the numbers are negative a lot
while letter_num < len(input_str):
    color = pixels[point_x, point_y]

    #make fucking sure its a tuple and not a single number like some images are for some reason in certain colors
    if type(color) == type(tuple()):
        #get a new color by subtracting the index of the letter in the alphabet list (the +1 is so that if its the index 0 in alphabet it still encodes)
        changed_col = color[channel] - (alphabet.index(input_str[letter_num]) + 1)

        #make sure it isnt negative (the image editing library wont throw an error, it will instead troll me if the number is negative)
        if changed_col > 0:
            new_col = list(color)
            new_col[channel] = changed_col
            img.putpixel((point_x,point_y), tuple(new_col))

            #go up a letter and increase by multiplier if the number isnt negative and wrong
            letter_num += 1
            point_x += multiplier
        else:
            #just skip that pixel if its negative and try the next one
            point_x += 1
    else:
        point_x += 1    

    #wrap around for the y axis
    if point_x >= width:
        point_y += 1
        point_x = point_x - width

img.save("new.png")
