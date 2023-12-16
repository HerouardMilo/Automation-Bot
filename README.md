# File Organizer

## Overview

The File Organizer is a Python script with a graphical user interface (GUI) built using Tkinter. This script automates the organization of files from a source directory into different destination folders based on their file extensions.

## Features

- Browse for source and destination folders using a GUI interface.
- Classify files into specific folders based on their extensions.
- Copy files to the destination folders.
- Delete the copied files from the source folder.
- Display a success message after organizing the files.

## How to Use

1. Run the script (`script.pyw`).
2. Use the "Browse Source" button to select the source folder.
3. Use the "Browse Destination" button to select the destination folder.
4. Click the "Start" button to initiate the file organization process.

## File Classification

- **Images:** `.jpg`, `.jpeg`, `.png`, `.gif`
- **Documents:** `.pdf`, `.docx`, `.xlsx`, `.txt`
- **Videos:** `.mp4`, `.avi`, `.mkv`
- **Other:** Files with extensions not covered in the above categories.

## Example

Suppose you have files in a folder named `DataProject`:

- `D:/DataProject/testOrigine/sample.jpg`
- `D:/DataProject/testOrigine/sample.docx`
- ...

After running the script:

- Images will be copied to `D:/DataProject/testDestination/Images`.
- Documents will be copied to `D:/DataProject/testDestination/Documents`.
- Videos will be copied to `D:/DataProject/testDestination/Videos`.
- Other files will be copied to `D:/DataProject/testDestination/Other`.

## Notes

- Files are deleted from the source folder after being copied.
- The success message will be displayed once the process is complete.

## Dependencies

Run the Makefile to install all the required libraries :
1. Python 3.x
2. Tkinter (Included in the standard Python distribution)

Feel free to use and modify the script according to your needs!

## Technical Details

Let's take a closer look at specific sections of the code:

```python
# Import necessary libraries
import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

# Define GUI dimensions
GUI_WIDTH = 300
GUI_HEIGHT = 250
```

In this section, we import the required libraries (`os`, `shutil`, `tkinter`) and define the dimensions for the graphical user interface.

```python
def classify_and_copy_files(source_folder, destination_folder, success_label, progress_bar):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    total_files = sum(len(files) for _, _, files in os.walk(source_folder))
    progress_bar["max"] = total_files

    copied_files = []

    # Iterate through files in the source folder
    for folder_path, _, files in os.walk(source_folder):
        for filename in files:
            source_path = os.path.join(folder_path, filename)
            _, file_extension = os.path.splitext(filename)

            destination_path = determine_destination_path(file_extension, destination_folder)

            if not os.path.exists(destination_path):
                os.makedirs(destination_path)

            # Copy files to the destination folders
            shutil.copy(source_path, os.path.join(destination_path, filename))
            copied_files.append(source_path)

            # Update progress bar
            progress_bar["value"] += 1
            root.update_idletasks()

    # Remove copied files and subfolders from the source
    remove_copied_files(copied_files, source_folder)

    # Display success message
    success_label.config(text=f"Success! Files have been organized in {destination_folder}.")
```

Here, the `classify_and_copy_files` function performs the main file organization. It iterates through files, copies them based on their extensions, updates the progress bar, removes copied files, and updates the success label.

```python
def browse_button(entry_var):
    # Open a dialog for selecting a directory and set the selected path to the provided entry variable
    folder_selected = filedialog.askdirectory()
    entry_var.set(folder_selected)
```

The `browse_button` function opens a dialog for selecting a directory and sets the selected path to the provided entry variable.

```python
if __name__ == "__main__":
    # Create the main Tkinter window
    root = tk.Tk()
    root.title("File Organizer")
    root.geometry(f"{GUI_WIDTH}x{GUI_HEIGHT}")

    frame = ttk.Frame(root)
    frame.pack(expand=True)

    # Define Tkinter StringVars for source and destination directories
    source_var = tk.StringVar()
    destination_var = tk.StringVar()

    # Create Entry widgets for displaying source and destination paths
    source_entry = ttk.Entry(frame, textvariable=source_var, state='readonly')
    destination_entry = ttk.Entry(frame, textvariable=destination_var, state='readonly')

    # Create buttons for browsing source and destination directories
    source_button = ttk.Button(frame, text="Browse Source", command=lambda: browse_button(source_var))
    destination_button = ttk.Button(frame, text="Browse Destination", command=lambda: browse_button(destination_var))

    # Create Start button for initiating the file organization process
    start_button = ttk.Button(frame, text="Start", command=lambda: classify_and_copy_files(source_var.get(), destination_var.get(), success_label, progress_bar))

    # Create label for displaying success messages
    success_label = tk.Label(frame, text="", fg="green")

    # Create progress bar for visualizing the file organization progress
    progress_bar = ttk.Progressbar(frame, orient="horizontal", length=250, mode="determinate")
