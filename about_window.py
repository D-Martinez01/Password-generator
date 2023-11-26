from tkinter import Toplevel, Label, Button, Frame
from PIL import ImageTk, Image
import webbrowser


def callback(url):
    webbrowser.open_new(url)


class AboutWindow:
    def __init__(self, parent):
        self.parent = parent
        self.about_window = Toplevel(self.parent)
        self.about_window.title("About")
        self.about_window.iconbitmap('cyber-security.ico')
        self.about_window.geometry("250x220")
        self.about_window.resizable(False, False)

        generator_version = Label(self.about_window, text='Password generator 0.1')

        img_frame = Frame(self.about_window)

        generator_img = Image.open("cyber-security.png")
        resize_image = generator_img.resize((100, 100))
        img = ImageTk.PhotoImage(resize_image)

        show_img = Label(img_frame, image=img)
        show_img.image = img

        made_by = Label(self.about_window, text="Made by David")

        github_web = Label(self.about_window, text='Github', fg='blue', cursor='hand2')
        github_web.bind('<Button-1>', lambda e: callback('https://github.com/D-Martinez01'))

        script_engine = Label(self.about_window, text="Script engine powered by Python")

        special_thanks = Label(self.about_window, text="Special thanks to:\n Code Academy ")

        close_button = Button(self.about_window, text="OK", command=self.about_window.destroy)

        # Arrangement
        generator_version.grid(row=0, column=0, sticky='w')
        img_frame.grid(row=1, column=0, rowspan=3, sticky='w')
        show_img.grid(row=0, column=0, sticky='w')
        made_by.grid(row=1, column=1, sticky='nsew')
        github_web.grid(row=2, column=1, sticky='w')
        script_engine.grid(row=4, column=0, columnspan=2, sticky='nsew')
        special_thanks.grid(row=5, column=0, columnspan=2, sticky='nsew')
        close_button.grid(row=6, column=0, columnspan=2, sticky='n')
