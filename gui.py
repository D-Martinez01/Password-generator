from tkinter import ttk, IntVar, Label, Frame, Checkbutton, Entry, Button, CENTER, Menu
from password_generator import PasswordGenerator


def change_select_color(var, check_button):
    if var.get() == 0:
        check_button.config(selectcolor='red')
    else:
        check_button.config(selectcolor='green')


class PasswordGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.geometry('600x500')
        self.root.resizable(False, False)
        self.root.title('Password Generator')

        self.check_vars = [IntVar() for _ in range(6)]
        self.password_generator = PasswordGenerator()

        menu_bar = Menu(root)
        root.config(menu=menu_bar)
        menu_bar.add_command(label="About", command=self.open_about_window)

        label_select_language = Label(root, text='Select Language', font=('Arial', 11, 'bold'))

        separator = ttk.Separator(root, orient='horizontal')

        characters_frame = Frame()

        self.english_check = Checkbutton(characters_frame, text='English', variable=self.check_vars[0],
                                         onvalue=True, offvalue=False,
                                         selectcolor='red', font=("Arial", 11),
                                         command=lambda: change_select_color(self.check_vars[0],
                                                                             self.english_check)
                                         )

        self.russian_check = Checkbutton(characters_frame, text='Russian', variable=self.check_vars[1],
                                         onvalue=True, offvalue=False,
                                         selectcolor='red', font=("Arial", 11),
                                         command=lambda: change_select_color(self.check_vars[1],
                                                                             self.russian_check)
                                         )

        self.japanese_h_check = Checkbutton(characters_frame, text='Japanese\n Hiragana', variable=self.check_vars[2],
                                            onvalue=True, offvalue=False,
                                            selectcolor='red', font=("Arial", 11),
                                            command=lambda: change_select_color(self.check_vars[2],
                                                                                self.japanese_h_check)
                                            )

        self.japanese_k_check = Checkbutton(characters_frame, text='Japanese\n Katakana', variable=self.check_vars[3],
                                            onvalue=True, offvalue=False,
                                            selectcolor='red', font=("Arial", 11),
                                            command=lambda: change_select_color(self.check_vars[3],
                                                                                self.japanese_k_check)
                                            )

        self.number_check = Checkbutton(characters_frame, text='Numbers', variable=self.check_vars[4],
                                        onvalue=True, offvalue=False,
                                        selectcolor='red', font=("Arial", 11),
                                        command=lambda: change_select_color(self.check_vars[4], self.number_check)
                                        )

        self.punctuation_check = Checkbutton(characters_frame, text='Punctuations', variable=self.check_vars[5],
                                             onvalue=True, offvalue=False,
                                             selectcolor='red', font=("Arial", 11),
                                             command=lambda: change_select_color(self.check_vars[5],
                                                                                 self.punctuation_check)
                                             )

        password_length_frame = Frame(root)

        password_length_label = Label(password_length_frame, text='Password Length:', font=("Arial", 11))

        validation = root.register(lambda char, entry_value: self.validate_integer(char, entry_value))
        self.password_length_entry = Entry(password_length_frame, width=3, validate="key",
                                           validatecommand=(validation, '%S', '%P'))

        separator2 = ttk.Separator(root, orient='horizontal')

        generate_button = Button(root, text="GENERATE PASSWORD",
                                 font=("Arial", 11, 'bold'),
                                 command=self.generate_password_and_update_tree
                                 )

        password_copy = Button(root, text='Copy password', font=("Arial", 11),
                               command=self.copy_selected_item)
        delete_generated = Button(root, text='Delete generated passwords', font=("Arial", 11),
                                  command=self.delete_generated_entries)
        export_password = Button(root, text='Export passwords', font=("Arial", 11),
                                 command=self.export_generates_password)

        style = ttk.Style()
        style.theme_use('clam')

        self.tree = ttk.Treeview(root, columns=('c1', 'c2'), show='headings', height=5)

        self.tree.column("c1", anchor=CENTER)
        self.tree.heading("c1", text="ID")
        self.tree.column("c2", anchor=CENTER)
        self.tree.heading("c2", text="Generated password")

        for i in range(3):
            root.columnconfigure(i, weight=1)

        # Arrangement
        label_select_language.grid(row=1, column=0, columnspan=3, sticky='nsew', padx=30, pady=10)
        separator.grid(row=2, column=0, columnspan=3, sticky='nsew')
        characters_frame.grid(row=3, column=2, columnspan=2, sticky='w')

        self.english_check.grid(row=3, column=2, sticky='w')
        self.russian_check.grid(row=4, column=2, sticky='w')
        self.japanese_h_check.grid(row=5, column=2, sticky='w')
        self.japanese_k_check.grid(row=6, column=2, sticky='w')
        self.number_check.grid(row=3, column=3, sticky='w')
        self.punctuation_check.grid(row=4, column=3, sticky='w')

        password_length_frame.grid(row=3, column=0, columnspan=2, sticky='w', padx=(10, 0))
        password_length_label.grid(row=1, column=0, sticky='w')
        self.password_length_entry.grid(row=1, column=1, sticky='w', padx=(0, 10))

        separator2.grid(row=7, column=0, columnspan=3, sticky='nsew')

        generate_button.grid(row=8, column=0, columnspan=3, sticky='nsew', padx=30, pady=10)
        self.tree.grid(row=9, column=0, columnspan=3, sticky='nsew', padx=30, pady=10)

        password_copy.grid(row=10, column=0, sticky='e')
        export_password.grid(row=10, column=1, sticky='n')
        delete_generated.grid(row=10, column=2, sticky='w')

    @staticmethod
    def validate_integer(char, entry_value):
        if entry_value == '':
            return True
        return char.isdigit() and len(entry_value) <= 3 and int(entry_value) != 0 or char == ""

    def generate_password_and_update_tree(self):
        password_length = self.password_length_entry.get()
        self.password_generator.generate_password_and_update_tree(self.tree, password_length, self.check_vars)

    def delete_generated_entries(self):
        self.password_generator.delete_columns(self.tree)

    def copy_selected_item(self):
        self.password_generator.copy_password(self.tree, self.root)

    def export_generates_password(self):
        self.password_generator.export_generated_password(self.tree)

    def open_about_window(self):
        self.password_generator.open_new_window(self.root)
