"""
elif = else if

Decision tree In Python

- if: elif:  else:
. while :    else:
- for x in : else:

Breaking & Passing
- pass : add to empty if condition
- break: breaks loop
- continue: skip loop

Range:
- range(n) : return sequence of 0 to n-1
- range(n,m): sequence of  n+1,n+2 .. <m
- range(n,m,l): sequence of n, n+l,n+2l ...<m

"""

# ---------------IF ELIF---------------

a = 200
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")


# ---------------WHILE---------------

print("While")
i = 0
while i < 7:
    i += 1
    if i == 3:
        continue  # skip loop

    elif i == 7:
        pass      # decison without code
        # break   # break loop
    print(i)
else:
    print("i is no longer less than 7\n")


# ---------------FOR---------------

    print("For in range(n)")
for x in range(5):  # range(M) return Sequence of length N starting with 0, 1, 2..<M
    print(x)
else:
    print("Else reached!\n")

    print("For in range(n,m)")
for x in range(2, 5):  # range(N, M) return Sequence of length (M-N) starting with N, N+1, N+2...<M
    print(x)
else:
    print("Else reached!\n")

    print("For in range(n,l,m)")
    for x in range(1, 10, 1):  # range(N, M, l) return Sequence starting with N, N+l, N+2*l...N+l*n < M
        print(x)
    else:
        print("Else reached!\n")





