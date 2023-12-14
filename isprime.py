def isPrime(n):
    for artinCounter in range(2, n):
        if n % artinCounter == 0:
            return False
    return True


def isEven(n):
    res = n % 2 == 0
    return res

def isOdd(n):
    return n % 2 != 0


def sayHello(name, age):
    print("Hello I am " + name + " and I am " + str(age) + " years old")

# sayHello("Aidin", 14)



# n  = 5
#   *
#  ***
# *****

def printStar(n):
    for x in range(1, n+1, 2):
        print(" " * ((n - x)//2) + "*" * x)

def printTri(n, sep=0):
    if n < 1:
        return
    printTri(n-2, sep + 2)
    print(" " * (sep//2) + "*" * n)


# printStar(11)
# printTri(11, 0)

def fibonacci(n):
    """
    n = 1 -> 1
    n = 2 -> 1
    n = 3 -> 2
    n = 4 -> 3
    n = 5 -> 5
    n = 6 -> 8
    n = 7 -> 13
    n = 8 -> 21
    n = 9 -> 34
    n = 10 -> 55
    """
    f1 = 1
    f2 = 1
    if n == 1 or n == 2:
        return f1
    for x in range(3,  n+1):
        tmp = f2
        f2 = f1 + f2
        f1 = tmp
    return f2

def fibo(n):
    if n <= 2:
        return 1
    return fibo(n-1) + fibo(n-2)


print(fibonacci(10))
print(fibo(10))
