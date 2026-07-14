from pathlib import Path
from parser import extract_resume_text
# parsing file
def choose_file():
    # take file from user
    # we use graphical file picker: tkinter
    import tkinter as tk
    from tkinter import filedialog

    # to prevent an empty tkinter window from   popping up we write:
    root=tk.Tk()
    root.withdraw()

    print("Opening file selector window...")

    file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=[("PDF file", "*.pdf"),("DOCX file","*.docx")]
    )
    return file_path




def main():
    # choosing file
    file_path = choose_file()
    resume_text = extract_resume_text(file_path)
    print(resume_text)


if __name__ == "__main__":
    main()
