from pathlib import Path

new_folder = Path.home() / "my_folder"
new_folder.mkdir(exist_ok=True)

new_files = [new_folder / "file1.txt",
             new_folder / "file2.txt",
              new_folder / "image1.png"
             ]
for files in new_files:
    files.touch(exist_ok=True)

images = new_folder / "images"
images.mkdir(exist_ok=True)

source = new_folder / "image1.png"
destination = images / "image1.png"

source.replace(destination)

deletefile1txt = new_folder / "file1.txt"
deletefile1txt.unlink()

deletefiletxt = new_folder / images / "image1.png"

for files in deletefiletxt:
    files.unlink()
deleteimagesfolder = new_folder / "images"
deleteimagesfolder.rmdir()

deletemyfolder = Path.home() / "my_folder"
deletemyfolder.rmdir()

print(new_folder)





