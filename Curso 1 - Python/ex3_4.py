numero = int(input("Digite o valor de n: "))

grandeza = len(str(numero))

soma = 0

while grandeza >= 1:
	soma = numero%10 + soma
	numero = numero // 10
	grandeza -= 1
print(soma)