import os
from pathlib import Path

SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIO": ['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}

def pickDirectory(value):
    for category, suffix in SUBDIRECTORIES.items():
        for item in suffix:
            if item == value:
                return category
    return "MISC"

def organizeFiles():
    for item in os.scandir():
        if item.is_dir():
            continue
        filePath = Path(item)
        filetype = filePath.suffix.lower()

        directory = pickDirectory(filetype)
        directoryPath = Path(directory)

        if not directoryPath.is_dir():
            directoryPath.mkdir()
        
        filePath.rename(directoryPath.joinpath(filePath))

organizeFiles()