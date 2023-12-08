import os

if __name__ == "__main__":
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    document_extensions = ['.pdf', '.docx', '.xlsx', '.txt']
    video_extensions = ['.mp4', '.avi', '.mkv']

    base_directory = 'testOrigine'

    if not os.path.exists(base_directory):
        os.maledirs(base_directory)

    all_extensions =image_extensions + document_extensions + video_extensions

    for extension in all_extensions:
        file_name = f'sample{extension}'
        file_path = os.path.join(base_directory, file_name)

        try:
            with open(file_path, 'w') as file:
                pass
            print(f'The file {file_path} has been created successfully !')
        except OSError as e:
            print(f"Error opening: {file_path} - {e.strerror}")