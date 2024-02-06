def ler_arquivo():
    with open("C://Users/Beto_Business/Desktop/Python/Programa_Ands.txt","r", encoding = "utf-8") as arquivo:
        mensagem = arquivo.readlines()
        return mensagem

def escrever_arquivo(mensagem):
    quantidade = len(mensagem)
    cont = 0
    string = ""
    while cont < quantidade:
        string = string + mensagem[cont]
        cont += 1
    with open("C://Users/Beto_Business/Desktop/Python/Programa_Ands.txt","w") as arquivo:
        arquivo.write(string)
    return 1

def mostrar_emails():
    mensagem = ler_arquivo()
    if mensagem[0] == "Emails:\n":
        tamanho = len(mensagem)
        if tamanho > 1:
            print("Você possui", (tamanho - 1)/2, "emails:\n")
            cont = 1
            for i in range(1, tamanho, 2):
                print("Email", cont, "é", mensagem[i])
                cont += 1
        else:
            print("Você não tem email cadastrado")
            return 1
        return (tamanho - 1)/2
    else:
        print("Arquivo não encontrado")
    

def adicionar_email():
    email = input("Digite o email que você quer adicionar: ")
    email = email + "\n"
    senha = input("Agora digite a sua senha: ")
    senha = senha + "\n"
    mensagem = ler_arquivo()
    mensagem.append(email)
    mensagem.append(senha)
    escrever_arquivo(mensagem)
    print("Email salvo com sucesso!")
    return 1

def modificar_senha():
    print("Qual email deseja alterar a senha: ")
    quantidade = mostrar_emails()
    email = int(input())
    mensagem = ler_arquivo()

    print("Senha Atual:", mensagem[2*email])
    nova_senha = input("Nova Senha: ")
    mensagem[2*email] = nova_senha + "\n"
    escrever_arquivo(mensagem)

def deletar_email():
    print("Qual email deseja deletar a senha: ")
    mostrar_emails()
    email = int(input())
    mensagem = ler_arquivo()
    del mensagem[email*2]
    del mensagem[email*2 - 1]
    escrever_arquivo(mensagem)


def main():
    opcao = 1
    while opcao != 0:
        print("Bem vindo!! O que você deseja fazer?\n")
        print("1- Visualizar todos os seus emails.")
        print("2- Adicionar email.")
        print("3- Modificar senhas.")
        print("4- Deletar email.")
        opcao = int(input())
        while opcao < 0 or opcao > 4:
            print("\nOpção inválida! Tente novamente")
            opcao = int(input())
        if opcao == 1:
            mostrar_emails()
        if opcao == 2:
            adicionar_email()
        if opcao == 3:
            modificar_senha()
        if opcao == 4:
            deletar_email()
main()
    
