value = "function"
for i in value:
    if i == "c":
        print ("found it")

new_value = "Hello boss baby"
word = "b"
for i in range(len(new_value)):
    if new_value[i] == word:
        print("hi--> ", i,  new_value[i], "\n")
    if new_value[i] != "b":
        print(new_value[i], end=" ")

#for j in range(len(new_value)):
 #   if new_value[j] == "b":
  #      print(j)

for i in new_value:
   if i != "b":
      print(i, end= " ")

for index, value in enumerate(new_value):
    if value == "b":
        print("\n", index, "and", value)
    if value != "b":
        print("\n", value, end= " ")


