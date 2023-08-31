
n = int(input("Enter n value.\n"))
a = 0
b = 1
print("Fibonacci sequence is :")
print ( a,b, sep =",",end = ",")
while (n-2 > 0):
    c = a + b
    if n-2 != 1:
        print(c, end = ",")
    else:
        print(c, end = ",...")
    a = b
    b = c
    n -=1

