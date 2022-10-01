from random import *
import string
L = int(input("Enter the length of password between 6 and 8 : "))
if 6 <= L <= 8:
    pass
else:
    print("Please follow instructions ")
    L = int(input("Enter the length of password between 6 and 8 : "))

m = L - 3
ans = []

for i in range(m):
    t = (choice(string.ascii_letters))
    ans.append(t)

#p = ["@", "$", "!", "&"]
#ans.append(shuffle(p))

for i in range(2):
    x = randrange(9)
    ans.append(x)

for i in ans:
    print(i,end="")