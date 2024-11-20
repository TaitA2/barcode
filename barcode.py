import turtle
import time

# create Turtle object to draw lines with
pen = turtle.Turtle()
# increase drawing speed
pen.speed("fastest")
# orientate pen to draw vertically instead of horizontally
pen.right(90)

# Dictionary for converting decimal numbers to barcode binary
codes = {
    "0": "0001101",
    "1": "0011001",
    "2": "0010011",
    "3": "0111101",
    "4": "0100011",
    "5": "0110001",
    "6": "0101111",
    "7": "0111011",
    "8": "0110111",
    "9": "0001011"
}

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
def convert(dec):
    # declare empty string for binary 
    bin = ""
    # declare border and center values for
    border = "101"
    center = "01010"
    # add left border lines to start of barcode
    bin += border
    # converts to binary according to 'codes' dictionary
    i = 0
    while i < len(dec) // 2:
        bin += codes[dec[i]]
        i += 1
    # add center lines to center of barcode
    bin += center
    # converts to binary according to the inversion of the 'codes' dictionary
    while i < len(dec):
        temp = codes[dec[i]]
        # swaps every 1 with 0 and 0 with 1
        for bit in temp:
            bin += str(1 - int(bit))
        i += 1
    # add right border lines to end of barcode
    bin += border
    # return resulting binary
    return bin

# function to draw barcode
def draw_barcode(length, width, dec):
    bin = convert(dec)
    for digit in bin:
        if digit == "1":
            draw_line(length, width)
        elif digit == "0":
            skip_line(width)
        else:
            raise Exception("Invalid binary")

def main():
    # set length of bar code lines
    length = 300
    # set width of bar code lines
    width = 5
    # set decimal value to be converted
    dec = "51000012517"
    if len(dec) < 12:
        dec = "0" * (12 - len(dec)) + dec
    print(dec)
    draw_barcode(length, width, dec)

    # leave time to view result
    time.sleep(60)

if __name__ == "__main__":
    main()
