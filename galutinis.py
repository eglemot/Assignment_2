from tkinter import *
from mygtukai.main_window import PagrindinisLangas

def paleisti():
    root = Tk()
    root.title("PROJEKTŲ VALDYMAS")
    root.geometry("200x500")
    app = PagrindinisLangas(root)
    root.mainloop()

if __name__ == "__main__":
    paleisti()