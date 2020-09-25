speed = int(input("Please enter current speed in km/h:"))
allowed_speed = int(input("Please enter the allowed speed:"))
demerits = (speed-allowed_speed)//5
if (speed<allowed_speed):
    print("OK")
elif (allowed_speed<speed and demerits<=12):
    print(demerits,"points")
else:
    print("Go To Jail")