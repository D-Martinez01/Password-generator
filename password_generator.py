from random import choice
from tkinter import filedialog, messagebox
import settings
from about_window import AboutWindow


class PasswordGenerator:
    def __init__(self):
        self.selected_alphabet = ''

    def generate_password(self, length, use_english, use_russian, use_japanese_hiragana, use_japanese_katakana,
                          use_numbers, use_punctuation):

        self.selected_alphabet = ''

        if use_english:
            self.selected_alphabet += settings.ENGLISH_ALPHABET
        if use_russian:
            self.selected_alphabet += settings.RUSSIAN_ALPHABET + settings.RUSSIAN_ALPHABET.upper()
        if use_japanese_hiragana:
            self.selected_alphabet += settings.JAPANESE_HIRAGANA
        if use_japanese_katakana:
            self.selected_alphabet += settings.JAPANESE_KATAKANA
        if use_numbers:
            self.selected_alphabet += settings.NUMBERS
        if use_punctuation:
            self.selected_alphabet += settings.PUNCTUATION

        if not self.selected_alphabet:
            warning_message = 'No language or character set selected.'
            messagebox.showwarning('Warning', warning_message)
            return None

        password = ''.join(choice(self.selected_alphabet) for _ in range(length))
        return password

    def generate_password_and_update_tree(self, tree, password_length, check_vars):
        try:
            password_length = int(password_length)
        except ValueError:
            warning_message = 'Invalid password length.\nPassword length cannot be empty or equal 0.'
            messagebox.showwarning('Warning', warning_message)
            return

        use_english = bool(check_vars[0].get())
        use_russian = bool(check_vars[1].get())
        use_japanese_hiragana = bool(check_vars[2].get())
        use_japanese_katakana = bool(check_vars[3].get())
        use_numbers = bool(check_vars[4].get())
        use_punctuation = bool(check_vars[5].get())

        generated_password = self.generate_password(password_length, use_english, use_russian,
                                                    use_japanese_hiragana, use_japanese_katakana,
                                                    use_numbers,
                                                    use_punctuation)

        if generated_password is not None:
            tree.insert('', 'end', values=(len(tree.get_children()) + 1, generated_password))

    @staticmethod
    def copy_password(tree, root):
        selected_item = tree.selection()
        if selected_item:
            item = selected_item[0]
            root.clipboard_clear()
            root.clipboard_append(tree.item(item, 'values')[1])

            info_message = "Password copied successfully"
            messagebox.showinfo("Information", info_message)
        else:
            warning_message = 'Choose a password before copying'
            messagebox.showwarning('Warning', warning_message)

    @staticmethod
    def delete_columns(tree):
        confirmation = messagebox.askyesno('Question', 'Are you sure you want to delete the generated entries?')
        for item in tree.get_children():
            if confirmation:
                tree.delete(item)

    @staticmethod
    def export_generated_password(tree):
        # Ask the user to choose the file location and name
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"),
                                                            ("All files", "*.*")],
                                                 title="Save generated passwords",
                                                 initialfile="generated_passwords.txt")

        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as file:
                    # Write header
                    file.write("Generated Passwords:\n\n")

                    # Write each generated password to the file
                    for child in tree.get_children():
                        values = tree.item(child, 'values')
                        password_id, generated_password = values[0], values[1]
                        file.write(f"{password_id}. {generated_password}\n")

                messagebox.showinfo("Information", "Generated passwords exported successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Error exporting passwords: {str(e)}")

    @staticmethod
    def open_new_window(root):
        AboutWindow(root)
