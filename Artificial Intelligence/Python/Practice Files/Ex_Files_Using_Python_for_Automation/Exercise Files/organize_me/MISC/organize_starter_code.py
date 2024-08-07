import os
from pathlib import Path

SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIOS": ['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}

def pickDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        print(f'{category} {suffixes}')
        if value in suffixes:
            return category
    return "MISC"

# test out the pickDirectory() function
# uncomment this line and write your code

def organizeDirectory():
    for item in os.scandir():
        print(f'Just Come into Organizer and found {item}')
        if item.is_dir():
            print(f'It is directory. Skipping!!!')
            continue
        filePath = Path(item)
        print(f'Here is filePath {filePath}')
        fileType = filePath.suffix.lower()
        print(f'Here is FileType {fileType}')
        directory = pickDirectory(fileType)

        directoryPath = Path(directory)
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))

# test out the organizeDirectory() function
# uncomment this line and write your code
organizeDirectory()