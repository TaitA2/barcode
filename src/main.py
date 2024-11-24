from utils import *


def main():

    # set barcode type
    type = get_type()

    # set decimal value to be converted
    num = get_num(type)

    # draw the barcode
    draw_barcode(num, type)


# call main function
if __name__ == "__main__":
    main()
