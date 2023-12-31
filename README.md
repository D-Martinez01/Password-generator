﻿
# Password Generator

The "Password Generator" program is a graphical user interface (GUI) application built with Tkinter in Python.
The application allows users to generate secure passwords with various language and character set options, including
English, Russian, Japanese (Hiragana and Katakana), numbers, and punctuation.
Users can customize the password length and selectively include or exclude character sets.

## Features

- Intuitive GUI for easy interaction.
- Customizable password settings, including length and character sets.
- Visual representation of selected character sets with color-coded checkboxes.
- Generated passwords are displayed in a treeview for easy reference.
- Users can copy individual passwords to the clipboard.
- Export functionality to save generated passwords to a text file.
- About window providing information about the generator, its version, and credits.

# Run Locally

- Create and activate virtual environment
  ```bash
  python -m venv venv
  venv\Scripts\activate.bat
  ```

- Clone the project
  ```bash
  git clone https://github.com/D-Martinez01/Password-generator.git
  ```

- Navigate to the project directory
  ```bash
  cd your_project_directory
  ```

- Install requirements
  ```bash
  pip install -r requirements.txt
  ```

- Run the program
  ```bash
  python main.py
  ```
