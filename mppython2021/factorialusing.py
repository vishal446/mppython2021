def testfact():
    n = int(input("enter any number for which u want factorial"))
    i = 1
    f = 1
    while i <= n:
        f = f * i
        i = i + 1
    print("Factorial=", f)

testfact()