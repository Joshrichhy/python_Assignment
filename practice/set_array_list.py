set_val = {"hi", "ho"}
user_Input = list(input("enter numbers"))
count = 0
for i in range(len(user_Input)):
    if user_Input[i] == set_val:
        set_val.add(user_Input[i])
    else:
        print(user_Input[i])

    count = len(set_val)

print("set --> ", set_val, count)

