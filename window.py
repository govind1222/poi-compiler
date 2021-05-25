from tkinter import Tk, Button

window = Tk()

# defining constants
SCREEN_WIDTH = window.winfo_screenwidth()
SCREEN_HEIGHT = window.winfo_screenheight()
WINDOW_WIDTH = window.winfo_reqwidth()  # int(SCREEN_WIDTH * .8)
WINDOW_HEIGHT = window.winfo_reqheight()  # int(SCREEN_HEIGHT * .8)

# setting window size to be 80% the size of the screen
window.eval('tk::PlaceWindow . center')


nextBtn = Button(
    window,
    text="Next",
    width=int(0.05 * WINDOW_WIDTH),
    height=int(0.01 * WINDOW_HEIGHT)
)

nextBtn.pack()
window.mainloop()
