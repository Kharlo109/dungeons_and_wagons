from tkinter import *


def title_screen():

    global bg

    # Create object
    splash_root = Tk()

    # Window size
    splash_root.geometry("1280x720")

    # Top bar label
    splash_root.title("Dungeons & Wagons")

    # Title

    bg = PhotoImage(file="images/1.png")
    my_picture = Label(splash_root, image=bg)
    my_picture.place(x=0, y=0, relwidth=1, relheight=1)


title_screen()

mainloop()
