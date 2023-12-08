import os
import shutil

def classify_and_copy_files(source_folder, destination_folder):
    # Liste des extensions de fichiers à classer
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    document_extensions = ['.pdf', '.docx', '.xlsx', '.txt']
    video_extensions = ['.mp4', '.avi', '.mkv']

    # Vérifier et créer le dossier de destination s'il n'existe pas
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Parcourir tous les fichiers du dossier source
    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)

        # Ignorer les dossiers
        if os.path.isdir(source_path):
            continue

        # Déterminer l'extension du fichier
        _, file_extension = os.path.splitext(filename)

        # Classer les fichiers en fonction de leur extension
        if file_extension in image_extensions:
            destination_path = os.path.join(destination_folder, 'Images')
        elif file_extension in document_extensions:
            destination_path = os.path.join(destination_folder, 'Documents')
        elif file_extension in video_extensions:
            destination_path = os.path.join(destination_folder, 'Videos')
        else:
            destination_path = os.path.join(destination_folder, 'Other')

        # Vérifier et créer le dossier de destination spécifique s'il n'existe pas
        if not os.path.exists(destination_path):
            os.makedirs(destination_path)

        # Copier le fichier vers le dossier de destination
        shutil.copy(source_path, os.path.join(destination_path, filename))
        print(f"File '{filename}' copied to {destination_path}")

if __name__ == "__main__":
    # Spécifier les dossiers source et destination
    source_folder = 'C:\\'
    destination_folder = 'D:\\OrganizedFiles'

    # Appeler la fonction pour classer et copier les fichiers
    classify_and_copy_files(source_folder, destination_folder)
