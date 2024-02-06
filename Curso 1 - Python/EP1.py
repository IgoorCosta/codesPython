
def computador_escolhe_jogada(n, m):
    cont = m
    while cont > 0: 
        if (n - cont)%(m + 1) == 0:
            if cont == 1:
                print("\nO computador tirou uma peça.")
            else:
                print("\nO computador tirou", cont, "peças")
            return cont
        cont -= 1
    if m == 1:
        print("\nO computador tirou uma peça.")
    else:
        print("\nO computador tirou", m, "peças")
    return m

def usuario_escolhe_jogada(n, m):
    retirar = 0
    while retirar > m or retirar < 1:
        retirar = int(input("\nQuantas peças você vai retirar? "))
        if (retirar > m or retirar < 1):
            print("\nOops! Jogada inválida! Tente de novo. ")
    if retirar == 1:
        print("\nVocê tirou uma peça.")
    else:
        print("\nVocê tirou", retirar, "peças")
    return retirar
    
def partida():
    n = int(input("Quantas peças? " ))
    m = int(input("Limite de peças por jogada? " ))
                  
    if (n % (m + 1) == 0):
        print("\nVocê começa!")
        vez = True
    else:
        print("\nComputador começa!")
        vez = False

    while n > 0:
        if (vez == True):
            retirou = usuario_escolhe_jogada(n, m)
            n = n - retirou
        else:
            retirou = computador_escolhe_jogada(n, m)
            n = n - retirou
        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.")
        if n > 1:
            print("Agora restam", n, "peças no tabuleiro.")
        if n <= 0:
            if(vez == False):
                print("\nFim do jogo! O computador ganhou!")
                return 1
            else:
                print("\nFim do jogo! Você ganhou!")
                return 0
        vez = not vez
    

def campeonato():
    print("\nRodada 1")
    a = partida()
    print("\nRodada 2")
    b = partida()
    print("\nRodada 3")
    c = partida()
    print("\nFinal do campeonato!")
    print("\nPlacar: Você", 3 - (a + b + c), "X", a+b+c, "Computador")

print("Bem-vindo ao jogo do NIM! Escolha:")
print("1 - para jogar uma partida isolada")
escolha = int(input("2 - para jogar um campeonato "))

while escolha != 1 and escolha != 2:
    if (escolha != 1 and escolha != 2):
        print("\nOops! Opção inválida! Tente de novo. ")
    escolha = int(input())

if escolha == 1:
    print("\nVocê escolheu uma partida isolada!")
    partida()
    
else:
    print("\nVoce escolheu um campeonato!")
    campeonato()
    
    
