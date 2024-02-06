def primo(N):
	cont = 1
	quantidade = 0
	while ((cont <= N) and (quantidade < 3)):
		if(N % cont == 0):
			quantidade += 1
		cont += 1 
	if (quantidade <= 2):
		return 1
	else: 
		return 0

def maior_primo(x):
	while (x >= 2):
		if (primo(x) == 1):
			return x
		x -= 1
	return 1

a = int(input("Digite o número: "))
x = maior_primo(a)
print(x)