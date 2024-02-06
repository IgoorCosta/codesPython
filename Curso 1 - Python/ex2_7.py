largura = int(input())
altura = int(input())
a = altura

while a > 0:
    l = largura
    while l > 0:
        if (largura == l or l == 1 or altura == a or a == 1):
            print("#", end ="")
        else:
            print(" ", end = "")
        l -= 1
    print()
    a -= 1
