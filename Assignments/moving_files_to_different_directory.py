from pathlib import Path

main_folder = Path.home() / " Practice Files Folder"
main_folder.mkdir(exist_ok=True)

subfolder = main_folder / "documents"
subfolder.mkdir(exist_ok=True)

files_in_subfolder = [subfolder / "spencer.csv",
                      subfolder / "felix.txt",
                      subfolder / "image1.png",
                      subfolder / "image2.gif",
                      subfolder / "image3.png",
                      subfolder / "image4.png"]

for files in files_in_subfolder:
    files.touch(exist_ok=True)

image_folder = main_folder / "images"
image_folder.mkdir(exist_ok=True)

source = subfolder / "image1.png"
destination = image_folder / "image1.png"
source.replace(destination)

source1 = subfolder / "image2.gif"
destination1 = image_folder / "image2.gif"
source1.replace(destination1)

source2 = subfolder / "image3.png"
destination2 = image_folder / "image3.png"
source2.replace(destination2)

source3 = subfolder / "image4.png"
destination3 = image_folder / "image4.png"
source3.replace(destination3)











