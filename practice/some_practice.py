# a = 5 ** 5
# # exponential
# print(a)
#
# for i in range(1, 10, 2):
#     print(i, end=" ")
#
# new_file = open("renike.txt", "w")
# new_file.write("hello Renike, how is your reading going?")
# new_file.writelines(["Hello", " how is it going\n do not worry\nyou just entered your second month"])
# new_file.close()
#
# new_file = open("renike.txt", "r")
# print(new_file.readlines())
# new_file.seek(0)
#
# print(new_file)
from pathlib import Path
file = Path.cwd()/"josh.py"/"josh.py"
file.touch(exist_ok = True)
print(list(file.parents))


