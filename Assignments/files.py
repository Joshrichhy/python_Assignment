#import pathlib
from pathlib import Path

#path = pathlib.Path.home()
#path = pathlib.Path.cwd()
#path = pathlib.Path("c:/cohort14/private.img")
#print(path)
#print(path.is_absolute())
#path = Path("/Cohort 14/private img")
#cwd_path = Path.cwd()
#print(cwd_path)
#print("parent -", cwd_path.parent)
#print(list(cwd_path.parents))
#print (path.parents)
fake_path = Path("c:/kellogs/hello.txt")
#cwd_path = Path.cwd()/"Josh"/"numbers"/"green.csv"
#print (cwd_path)

#print("Parent -", fake_path.parent)
#print(Path.parents)
#print(list(fake_path.parents))
#print("Anchor - ", fake_path.anchor)
#print("Name - ", fake_path.name)
#print("Suffix - ", fake_path.suffix)
#print("Stem - ", fake_path.stem)






#cwd_path.mkdir()
#cwd_path.mkdir(exist_ok=True)

#new_file_path = cwd_path / "private.txt"
#new_file_path.touch()

#cwd_path.parent.mkdir()


print(fake_path.exists())
#print(cwd_path.exists())
#print("Exist? - ", cwd_path.exists())
#print("isDir - ", cwd_path.is_file())