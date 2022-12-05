name = "Josh"
age = 18
s = "{} is {} years old".format(name, age)
#or
s = "{1} is {0} years old".format(age, name)#to add number to know which to print
#or
s = "{1} is {0} years old and {1} loves Java".format(age, name)
s = "{1:20} is {0} years old".format(age, name) #to put spaces
s = "{1:^20} is {0} years old".format(age, name) #to put alignent ><^
#or
s = f"{name:<20} is {age} years old"
s = f"{name=} is {age=} years old"
s = f"{name=} is {age:.2%} years old" #for calculations etc, this one is in percentage anyways
s = f"{name:#<20} is {age} years old" #to fll the said spaces
print(s)


hello = "hello world"
for index, letter in enumerate(hello, start =1):
    print(f"{letter}--> {index}")

# for index in range(len(hello)):
#     print(f"{hello[index]} --> {index}")

for i in range(1,21, 2):
    s = "*" * i
    print(f"{s:^20}")

for i in range(1,21, 2):
    s = "*" * i
    print(f"{s:20}{s:^20}")

for i in range(1,21, 2):
    s = "*" * i
    print(f"{s:20}{s:^20}{s:>20}")