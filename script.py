import os
import shutil
import tkinter as tk
from tkinter import filedialog

def classify_and_copy_files(source_folder, destination_folder, success_label):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    document_extensions = ['.pdf', '.docx', '.xlsx', '.txt']
    video_extensions = ['.mp4', '.avi', '.mkv']

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    copied_files = []

    for folder_path, _, files in os.walk(source_folder):
        for filename in files:
            source_path = os.path.join(folder_path, filename)

            _, file_extension = os.path.splitext(filename)

            if file_extension in image_extensions:
                destination_path = os.path.join(destination_folder, 'Images')
            elif file_extension in document_extensions:
                destination_path = os.path.join(destination_folder, 'Documents')
            elif file_extension in video_extensions:
                destination_path = os.path.join(destination_folder, 'Videos')
            else:
                destination_path = os.path.join(destination_folder, 'Other')

            if not os.path.exists(destination_path):
                os.makedirs(destination_path)

            shutil.copy(source_path, os.path.join(destination_path, filename))
            copied_files.append(source_path)
            print(f"File '{filename}' copied to {destination_path}")

    for file_path in copied_files:
        os.remove(file_path)
        print(f"File '{file_path}' deleted.")

    for subfolder in next(os.walk(source_folder))[1]:
        subfolder_path = os.path.join(source_folder, subfolder)
        shutil.rmtree(subfolder_path)
        print(f"Subfolder '{subfolder}' deleted from '{source_folder}'.")

    success_label.config(text=f"Success! Files have been organized in {destination_folder}.")

def browse_button(entry_var):
    folder_selected = filedialog.askdirectory()
    entry_var.set(folder_selected)

if __name__ == "__main__":

    root = tk.Tk()
    root.title("File Organizer")

    source_var = tk.StringVar()
    destination_var = tk.StringVar()

    source_entry = tk.Entry(root, textvariable=source_var, state='readonly')
    destination_entry = tk.Entry(root, textvariable=destination_var, state='readonly')

    source_button = tk.Button(root, text="Browse Source", command=lambda: browse_button(source_var))
    destination_button = tk.Button(root, text="Browse Destination", command=lambda: browse_button(destination_var))

    start_button = tk.Button(root, text="Start", command=lambda: classify_and_copy_files(source_var.get(), destination_var.get(), success_label))

    success_label = tk.Label(root, text="", fg="green")

    source_entry.grid(row=0, column=0, padx=5, pady=5, columnspan=2)
    source_button.grid(row=0, column=2, padx=5, pady=5)

    destination_entry.grid(row=1, column=0, padx=5, pady=5, columnspan=2)
    destination_button.grid(row=1, column=2, padx=5, pady=5)

    start_button.grid(row=2, column=0, columnspan=3, pady=10)

    success_label.grid(row=3, column=0, columnspan=3)

    root.mainloop()