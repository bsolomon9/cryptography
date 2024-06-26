import string
from PIL import Image

img = Image.open("new.png")
original = Image.open("Bliss.png")

pixels = img.load()
original_pixels = original.load()

alphabet = string.ascii_lowercase + string.digits + ' ' + '\n'

#these need to match the given values for the encoded image (if the channel is wrong it will get nothing, if the multiplier is too high or the correct one isnt divisible by it, it wont get all of the letters)
channel = 0
multiplier = 10

width = img.size[0]
height = img.size[1]

point_x = 0
point_y = 0

out = ''
while True:
    #get the difference of the colors by literally just subtracting the color values on the given channel
    delta_color = original_pixels[point_x, point_y][channel] - pixels[point_x, point_y][channel]
    if delta_color != 0:
        #subtract one because we had to add one on encoding to prevent it from subtracting 0 and making the same color
        out += alphabet[delta_color-1]

        #this iteration worked! go to the next letter like the encoder would to save time
        point_x += multiplier
    else:
        #if there is no difference it must be skipped in encoding due to a negative color, or it must be after the message, skip that pixel
        point_x += 1

    #wrap around the y axis
    if point_x >= width:
        point_y += 1
        point_x = point_x - width
        #break if we go off of the image
        if point_y > height-1:
            break


print(out)