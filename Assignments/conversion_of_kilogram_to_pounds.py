kilogram = 1
space = " "
print("kilogram", f"{space:^5}", "pounds")
while kilogram < 200:
    pounds = kilogram * 2.2
    print(kilogram, f"{space:^12}", f"{pounds: .2f}")
    kilogram += 1
