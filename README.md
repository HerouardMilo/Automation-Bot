# Algorithme pour Classer et Copier des Fichiers

## Objectif
L'objectif de cet algorithme est de créer un bot qui automatise le processus de classification et de copie des fichiers du lecteur C: vers le lecteur D: afin d'optimiser l'espace de stockage et de maintenir les fichiers système propres et organisés.

## Étapes

1. **Définition des Extensions de Fichiers à Classer :**
   - Images : [.jpg, .jpeg, .png, .gif]
   - Documents : [.pdf, .docx, .xlsx, .txt]
   - Vidéos : [.mp4, .avi, .mkv]

2. **Création du Dossier de Destination :**
   - Vérifier si le dossier de destination existe.
   - S'il n'existe pas, le créer.

3. **Parcourir les Fichiers du Dossier Source :**
   - Pour chaque fichier dans le dossier source C:
     - Ignorer les dossiers.
     - Récupérer l'extension du fichier.

4. **Classer les Fichiers en Fonction de leur Extension :**
   - Si l'extension est dans les images, copier vers le dossier "Images".
   - Si l'extension est dans les documents, copier vers le dossier "Documents".
   - Si l'extension est dans les vidéos, copier vers le dossier "Vidéos".
   - Sinon, copier vers le dossier "Autres".

5. **Copier les Fichiers :**
   - Vérifier si le dossier de destination spécifique existe.
   - S'il n'existe pas, le créer.
   - Copier le fichier vers le dossier de destination.

6. **Afficher le Résultat :**
   - Afficher un message indiquant que le fichier a été copié avec succès.

## Exécution
- Spécifier les dossiers source et destination.
- Appeler la fonction pour classer et copier les fichiers.

Cet algorithme peut être adapté en fonction des besoins spécifiques de l'utilisateur en ajoutant d'autres critères de classification.
