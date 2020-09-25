mark =int(input("Please enter your mark:"))
if not isinstance(mark, int):
    print("Wrong Input")
elif (mark >= 80) and (mark <= 100):
    print("Grade A")
elif (mark >= 70) and (mark <= 79):
    print("Grade B")
elif (mark >= 50) and (mark <= 69):
    print("Grade C")
elif (mark >= 40) and (mark <= 49):
    print("Grade D")
elif (mark >= 0) and (mark <= 39):
    print("Grade E")
else:
    print("Out of range")
