from pathlib import Path


def writing_files():
    file = Path.cwd() / "Joshua"
    file.mkdir(exist_ok=True)

    new_file = file/"precious.txt"
    new_file.write_text("hello Olayinka Oniyide, how is your reading going? Josh misses you")
    word = new_file.read_text()
    lists = word.split(" ")
    return lists
print(writing_files())


new_file = open("jay.txt", "w")
new_file.write("hello Renike, how is your reading going?")
new_file.close()


new_file = open("jay.txt", "r")
print(new_file.readlines())
