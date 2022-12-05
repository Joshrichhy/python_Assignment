miles = 1
space = " "
print("Miles" f"{space: ^5}", "Kilometer")
while miles <= 10:
    kilometer = miles * 1.609
    print(miles, f"{kilometer:>15.3f}")
    miles += 1