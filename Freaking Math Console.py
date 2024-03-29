from random import *
import time


import sys
from colorama import Fore, Back, Style
from colorama import init, AnsiToWin32

init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream

def print_score(score):
    # print("Score: ", score, "\n")
    print(Fore.GREEN + "Correct!")
    print(Fore.BLUE + f"Score: {score}\n", Style.RESET_ALL)
def print_times_up():
    # print("Time's up!")
    print(Fore.RED + "Times up!")
def print_wrong():
    # print("Incorrect!")
    print(Fore.RED + "Incorrect!")

start = 0
end = 0
t = 5
count = 0


start = time.time()
end = time.time()




print("== FREAKING MATH CONSOLE == \nGive correct answers to get scores.")

score = 0

for i in range(10):
    if count == 3:
        t -= 1
        count = 0
    a = random.randint(1,15)
    b = random.randint(1,15)
    c = random.randint(-15,30)
    # n = choice("+", "-", "*", "/")
    n = random.randint(1,4)
    e = random.randint(0,1)
    # wrong answer
    if e == 0:
        if (n==1):
            print(f"{a}+{b}={c}")
            start = time.time()
            ans = int(input("1 for True, 0 for False: "))
            end = time.time()

            if ((ans == 1 and a+b==c) or (ans == 0  and not a+b==c)) and (end-start < t):
                score += 1
                print_score(score)
                continue
            elif (end-start >= t):
                print_times_up()
                break
            else:
                print_wrong()
                break
        elif (n==2):
            print(f"{a}-{b}={c}")
            start = time.time()
            ans = int(input("1 for True, 0 for False: "))
            end = time.time()

            if ((ans == 1 and a-b==c) or (ans == 0  and not a-b==c)) and (end-start < t):
                score += 1
                print_score(score)
                continue
            elif (end-start >= t):
                print_times_up()
                break
            else:
                print_wrong()
                break
        elif (n==3):
            print(f"{a}*{b}={c}")
            start = time.time()
            ans = int(input("1 for True, 0 for False: "))
            end = time.time()

            if ((ans == 1 and a*b==c) or (ans == 0  and not a*b==c)) and (end-start < t):
                score += 1
                print_score(score)
                continue
            elif (end-start >= t):
                print_times_up()
                break
            else:
                print_wrong()
                break
        else:
            print(f"{a}/{b}={c}")
            start = time.time()
            ans = int(input("1 for True, 0 for False: "))
            end = time.time()

            if ((ans == 1 and a/b==c) or (ans == 0  and not a/b==c)) and (end-start < t):
                score += 1
                print_score(score)
                continue
            elif (end-start >= t):
                print_times_up()
                break
            else:
                print_wrong()
                break
    # correct answer
    else:
        if (n==1):
            print(f"{a}+{b}={a+b}")
            start = time.time()
            ans = int(input("1 for True, 0 for False: "))
            end = time.time()

            if (ans == 1) and (end-start < t):
                score += 1
                print_score(score)
                continue
            elif (end-start >= t):
                print_times_up()
                break
            else:
                print_wrong()
                break
        elif (n==2):
            print(f"{a}-{b}={a-b}")
            start = time.time()
            ans = int(input("1 for True, 0 for False: "))
            end = time.time()

            if (ans == 1) and (end-start < t):
                score += 1
                print_score(score)
                continue
            elif (end-start >= t):
                print_times_up()
                break
            else:
                print_wrong()
                break
        elif (n==3):
            print(f"{a}*{b}={a*b}")
            start = time.time()
            ans = int(input("1 for True, 0 for False: "))
            end = time.time()

            if (ans == 1) and (end-start < t):
                score += 1
                print_score(score)
                continue
            elif (end-start >= t):
                print_times_up()
                break
            else:
                print_wrong()
                break
        else:
            print(f"{a}/{b}={a/b}")
            start = time.time()
            ans = int(input("1 for True, 0 for False: "))
            end = time.time()

            if (ans == 1) and (end-start < t):
                score += 1
                print_score(score)
                continue
            elif (end-start >= t):
                print_times_up()
                break
            else:
                print_wrong()
                break
if score == 10:
    print(Fore.YELLOW + "Congratulations! You've completed the game!")
else:
    print(Fore.RED + "You lose!")