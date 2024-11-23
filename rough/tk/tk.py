import tkinter

root = tkinter.Tk()

root.title("Barcode Generator")

label = tkinter.Label(root, text="BARCODE NUMBER")
label.pack()

canvas = tkinter.Canvas(root, width=400, height=300)
canvas.pack()

bin = "111111111111"

i = 0
while i < len(bin):
    if bin[i] == "1":
        for _ in range(3):
            canvas.create_line(40 + i, 40, 40 + i, 200)

    i += 1
# canvas.create_line(40, 40, 40, 200)

# canvas.create_line(42, 40, 42, 200)

# canvas.create_line(80, 40, 80, 200)

root.mainloop()
