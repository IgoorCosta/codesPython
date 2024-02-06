import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def tamanho_médio_de_palavras(palavras):
    quantidade = len(palavras)
    letras = 0
    cont = 0
    while (cont < quantidade):
        letras = letras + len(palavras[cont])
        cont += 1
    if (quantidade > 0):
        return letras/quantidade
    else:
        return 1

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    grau_de_similaridade = 0
    cont = 0
    while (cont < 6):
        grau_de_similaridade = grau_de_similaridade + abs(as_a[cont] - as_b[cont])
        cont += 1
    return grau_de_similaridade/6

    pass

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    palavras = []
    frases = []
    sentencas = separa_sentencas(texto)
    cont = 0
    while (cont < len(sentencas)):
        frases = frases + separa_frases(sentencas[cont])
        cont += 1

    cont = 0
    while (cont < len(frases)):
        palavras = palavras + separa_palavras(frases[cont])
        cont += 1

    caracteres = 0
    for i in range(len(sentencas)):
        caracteres = caracteres + len(sentencas[i])
    caracteres2 = 0
    for i in range(len(frases)):
        caracteres2 = caracteres2 + len(frases[i])

    quantidade_palavras = len(palavras)
    tamanho_medio_palavra = tamanho_médio_de_palavras(palavras)
    type_Token = n_palavras_diferentes(palavras)/quantidade_palavras
    hapax = n_palavras_unicas(palavras)/quantidade_palavras
    tamanho_medio_sentenca = caracteres/len(sentencas)
    complexidade_sentenca = len(frases)/len(sentencas)
    tamanho_medio_frase = caracteres2/len(frases)

    return ([tamanho_medio_palavra, type_Token, hapax, tamanho_medio_sentenca, complexidade_sentenca, tamanho_medio_frase])

    pass

def minimo(sim):
    min = sim[0]
    i = 1
    while i < len(sim):
        if sim[i] < min:
            min = sim[i]
        i += 1
    i = 0
    while (i < len(sim)):
        if (sim[i] == min):
            return i + 1
        i += 1
    return 0

        
def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    
    assinatura = []
    cont = 0
    print(len(textos))
    while (cont < len(textos)):
        x = textos[cont]
        assinatura.append(calcula_assinatura(x))
        cont += 1
    
    similaridade = []
    cont = 0
    while (cont < len(assinatura)):
        similaridade.append(compara_assinatura(ass_cp, assinatura[cont]))
        cont += 1
    return (minimo(similaridade))

    pass

a = le_assinatura()
aval = avalia_textos(le_textos(), a)
#aval = avalia_textos([t1, t2, t3], n)
print("O autor do texto", aval, "está infectado com COH-PIAH")
