# bai 1:

# for i in range(3, 13):
#     print(i, end=" ")

# bai 2:

# n = int(input("Input a number: "))
# for i in range(n+1):
#     print(i, end=" ")

# bai 3:

# n = int(input("Input a number: "))
# for i in range(1, n+1):
#     if (i % 2 == 1):
#         print(i, end=" ")

# bai 4:

import turtle
a = int(input("Input number of edges: "))
t = turtle
t.speed(10)
for i in range(a):
    t.forward(50)
    t.left(180-(a-2)*180/a)
t.done()