import tkinter
import time

# import dictionaries for binary_dicts file
from binary_dicts import *

# declare pen variable as None in global scope to allow for user input
pen = None


# initialize turtle object for drawing barcode
def init(dec):
    root = tkinter.Tk()

    root.title("Barcode Generator")

    label = tkinter.Label(root, text=dec)
    label.pack()

    canvas = tkinter.Canvas(root, width=365, height=250)
    canvas.pack()
    return root, canvas


# function to draw a line
def draw_line(length, width):
    for i in range(width):
        # draw line
        pen.forward(length)
        # reset pen to position for drawing next line
        pen.penup()
        pen.left(180)
        pen.forward(length)
        pen.right(90)
        pen.forward(1)
        pen.right(90)
        pen.pendown()


# function to skip a line
def skip_line(width):
    pen.penup()
    pen.left(90)
    pen.forward(width)
    pen.right(90)
    pen.pendown()


# function to convert decimal numbers to their barcode binary conterpart
def convert(dec, type):
    # declare empty string for binary
    bin = ""
    # declare border and center values for
    border = "101"
    center = "01010"
    # add left border lines to start of barcode
    bin += border
    # converts to binary according to appropriate dictionary
    i = 0
    while i < len(dec) // 2:
        bin += type[dec[i]]
        i += 1
    # add center lines to center of barcode
    bin += center
    # converts to binary according to the inversion of the appropriate dictionary
    while i < len(dec):
        temp = type[dec[i]]
        # swaps every 1 with 0 and 0 with 1
        for bit in temp:
            bin += str(1 - int(bit))
        i += 1
    # add right border lines to end of barcode
    bin += border
    # return resulting binary
    return bin


# function to draw barcode
def draw_barcode(length, width, dec, type):
    root, canvas = init(dec)
    bin = convert(dec, type)
    i = x = 0
    while i < len(bin):
        if bin[i] == "1":
            canvas.create_rectangle(40 + x, 40, 40 + x + width, length, fill="black")

        x += width
        i += 1

    # do the thing
    root.mainloop()


def main():

    # set length of bar code lines
    length = 200
    # set width of bar code lines
    width = 3

    # set barcode type
    type = input("Enter a barcode type(UPC / EAN): ").lower()
    while type not in ["upc", "ean"]:
        type = input("Enter a barcode type(UPC / EAN): ").lower()
    if type == "upc":
        type = upc
    elif type == "ean":
        type = ean

    # set decimal value to be converted
    dec = input("Enter a barcode number: ")
    if type == "upc":
        while not dec.isnumeric() or len(dec) != 12:
            print("INVALID NUMBER - Must be 12 digits")
            dec = input("Enter a barcode number: ")
    elif type == "ean":
        while not dec.isnumeric() or len(dec) != 13:
            print("INVALID NUMBER - Must be 13 digits")
            dec = input("Enter a barcode number: ")

    # draw the barcode
    draw_barcode(length, width, dec, type)


if __name__ == "__main__":
    main()
