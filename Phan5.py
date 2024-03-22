import random
print("== FREAKING MATH CONSOLE == \nGive correct answers to get scores.")

score = 0

for i in range(30):
    a = random.randint(1,15)
    b = random.randint(1,15)
    c = random.randint(-15,30)
    n = random.randint(1,4)
    if (n==1):
        print(f"{a}+{b}={c}")
        ans = int(input("1 for True, 0 for False: "))
        if (ans == 1 and a+b==c) or (ans == 0  and not a+b==c):
            score += 1
            print("Score: ", score, "\n")
            continue
        else:
            print("Incorrect!")
            break
    elif (n==2):
        print(f"{a}-{b}={c}")
        ans = int(input("1 for True, 0 for False: "))
        if (ans == 1 and a-b==c) or (ans == 0  and not a-b==c):
            score += 1
            print("Score: ", score, "\n")
            continue
        else:
            print("Incorrect!")
            break
    elif (n==3):
        print(f"{a}*{b}={c}")
        ans = int(input("1 for True, 0 for False: "))
        if (ans == 1 and a*b==c) or (ans == 0  and not a*b==c):
            score += 1
            print("Score: ", score, "\n")
            continue
        else:
            print("Incorrect!")
            break
    else:
        print(f"{a}/{b}={c}")
        ans = int(input("1 for True, 0 for False: "))
        if (ans == 1 and a/b==c) or (ans == 0  and not a/b==c):
            score += 1
            print("Score: ", score, "\n")
            continue
        else:
            print("Incorrect!")
            break
if score == 30:
    print("Congratulations! You've completed the game!")