import random
import numpy as np
import tkinter as tk
import pyautogui
import time

global position
global colors
global metrhths
global Kinhseis

pyautogui.PAUSE = 0.0001
# waiting=0

for _i in range(1):
    Kinhseis = []
    position = 1
    metrhths = 0
    colors = {0: "white", 1: "blue", 2: "red", 3: "green", 4: "yellow", 5: "orange"}

    R = np.arange(9).reshape(3, 3)
    U = np.arange(9).reshape(3, 3)
    F = np.arange(9).reshape(3, 3)
    L = np.arange(9).reshape(3, 3)
    B = np.arange(9).reshape(3, 3)
    D = np.arange(9).reshape(3, 3)
    A = np.arange(9).reshape(3, 3)
    R1 = np.arange(9).reshape(3, 3)
    U1 = np.arange(9).reshape(3, 3)
    F1 = np.arange(9).reshape(3, 3)
    L1 = np.arange(9).reshape(3, 3)
    B1 = np.arange(9).reshape(3, 3)
    D1 = np.arange(9).reshape(3, 3)

for x in range(0, 3):
    for y in range(0, 3):
        D[x, y] = 0
        L[x, y] = 1
        F[x, y] = 2
        R[x, y] = 3
        U[x, y] = 4
        B[x, y] = 5


def printcube():
    print("       ", B[0, 0], B[0, 1], B[0, 2])
    print("       ", B[1, 0], B[1, 1], B[1, 2])
    print("       ", B[2, 0], B[2, 1], B[2, 2])
    print(" ")
    print("       ", U[0, 0], U[0, 1], U[0, 2])
    print("       ", U[1, 0], U[1, 1], U[1, 2])
    print("       ", U[2, 0], U[2, 1], U[2, 2])
    print(" ")
    print(L[0, 0], L[0, 1], L[0, 2], " ", F[0, 0], F[0, 1], F[0, 2], " ", R[0, 0], R[0, 1], R[0, 2])
    print(L[1, 0], L[1, 1], L[1, 2], " ", F[1, 0], F[1, 1], F[1, 2], " ", R[1, 0], R[1, 1], R[1, 2])
    print(L[2, 0], L[2, 1], L[2, 2], " ", F[2, 0], F[2, 1], F[2, 2], " ", R[2, 0], R[2, 1], R[2, 2])
    print(" ")
    print("       ", D[0, 0], D[0, 1], D[0, 2])
    print("       ", D[1, 0], D[1, 1], D[1, 2])
    print("       ", D[2, 0], D[2, 1], D[2, 2])
    print("      ", "-------")


def r():
    global Kinhseis
    Kinhseis.append("r")
    a = R[0, 0]
    b = R[1, 0]
    R[0, 0] = R[2, 0]
    R[1, 0] = R[2, 1]
    R[2, 0] = R[2, 2]
    R[2, 1] = R[1, 2]
    R[2, 2] = R[0, 2]
    R[1, 2] = R[0, 1]
    R[0, 2] = a
    R[0, 1] = b
    for x in range(0, 3):
        a = B[x, 2]
        B[x, 2] = U[x, 2]
        U[x, 2] = F[x, 2]
        F[x, 2] = D[x, 2]
        D[x, 2] = a


def u():
    global Kinhseis
    Kinhseis.append("u")
    a = U[0, 0]
    b = U[1, 0]
    U[0, 0] = U[2, 0]
    U[1, 0] = U[2, 1]
    U[2, 0] = U[2, 2]
    U[2, 1] = U[1, 2]
    U[2, 2] = U[0, 2]
    U[1, 2] = U[0, 1]
    U[0, 2] = a
    U[0, 1] = b
    for y in range(0, 3):
        a = L[0, y]
        L[0, y] = F[0, y]
        F[0, y] = R[0, y]
        R[0, y] = B[2, 2 - y]
        B[2, 2 - y] = a


def f():
    global Kinhseis
    Kinhseis.append("f")
    a = F[0, 0]
    b = F[1, 0]
    F[0, 0] = F[2, 0]
    F[1, 0] = F[2, 1]
    F[2, 0] = F[2, 2]
    F[2, 1] = F[1, 2]
    F[2, 2] = F[0, 2]
    F[1, 2] = F[0, 1]
    F[0, 2] = a
    F[0, 1] = b
    for x in range(0, 3):
        a = U[2, 2 - x]
        U[2, 2 - x] = L[x, 2]
        L[x, 2] = D[0, x]
        D[0, x] = R[2 - x, 0]
        R[2 - x, 0] = a


def l():
    global Kinhseis
    Kinhseis.append("l")
    a = L[0, 0]
    b = L[1, 0]
    L[0, 0] = L[2, 0]
    L[1, 0] = L[2, 1]
    L[2, 0] = L[2, 2]
    L[2, 1] = L[1, 2]
    L[2, 2] = L[0, 2]
    L[1, 2] = L[0, 1]
    L[0, 2] = a
    L[0, 1] = b
    for x in range(0, 3):
        a = B[x, 0]
        B[x, 0] = D[x, 0]
        D[x, 0] = F[x, 0]
        F[x, 0] = U[x, 0]
        U[x, 0] = a


def d():
    global Kinhseis
    Kinhseis.append("d")
    a = D[0, 0]
    b = D[1, 0]
    D[0, 0] = D[2, 0]
    D[1, 0] = D[2, 1]
    D[2, 0] = D[2, 2]
    D[2, 1] = D[1, 2]
    D[2, 2] = D[0, 2]
    D[1, 2] = D[0, 1]
    D[0, 2] = a
    D[0, 1] = b
    for x in range(0, 3):
        a = R[2, x]
        R[2, x] = F[2, x]
        F[2, x] = L[2, x]
        L[2, x] = B[0, 2 - x]
        B[0, 2 - x] = a


def b():
    global Kinhseis
    Kinhseis.append("b")
    a = B[0, 0]
    b = B[1, 0]
    B[0, 0] = B[2, 0]
    B[1, 0] = B[2, 1]
    B[2, 0] = B[2, 2]
    B[2, 1] = B[1, 2]
    B[2, 2] = B[0, 2]
    B[1, 2] = B[0, 1]
    B[0, 2] = a
    B[0, 1] = b
    for x in range(0, 3):
        a = U[0, x]
        U[0, x] = R[x, 2]
        R[x, 2] = D[2, 2 - x]
        D[2, 2 - x] = L[2 - x, 0]
        L[2 - x, 0] = a


def rotate():
    global Kinhseis
    Kinhseis.append("rotate")
    for _i in range(3):
        a = U[0, 0]
        b = U[1, 0]
        U[0, 0] = U[2, 0]
        U[1, 0] = U[2, 1]
        U[2, 0] = U[2, 2]
        U[2, 1] = U[1, 2]
        U[2, 2] = U[0, 2]
        U[1, 2] = U[0, 1]
        U[0, 2] = a
        U[0, 1] = b
        for y in range(0, 3):
            a = L[0, y]
            L[0, y] = F[0, y]
            F[0, y] = R[0, y]
            R[0, y] = B[2, 2 - y]
            B[2, 2 - y] = a
    a = D[0, 0]
    b = D[1, 0]
    D[0, 0] = D[2, 0]
    D[1, 0] = D[2, 1]
    D[2, 0] = D[2, 2]
    D[2, 1] = D[1, 2]
    D[2, 2] = D[0, 2]
    D[1, 2] = D[0, 1]
    D[0, 2] = a
    D[0, 1] = b
    for x in range(0, 3):
        a = R[2, x]
        R[2, x] = F[2, x]
        F[2, x] = L[2, x]
        L[2, x] = B[0, 2 - x]
        B[0, 2 - x] = a
    for x in range(0, 3):
        a = R[1, x]
        R[1, x] = F[1, x]
        F[1, x] = L[1, x]
        L[1, x] = B[1, 2 - x]
        B[1, 2 - x] = a


def wellowcross():
    for x in range(0, 8):
        rotate()
        if L[1, 0] == 0:
            for y in range(0, 4):
                if U[0, 1] != 0:
                    b()
                    b()
                    b()
                    break
                else:
                    u()

        if L[1, 2] == 0:
            for y in range(0, 4):
                if U[2, 1] != 0:
                    f()
                    break
                else:
                    u()

        if L[0, 1] == 0:
            l()
            u()
            u()
            u()
            f()

        if L[2, 1] == 0:
            for y in range(0, 4):
                if U[2, 1] != 0:
                    l()
                    l()
                    l()
                    f()
                    l()
                    break
                else:
                    u()
        if D[1, 0] == 0:
            for y in range(0, 4):
                if U[1, 0] != 0:
                    l()
                    l()
                    break
                else:
                    u()
        if D[2, 1] == 0:
            for x in range(0, 4):
                if U[0, 1] != 0:
                    b()
                    b()
                    break
                else:
                    u()
        if D[0, 1] == 0:
            for x in range(0, 4):
                if U[2, 1] != 0:
                    f()
                    f()
                    break
                else:
                    u()
        if D[1, 2] == 0:
            for x in range(0, 4):
                if U[1, 2] != 0:
                    r()
                    r()
                    break
                else:
                    u()


def whitecross():
    for x in range(0, 4):
        rotate()
        for y in range(0, 4):
            if U[2, 1] == 0:
                if F[0, 1] == F[1, 1]:
                    f()
                    f()
                    break
                else:
                    u()
                    rotate()


def whiteangles():
    for x in range(0, 4):
        rotate()
        for y in range(0, 4):
            if L[0, 0] * U[0, 0] * B[2, 0] != 0:
                if F[2, 0] * L[2, 2] * D[0, 0] == 0:
                    f()
                    u()
                    u()
                    u()
                    f()
                    f()
                    f()
                    u()
                    break
                else:
                    u()
                    break
            else:
                u()

    for z in range(0, 4):
        for x in range(0, 4):
            rotate()
            for y in range(0, 4):
                if F[0, 0] == 0:
                    if L[0, 2] == L[1, 1]:
                        f()
                        u()
                        f()
                        f()
                        f()
                        u()
                        u()
                        u()
                        break
                    else:
                        u()
                        rotate()
        for x in range(0, 4):
            rotate()
            for y in range(0, 4):
                if L[0, 2] == 0:
                    if F[0, 0] == F[1, 1]:
                        l()
                        l()
                        l()
                        u()
                        u()
                        u()
                        l()
                        u()
                        break
                    else:
                        u()
                        rotate()
        for x in range(0, 4):
            rotate()
            for y in range(0, 4):
                if U[2, 0] == 0:
                    if F[0, 0] == L[1, 1]:
                        f()
                        u()
                        u()
                        f()
                        f()
                        f()
                        u()
                        u()
                        u()
                        f()
                        u()
                        f()
                        f()
                        f()
                        u()
                        u()
                        break
                    else:
                        u()
                        rotate()


def algorithm1():
    u()
    u()
    u()
    l()
    l()
    l()
    u()
    l()
    u()
    f()
    u()
    u()
    u()
    f()
    f()
    f()


def algorithm2():
    u()
    r()
    u()
    u()
    u()
    r()
    r()
    r()
    u()
    u()
    u()
    f()
    f()
    f()
    u()
    f()


def edges():
    for x in range(0, 8):
        rotate()
        for y in range(0, 4):
            if F[1, 0] != 4 and L[1, 2] != 4:
                if F[0, 1] == 4 or U[2, 1] == 4:
                    algorithm1()
                else:
                    u()
            else:
                break

    for x in range(0, 4):
        for y in range(0, 16):
            if F[0, 1] != 4 and U[2, 1] != 4:
                if F[0, 1] == F[1, 1]:
                    if U[2, 1] == L[1, 1]:
                        algorithm1()
                        break
                    if U[2, 1] == R[1, 1]:
                        algorithm2()
                        break
                else:
                    u()
                    rotate()
            else:
                u()


def algorithm3():
    f()
    u()
    r()
    u()
    u()
    u()
    r()
    r()
    r()
    f()
    f()
    f()


def yellowcross():
    for x in range(0, 4):
        if U[0, 1] != 4 and U[2, 1] != 4:
            algorithm3()
            algorithm3()
        if U[1, 0] != 4 and U[1, 2] != 4:
            u()
            algorithm3()
            algorithm3()
        if U[1, 0] == 4 and U[0, 1] == 4 and U[1, 2] != 4:
            algorithm3()
        if U[1, 0] == 4 and U[2, 1] == 4 and U[1, 2] != 4:
            u()
            algorithm3()
        if U[2, 1] == 4 and U[1, 2] == 4 and U[0, 1] != 4:
            u()
            u()
            algorithm3()
        if U[0, 1] == 4 and U[1, 2] == 4 and U[1, 0] != 4:
            u()
            u()
            u()
            algorithm3()


def aligncross():
    for x in range(0, 4):
        if F[0, 1] == F[1, 1]:
            for y in range(0, 4):
                if L[0, 1] != L[1, 1]:
                    r()
                    u()
                    r()
                    r()
                    r()
                    u()
                    r()
                    u()
                    u()
                    r()
                    r()
                    r()
                else:
                    if R[0, 1] != R[1, 1]:
                        u()
                        rotate()
                        rotate()
                        rotate()
                        r()
                        u()
                        r()
                        r()
                        r()
                        u()
                        r()
                        u()
                        u()
                        r()
                        r()
                        r()
                        break
                    else:
                        oo = 1
                        break

        else:
            u()


def algorithm4():
    u()
    r()
    u()
    u()
    u()
    l()
    l()
    l()
    u()
    r()
    r()
    r()
    u()
    u()
    u()
    l()


def algorithm5():
    a = 0
    if U[2, 0] == U[1, 1] and F[0, 0] == F[1, 1] and L[0, 2] == L[1, 1]:
        a = 1
    if U[2, 0] == L[1, 1] and F[0, 0] == U[1, 1] and L[0, 2] == F[1, 1]:
        a = 1
    if U[2, 0] == F[1, 1] and F[0, 0] == L[1, 1] and L[0, 2] == U[1, 1]:
        a = 1
    if a == 0:
        algorithm4()


def alignangles():
    for x in range(0, 4):
        rotate()
        b = 0
        if U[2, 2] == U[1, 1] and F[0, 2] == F[1, 1] and R[0, 0] == R[1, 1]:
            for y in range(0, 4):
                b = 1
                algorithm5()
        if U[2, 2] == F[1, 1] and F[0, 2] == R[1, 1] and R[0, 0] == U[1, 1]:
            for y in range(0, 4):
                b = 1
                algorithm5()
        if U[2, 2] == R[1, 1] and F[0, 2] == U[1, 1] and R[0, 0] == F[1, 1]:
            for y in range(0, 4):
                b = 1
                algorithm5()

    if b == 0:
        algorithm4()
        rotate()
        rotate()
        rotate()
        for x in range(0, 4):
            rotate()
            if U[2, 2] == U[1, 1] and F[0, 2] == F[1, 1] and R[0, 0] == R[1, 1]:
                for y in range(0, 4):
                    algorithm5()
            if U[2, 2] == F[1, 1] and F[0, 2] == R[1, 1] and R[0, 0] == U[1, 1]:
                for y in range(0, 4):
                    algorithm5()
            if U[2, 2] == R[1, 1] and F[0, 2] == U[1, 1] and R[0, 0] == F[1, 1]:
                for y in range(0, 4):
                    algorithm5()


def orientangles():
    global Kinhseis
    for x in range(0, 4):
        if F[0, 0] == 4:
            for y in range(0, 4):
                l()
                d()
                l()
                l()
                l()
                d()
                d()
                d()
        if L[0, 2] == 4:
            for y in range(0, 2):
                l()
                d()
                l()
                l()
                l()
                d()
                d()
                d()
        u()


def scramble(o):
    for x in range(0, o):
        ooo = random.randint(0, 5)
        if ooo == 0:
            r()
        if ooo == 1:
            u()
        if ooo == 2:
            l()
        if ooo == 3:
            b()
        if ooo == 4:
            d()
        if ooo == 5:
            f()


def show_side(x, y, size, A):
    for i in range(3):
        for j in range(3):
            w.create_rectangle(x + i * size, y + j * size, x + (i + 1) * size, y + (j + 1) * size, fill=colors[A[j, i]])


def show_cube(windowx, windowy, d, size):
    cx = windowx / 2 - 9 / 2 * size - d
    cy = windowy / 2 - 6 * size - 3 / 2 * d
    # show_side(cx, cy, 20, F)
    w.delete('all')
    for x in range(3):
        tempdict = {0: L, 1: F, 2: R}
        show_side(cx + x * (3 * size + d), cy + 6 * size + 2 * d, size, tempdict[x])
    for y in range(4):
        tempdict = {0: B, 1: U, 2: F, 3: D}
        show_side(cx + 3 * size + d, cy + y * (3 * size + d), size, tempdict[y])
    # printcube()

    w.pack()
    mylabel.configure(text=metrhths)
    mylabel.pack()


def enter(event):
    global position
    position = 1
    pyautogui.click()
    # print('Button-2 pressed at x = % d, y = % d' % (event.x, event.y))


def exit_(event):
    global position
    position = 0



def m1(event):
    global metrhths
    if position:
        if metrhths == len(telos):
            print("telos")
            for _ in range(100):
                time.sleep(0.1)

            quit()
        if telos[metrhths] == "u":
            u()
        if telos[metrhths] == "r":
            r()
        if telos[metrhths] == "f":
            f()
        if telos[metrhths] == "b":
            b()
        if telos[metrhths] == "l":
            l()
        if telos[metrhths] == "d":
            d()
        if telos[metrhths] == "rotate":
            rotate()
        metrhths += 1
        show_cube(500, 700, 30, 30)
        pyautogui.click()


def solve():
    wellowcross()

    whitecross()

    whiteangles()

    edges()

    yellowcross()

    aligncross()

    alignangles()

    orientangles()

    # for _i in range(2):
    #     rotate()


def copy_side(a1, a):
    for x in range(3):
        for y in range(3):
            a1[x, y] = a[x, y]


def move(oo):
    if oo == 'u':
        u()
    elif oo == 'f':
        f()
    elif oo == 'r':
        r()
    elif oo == 'd':
        d()
    elif oo == 'b':
        b()
    elif oo == 'l':
        l()
    elif oo == 'rotate':
        rotate()


root = tk.Tk()

root.geometry("500x700+10+10")

w = tk.Canvas(root, width=500, height=700)
mylabel = tk.Label(root, text=metrhths, font="arial 40", bg="yellow")
mylabel.pack(side="top")

scramble(20)
printcube()
copy_side(R1, R)
copy_side(L1, L)
copy_side(F1, F)
copy_side(U1, U)
copy_side(D1, D)
copy_side(B1, B)
Kinhseis = []

solve()
telos = Kinhseis[:]
print(len(telos))
copy_side(R, R1)
copy_side(L, L1)
copy_side(F, F1)
copy_side(U, U1)
copy_side(D, D1)
copy_side(B, B1)
printcube()

root.bind('<Enter>', enter)
root.bind('<Leave>', exit_)
root.bind('<1>', m1)

root.mainloop()
