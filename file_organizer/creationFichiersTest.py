import os

def create_file(file_path):
    try:
        with open(file_path, 'x'):
            pass
        print(f'The file {file_path} has been created successfully!')
    except FileExistsError:
        print(f'The file {file_path} already exists. Skipping creation.')
    except OSError as e:
        print(f"Error creating file {file_path} - {e.strerror}")

if __name__ == "__main__":
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    document_extensions = ['.pdf', '.docx', '.xlsx', '.txt']
    video_extensions = ['.mp4', '.avi', '.mkv']

    base_directory = "testOrigine"
    os.makedirs(base_directory, exist_ok=True)

    all_extensions = image_extensions + document_extensions + video_extensions

    for extension in all_extensions:
        extension_directory = os.path.join(base_directory, extension[1:])
        os.makedirs(extension_directory, exist_ok=True)

        file_name = f'sample{extension}'
        file_path = os.path.join(extension_directory, file_name)
        create_file(file_path)

        file_name_outside = f'sample_outside{extension}'
        file_path_outside = os.path.join(base_directory, file_name_outside)
        create_file(file_path_outside)