from tkinter import *


def title_screen():
    # Turn background to global to avoid Python garbage collector
    global background

    # Create object
    splash_root = Tk()

    # Window size
    splash_root.geometry("1280x720")

    # Top bar label
    splash_root.title("Dungeons & Wagons")

    # Background image definition
    background = PhotoImage(file="images/splash_screen.png")

    # Canvas overlay object
    splash_canvas = Canvas(splash_root, width=1280, height=720)
    splash_canvas.pack(fill="both", expand=True)

    # Background image placement on canvas
    splash_canvas.create_image(0, 0, image=background, anchor="nw")

    # Title

    splash_canvas.create_text(640, 50, text="Dungeons & Wagons", font=("Courier New", 40), fill="white")

    # Menu buttons
    exit_button = Button(splash_root, text="EXIT", font=("Courier New", 10))
    play_button = Button(splash_root, text="PLAY", font=("Courier New", 10))

    exit_button_window = splash_canvas.create_window(10, 10, anchor="nw", window=exit_button)
    play_button_window = splash_canvas.create_window(65, 10, anchor="nw", window=play_button)


title_screen()

mainloop()
