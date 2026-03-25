from email.mime import message

from PIL import Image
obr = Image.open("Priroda.png")
sprava = input("Zadejte správu, ktoru chcete zašifrovať: ")

def sprava_to_bin(message):
    message += "#"
    output = ""
    for char in message:
        temp = bin(ord(char))[2::]
        if len(temp) < 7:
           pocet = 7 - len(temp)
           temp = "0" * pocet + temp
        output += temp
    return output

def picture_shredder(bin_message, picture):
    pixels = picture.load()
    for i in range(len(bin_message)):
        x = i % picture.size[0]
        y = i // picture.size[0]
        blue_bin = bin(pixels[x, y][2])[2:-1:] # 2 -> odtrhne 0b , -1 -> odtrhne posledny
        blue_bin = blue_bin + bin_message[i]
        new_blue = int(blue_bin, 2)
        pixels [x, y] = (pixels[x, y][0], pixels[x, y][1], new_blue)
    picture.save("Final.png")


bin_message = sprava_to_bin(sprava)
picture_shredder(bin_message, obr)