#n=5

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

op=fact(5)
print(op)