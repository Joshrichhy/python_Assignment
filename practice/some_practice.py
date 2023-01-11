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
# from pathlib import Path
# file = Path.cwd()/"josh.py"/"josh.py"
# file.touch(exist_ok = True)
# print(list(file.parents))
from array import array

num = [1,2,3,4,5,6, "josh",7,8,9,10]
print(num[-3: -6: -1])
num.append("bolaji")
print(num)
num.insert(4, "kene")
print(num)
# import numpy as np
# number = np.array([2,4,6,8,10,12])


string = "mississippi is the longest river"
print(string[17: 11: -1])

num = ["Obi is a boy",
       "Ada is a girl",
       "Josh is a man"]
print(num[0][4:: 1])
num.append(10)
#to print a word
print(num[2][0: 5: 1])
print(num)

number = array("i", [1,2,3,4,5,6,7,8,9,10])
number.append(11)
print(number)






