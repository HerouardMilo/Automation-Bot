import os

if __name__ == "__main__":
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    document_extensions = ['.pdf', '.docx', '.xlsx', '.txt']
    video_extensions = ['.mp4', '.avi', '.mkv']

    all_extensions =image_extensions + document_extensions + video_extensions

    for extension in all_extensions:
        file_path =f'{extension}.{extension}'

        try:
            with open(file_path, 'w') as file:
                pass
            print(f'The file {file_path} has been created successfully !')
        except OSError as e:
            print(f"Error opening: {file_path} - {e.strerror}")