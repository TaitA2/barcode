# import dictionaries for binary_dicts file
from dicts import *
import tkinter


# initialize tkinter object for drawing barcode
def init(num):
    root = tkinter.Tk()

    root.title("Barcode Generator")

    canvas = tkinter.Canvas(root, width=365, height=250)
    canvas.pack()

    label = tkinter.Label(root, text=num)
    label.pack()

    return root, canvas


# function to convert decimal numbers to their barcode binary conterpart
def convert(num, type_dict):
    # declare empty string for binary
    bin = ""
    # declare border and center values for
    border = "101"
    center = "01010"
    # add left border lines to start of barcode
    bin += border
    # converts to binary according to appropriate dictionary
    i = 0
    while i < len(num) // 2:
        bin += type_dict[num[i]]
        i += 1
    # add center lines to center of barcode
    bin += center
    # converts to binary according to the inversion of the appropriate dictionary
    while i < len(num):
        temp = type_dict[num[i]]
        # swaps every 1 with 0 and 0 with 1
        for bit in temp:
            bin += str(1 - int(bit))
        i += 1
    # add right border lines to end of barcode
    bin += border
    # return resulting binary
    return bin


# function to draw barcode
def draw_barcode(num, type_dict, length=200, width=3):
    root, canvas = init(num)
    bin = convert(num, type_dict)
    i = x = 0
    while i < len(bin):
        if bin[i] == "1":
            canvas.create_rectangle(40 + x, 40, 40 + x + width, length, fill="black")

        x += width
        i += 1

    # do the thing
    root.mainloop()


# function to get barcode type
def get_type():
    type = input("Enter a barcode type(UPC / EAN): ").lower()
    while type not in ["upc", "ean"]:
        type = input("Enter a barcode type(UPC / EAN): ").lower()
    if type == "upc":
        type = upc
    elif type == "ean":
        type = ean
    return type


# function to get barcode number
def get_num(type):
    # get number to convert to barcode from user input
    num = input("Enter a barcode number: ")
    # ensure valid barcode number
    while (not num.isnumeric()) or len(num) != type["length"]:
        print(f"INVALID NUMBER - Must be {type['length']} digits")
        num = input("Enter a barcode number: ")
    # return
    return num
