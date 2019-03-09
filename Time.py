# Convert any number into Hours and Minutes

a = int(input("Enter any number as a string:"))
if a < 60:
    print('seconds :', a)
else:
    b = a // 60
    c = a % 60
    if b > 60:
        d = a // 3600
        e = a % 3600
        if e > 60:
            h = e // 60
            t = e % 60
            print("Hours:", d)
            print('Minutes:', h)
            print('Seconds:', t)
    else:
        print('Minutes:', b)
        print('Seconds:', c)
