import pathlib
from pathlib import Path

file_path = Path.home() / "my_folder"
file_path.mkdir(exist_ok=True)
new_file = file_path / "my_file.txt"
new_file.touch(exist_ok=True)

print(file_path.exists())
print(new_file.parent)
print(file_path)


print(Path.home())

