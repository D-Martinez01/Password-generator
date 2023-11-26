from tkinter import Tk
from gui import PasswordGeneratorGUI


def main():
    root = Tk()
    root.iconbitmap('cyber-security.ico')
    PasswordGeneratorGUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
