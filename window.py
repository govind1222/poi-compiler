from tkinter import Tk, Button, Frame, filedialog, LEFT, RIGHT
from PIL import Image, ImageTk

window = Tk()

# defining constants
SCREEN_WIDTH = window.winfo_screenwidth()
WINDOW_WIDTH = window.winfo_reqwidth()  # int(SCREEN_WIDTH * .8)
SCREEN_HEIGHT = window.winfo_screenheight()
WINDOW_HEIGHT = window.winfo_reqheight()  # int(SCREEN_HEIGHT * .8)

# global variables
selectedDirectory = None
currentImage = 0


def advanceImage():
    if not selectedDirectory:
        return
    else:
        print("next")


def prevImage():
    if not selectedDirectory:
        return
    else:
        print("prev")


def chooseDirectory():
    global selectedDirectory
    selectedDirectory = filedialog.askdirectory()


def main():

    # setting window size to be 80% the size of the screen
    window.eval('tk::PlaceWindow . center')

    image_frame = Frame(master=window, width=int(0.8 * WINDOW_WIDTH))
    button_frame = Frame(master=window, width=int(0.2 * WINDOW_WIDTH))

    nextBtn = Button(
        master=button_frame,
        text="Next",
        width=int(0.07 * WINDOW_WIDTH),
        height=int(0.01 * WINDOW_HEIGHT),
        command=advanceImage
    )
    nextBtn.pack()

    prevBtn = Button(
        master=button_frame,
        text="Previous",
        width=int(0.07 * WINDOW_WIDTH),
        height=int(0.01 * WINDOW_HEIGHT),
        command=prevImage
    )
    prevBtn.pack()

    dirBtn = Button(
        master=button_frame,
        text="Choose directory",
        width=int(0.07 * WINDOW_WIDTH),
        height=int(0.01 * WINDOW_HEIGHT),
        command=chooseDirectory
    )
    dirBtn.pack()

    image_frame.pack(side=LEFT)
    button_frame.pack(side=RIGHT)

    window.mainloop()


if __name__ == "__main__":
    main()
