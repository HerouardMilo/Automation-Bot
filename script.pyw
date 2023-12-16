"""
File Organizer GUI Application

This script organizes files from a source folder into subfolders based on their extensions.

Author: Your Name
Date: YYYY-MM-DD
"""

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

def classify_and_copy_files(my_source_folder, my_destination_folder, my_success_label, my_progress_bar, my_root):
    """
    Classify and copy files from the source folder to the destination folder.

    Parameters:
        my_source_folder (str): Path to the source folder.
        my_destination_folder (str): Path to the destination folder.
        my_success_label (tk.Label): Label to display success message.
        my_progress_bar (ttk.Progressbar): Progress bar to show file processing progress.
        my_root (tk.Tk): Root window of the application.
    """
    if not os.path.exists(my_destination_folder):
        os.makedirs(my_destination_folder)

    total_files = sum(len(files) for _, _, files in os.walk(my_source_folder))
    my_progress_bar["max"] = total_files

    copied_files = []

    for folder_path, _, files in os.walk(my_source_folder):
        for filename in files:
            source_path = os.path.join(folder_path, filename)
            _, file_extension = os.path.splitext(filename)

            destination_path = determine_destination_path(file_extension, my_destination_folder)

            if not os.path.exists(destination_path):
                os.makedirs(destination_path)

            shutil.copy(source_path, os.path.join(destination_path, filename))
            copied_files.append(source_path)

            my_progress_bar["value"] += 1
            my_root.update_idletasks()

    remove_copied_files(copied_files, my_source_folder)

    my_success_label.config(text=f"Success! Files have been organized in {my_destination_folder}.")

def determine_destination_path(my_file_extension, my_destination_folder):
    """
    Determine the destination path based on the file extension.

    Parameters:
        my_file_extension (str): File extension to determine the destination path.
        my_destination_folder (str): Path to the destination folder.

    Returns:
        str: Destination path for the given file extension.
    """
    if my_file_extension in IMAGE_EXTENSIONS:
        return os.path.join(my_destination_folder, 'Images')
    elif my_file_extension in DOCUMENT_EXTENSIONS:
        return os.path.join(my_destination_folder, 'Documents')
    elif my_file_extension in VIDEO_EXTENSIONS:
        return os.path.join(my_destination_folder, 'Videos')
    else:
        return os.path.join(my_destination_folder, 'Other')

def remove_copied_files(my_copied_files, my_source_folder):
    """
    Remove copied files and subfolders from the source folder.

    Parameters:
        my_copied_files (list): List of paths to copied files.
        my_source_folder (str): Path to the source folder.
    """
    for file_path in my_copied_files:
        os.remove(file_path)
        print(f"File '{file_path}' deleted.")

    for subfolder in next(os.walk(my_source_folder))[1]:
        subfolder_path = os.path.join(my_source_folder, subfolder)
        shutil.rmtree(subfolder_path)
        print(f"Subfolder '{subfolder}' deleted from '{my_source_folder}'.")

def browse_button(my_entry_var):
    """
    Open a file dialog to select a folder and set the selected folder path to the entry variable.

    Parameters:
        my_entry_var (tk.StringVar): Entry variable to set the selected folder path.
    """
    folder_selected = filedialog.askdirectory()
    my_entry_var.set(folder_selected)

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

    start_button = ttk.Button(frame, text="Start", command=lambda: classify_and_copy_files(
        source_var.get(), destination_var.get(), success_label, progress_bar, root
    ))

    success_label = tk.Label(frame, text="", fg="green")

    progress_bar = ttk.Progressbar(frame, orient="horizontal", length=250, mode="determinate")

    source_entry.grid(row=0, column=0, padx=5, pady=5)
    source_button.grid(row=0, column=1, padx=5, pady=5)
    destination_entry.grid(row=1, column=0, padx=5, pady=5)
    destination_button.grid(row=1, column=1, padx=5, pady=5)

    start_button.grid(row=2, column=0, columnspan=4, pady=10)
    success_label.grid(row=3, column=0, columnspan=4, pady=5)
    progress_bar.grid(row=4, column=0, columnspan=4, pady=0)

    root.mainloop()
