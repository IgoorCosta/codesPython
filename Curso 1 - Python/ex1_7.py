largura = int(input())
altura = int(input())

while altura > 0:
    l = largura
    while l > 0:
        print("#", end ="")
        l -= 1
    print()
    altura -= 1
