# count = 1
#
# while count <=100:
#     if count%15 ==0:
#         print(count, "Fizz Buzz")
#     elif count %5 == 0:
#         print (count, "buzz")
#     elif count % 3 == 0 :
#         print(count, "fizz")
#     else:
#         print(count)
#     count += 1
#
# word="Hello World"
# for letter in word:
#     print(letter, end = '')
#
# for i in range(1, 101):
#     if i %15 ==0:
#         print(i, "Fizz Buzz")
#     elif i %5 == 0:
#         print (i, "buzz")
#     elif i % 3 == 0 :
#         print(i, "fizz")
#     else:
#         print (i)
# while (score := int(input("Enter a score or -1 to exit"))) != -1:
#     print(score)

for i in range(1, 11):
    print("*" * i)

word="misisipi is the longest river"
print(word[24:31:])
print(word[-15:-21:-1])
print(word[12:15])
print(word[12:])
print(word[0:14:3])
print(word[:-14:-1])
print(word[:-30:-1])
print(word[::-1])

s = int(input("Enter Number"))
s = str(s)
if (s ==s[::-1]):
    print("palindrone")

