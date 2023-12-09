import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

GUI_WIDTH = 300
GUI_HEIGHT = 250

IMAGE_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif']
DOCUMENT_EXTENSIONS = ['.pdf', '.docx', '.xlsx', '.txt']
VIDEO_EXTENSIONS = ['.mp4', '.avi', '.mkv']

def classify_and_copy_files(source_folder, destination_folder, success_label, progress_bar):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    total_files = sum(len(files) for _, _, files in os.walk(source_folder))
    progress_bar["max"] = total_files

    copied_files = []

    for folder_path, _, files in os.walk(source_folder):
        for filename in files:
            source_path = os.path.join(folder_path, filename)
            _, file_extension = os.path.splitext(filename)

            destination_path = determine_destination_path(file_extension, destination_folder)

            if not os.path.exists(destination_path):
                os.makedirs(destination_path)

            shutil.copy(source_path, os.path.join(destination_path, filename))
            copied_files.append(source_path)

            progress_bar["value"] += 1
            root.update_idletasks()

    remove_copied_files(copied_files, source_folder)

    success_label.config(text=f"Success! Files have been organized in {destination_folder}.")

def determine_destination_path(file_extension, destination_folder):
    if file_extension in IMAGE_EXTENSIONS:
        return os.path.join(destination_folder, 'Images')
    elif file_extension in DOCUMENT_EXTENSIONS:
        return os.path.join(destination_folder, 'Documents')
    elif file_extension in VIDEO_EXTENSIONS:
        return os.path.join(destination_folder, 'Videos')
    else:
        return os.path.join(destination_folder, 'Other')

def remove_copied_files(copied_files,source_folder):
    for file_path in copied_files:
        os.remove(file_path)
        print(f"File '{file_path}' deleted.")

    for subfolder in next(os.walk(source_folder))[1]:
        subfolder_path = os.path.join(source_folder, subfolder)
        shutil.rmtree(subfolder_path)
        print(f"Subfolder '{subfolder}' deleted from '{source_folder}'.")

def browse_button(entry_var):
    folder_selected = filedialog.askdirectory()
    entry_var.set(folder_selected)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("File Organizer")
    root.geometry(f"{GUI_WIDTH}x{GUI_HEIGHT}")

    frame = ttk.Frame(root)
    frame.pack(expand=True)

    source_var = tk.StringVar()
    destination_var = tk.StringVar()

    source_entry = ttk.Entry(frame, textvariable=source_var, state='readonly')
    destination_entry = ttk.Entry(frame, textvariable=destination_var, state='readonly')

    source_button = ttk.Button(frame, text="Browse Source", command=lambda: browse_button(source_var))
    destination_button = ttk.Button(frame, text="Browse Destination", command=lambda: browse_button(destination_var))

    start_button = ttk.Button(frame, text="Start", command=lambda: classify_and_copy_files(source_var.get(), destination_var.get(), success_label, progress_bar))
    progress_bar = ttk.Progressbar(frame, orient="horizontal", length=250, mode="determinate")
    success_label = tk.Label(frame, text="", fg="green")

    source_entry.grid(row=0, column=0, padx=5, pady=5)
    source_button.grid(row=0, column=1, padx=5, pady=5)
    destination_entry.grid(row=1, column=0, padx=5, pady=5)
    destination_button.grid(row=1, column=1, padx=5, pady=5)

    start_button.grid(row=2, column=0, columnspan=4, pady=10)
    success_label.grid(row=3, column=0, columnspan=4, pady=5)
    progress_bar.grid(row=4, column=0, columnspan=4, pady=0)

    root.mainloop()