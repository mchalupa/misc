#!/usr/bin/python

def check(y, x):
    k = int(y / 6)
    u = int((k+1) / 2)

    l = 1
    while (3*(l**2) + l <= u):
        p1 = 6*l + 1
        p2 = 6*l - 1

        if x % p1 == 0:
            print("witness", p1)
            return False
        elif x % p2 == 0:
            print("witness", p2)
            return False

        l += 1

    return True

def isprime(x):
    "Check if x is a prime greater than 3"
    x1 = x - 1
    x2 = x + 1

    if x1 % 6 == 0:
        return check(x1, x)
    elif x2 % 6 == 0:
        return check(x2, x)
    else:
        print("witness 2 or 3")
        return False

if __name__ == "__main__":
    import sys
    print(isprime(int(sys.argv[1])))
