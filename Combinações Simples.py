# Modelos Probabilísticos Discretos

import math

def combinacao_Simples(N, k):
	x = math.factorial(int(N))/((math.factorial(int(N - k))*math.factorial(int(k))))
	return x

def distribuicao_Binominal_Multipla(N, k, p):
	x = (math.pow(p, k)*math.pow(1 - p, N - k))
	return (x * combinacao_Simples(N, k))

def distribuicao_Binominal(N, k, p):
	
	valor_Esperado = N*p
	variancia = N*p*(1 - p)

	print("- Valor Esperado:", valor_Esperado)
	print("- Variancia:", variancia)
	print("- Desvio Padrão:", math.sqrt(variancia))
	print("- P(x = k):", distribuicao_Binominal_Multipla(N, k, p))

	if (k <= N/2 and N < 1000):
		somatoria = 0
		while (k >= 0):
			somatoria = somatoria + distribuicao_Binominal_Multipla(N, k, p)
			k -= 1
		print("- P(x <= k):", somatoria)
		print("- P(x > k):", 1 - somatoria)
	if (k > N/2 and N < 1000):
		somatoria = 0
		while (k <= N):
			somatoria = somatoria + distribuicao_Binominal_Multipla(N, k, p)
			k += 1
		print("- P(x >= k):", somatoria)
		print("- P(x < k):", 1 - somatoria)

	return (True)

def distribuicao_geometrica(k, p):
        valor_Esperado = (1 - p)/p
        variancia = (1 - p)/(p*p)
        print("- Valor Esperado:", valor_Esperado)
        print("- Variancia:", variancia)
        print("- Desvio Padrão:", math.sqrt(variancia))

        probabilidade = ((1 - p)**k) * p
        cont = 0
        prob = 0
        while cont <= k:
                prob = prob + ((1 - p)**cont) * p
                cont += 1
        print("- P(x = k):", probabilidade)
        print("- P(x <= k):", prob)
        return 1

def distribuicao_poisson(l, k):
        valor_Esperado = l
        variancia = l
        print("- Valor Esperado:", valor_Esperado)
        print("- Variancia:", variancia)
        print("- Desvio Padrão:", math.sqrt(variancia))
        probabilidade = (2.718281828**(-l))*(l**k)/math.factorial(k)
        cont = 0
        prob = 0
        while cont <= k:
                prob = prob + (2.718281828**(-l))*(l**cont)/math.factorial(cont)
                cont += 1
        print("- P(x = k):", probabilidade)
        print("- P(x <= k) (0 até k):", prob)
        return 1

def main():
        opcao = 1
        while opcao != 0:
                print("\nEscolha as opções abaixo:")
                print("1. Distribuição Binominal")
                print("2. Distruibuição Geométrica")
                print("3. Distribuição de Poisson")
                opcao = int(input())
                if opcao == 1:
                        N = float(input("Digite o número de elementos N: "))
                        k = float(input("Digite o número de elementos k: "))
                        p = float(input("Digite o número de elementos p: "))
                        distribuicao_Binominal(N, k, p)
                if opcao == 2:
                        k = float(input("Número de falhas até o sucesso k: "))
                        p = float(input("Probabilidade de sucesso p: "))
                        distribuicao_geometrica(k, p)
                if opcao == 3:
                        l = float(input("Taxa média de ocorrencia lambda: "))
                        k = int(input("k: "))
                        distribuicao_poisson(l, k)
        print("tchau")

main()

