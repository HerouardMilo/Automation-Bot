# File Organizer

## Overview

The File Organizer is a simple Python script with a graphical user interface (GUI) built using Tkinter. This script helps organize files from a source directory into different destination folders based on their file extensions.

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

- Python 3.x
- Tkinter (Included in standard Python distribution)

Feel free to use and modify the script according to your needs!

# File Organizer

## Overview

The File Organizer is a simple Python script with a graphical user interface (GUI) built using Tkinter. This script helps organize files from a source directory into different destination folders based on their file extensions.

## Features

- Browse for source and destination folders using a GUI interface.
- Classify files into specific folders based on their extensions.
- Copy files to the destination folders.
- Delete the copied files from the source folder.
- Display a success message after organizing the files.

## How to Use

1. Run the script (`script.py`).
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

- Python 3.x
- Tkinter (Included in standard Python distribution)

Feel free to use and modify the script according to your needs!