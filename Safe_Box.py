#!/usr/bin/env python
# coding: utf-8

# In[1]:


# O objetivo do Safe Box é auxiliar o usuário no controle de senhas em emails, sites, redes sociais, etc.
# O programa cria um arquivo csv dentro da pasta Div no mesmo diretório do executável. Este arquivo é
# criptografado e armazena todas as informações de maneira segura.


# In[2]:


import pandas as pd
import numpy as np
import os
from datetime import date  # Para retornar a data de hoje
import random  # Para retornar um número aleatório


# In[3]:


# Interface inicial
def main(): 
    opcao = '1'
    while opcao != '3':
        print("\n-------- Safe Box --------\n\n"
              " 1 - Criar um Novo Perfil.\n 2 - Entrar em um Perfil.\n 3 - Sair do Safe Box.")
        opcao = input(" Digite uma opção: ")
        while opcao != '1' and opcao != '2' and opcao != '3' and opcao != 'DATAFRAME':
            print("\nOpção inválida! Digite uma opção: ")
            opcao = input()
        if opcao == '2':
            print("\n-------- Safe Box --------\n")
            contas_existentes()
        if opcao == '1':
            print("\n-------- Safe Box --------\n")
            criar_conta()
        if opcao == 'DATAFRAME':  # Modo programador: mostra o dataframe criptografado e original no terminal
            df = pd.read_csv('C:\Jupyter_Notebook_Python\Div\safe_box.csv', encoding='utf-8', dtype=str)
            print ("\n", df, "\n")
            df = dataframe()
            print (df)
    print("\n-------- Safe Box --------\n")
    return


# In[4]:


# Faz a leitura do csv e retorna o dataframe descriptografado
def dataframe():  
    if (not os.path.exists('C:\Jupyter_Notebook_Python\Div') or not os.path.exists('C:\Jupyter_Notebook_Python\Div\safe_box.csv')):  # Caso não exista o diretório ou o csv
        return False
    
    df = pd.read_csv('C:\Jupyter_Notebook_Python\Div\safe_box.csv', encoding='utf-8', dtype=str)
    if df.empty is True: 
        return False
    df = encrypt_decrypt(df, True)
    df.update(df.fillna("Sem cadastro"))  # Transforma os valores nulos em uma string
    return df


# In[5]:


# Recebe o nome e a senha de uma nova conta e acrescenta no csv criptografado
def criar_conta():
    if (not os.path.exists('C:\Jupyter_Notebook_Python\Div') or not os.path.exists('C:\Jupyter_Notebook_Python\Div\safe_box.csv')):  # Caso não exista o diretório ou o csv
        if not os.path.exists('C:\Jupyter_Notebook_Python\Div'):
            os.mkdir('C:\Jupyter_Notebook_Python\Div')
        df = pd.DataFrame(columns = ['User','Senha','Account','Password','Date', 'Shield'])
        df = encrypt_decrypt(df, False)
        df.to_csv('C:\Jupyter_Notebook_Python\Div\safe_box.csv', index=False)
        
    df = pd.read_csv('C:\Jupyter_Notebook_Python\Div\safe_box.csv', encoding='utf-8', dtype=str)
    df = encrypt_decrypt(df, True)
    df = df.append({'User' : input("Novo Usuário: ") , 'Senha' : input("Senha: "), 'Shield' : random.randint(1,1000000)} , ignore_index=True)
    df.update(df.fillna("Sem cadastro"))
    df = encrypt_decrypt(df, False)
    df.to_csv('C:\Jupyter_Notebook_Python\Div\safe_box.csv', index=False)
    print("\nConta salva com sucesso!\n")
    return


# In[6]:


#  Mostra todas as contas presentes no csv e permite até três tentativas para entrar em uma conta.
def contas_existentes():
    df = dataframe()
    if type(df) is bool:  # Verifica se o dataframe não está vazio
        print("\nNão existe nenhum perfil neste computador.\n")
        return
    quantidade_contas = df.groupby(['User']).size().reset_index(name='count')
    print("Para voltar ao menu principal digite: 0. \nPerfis existentes:\n")
    
    count = 1
    while count <= len(quantidade_contas):
        print(count,"-", quantidade_contas.loc[count - 1, 'User'])  # Printa as contas em ordem alfabética
        count += 1

    conta = int(input("\nDigite o número do perfil: "))
    while (conta < 0) or (conta > len(quantidade_contas)):
        conta = int(input("\nOpção inválida! Tente novamente\n"))
    if conta == 0: return

    i = user_index(quantidade_contas.loc[conta - 1, 'User'])  # Identifica o index do perfil escolhido
    senha = input("Digite a senha: ")
    q = 1
    while (str(senha) != str(df.loc[i, 'Senha'])):
        if q == 3:
            print("\nNão foi possível entrar no perfil")
            return
        q += 1
        senha = input("\n---------------------------\nSenha incorreta!"
                      "\n---------------------------\nDigite novamente: ")
    conta_pessoal(i)
    return 


# In[7]:


#  Interface pessoal
def conta_pessoal(numero_conta):
    opcao = '0'
    while opcao != '7':
        df = dataframe()
        print("\n----------",df.loc[numero_conta, 'User'], "----------\n" + "O que deseja fazer?")
        opcao = input(" 1 - Visualizar Contas Pessoais.\n 2 - Adicionar Conta Pessoal."
                          "\n 3 - Modificar Senhas."
                          "\n 4 - Duplicar uma Conta Pessoal.\n 5 - Deletar uma Conta Pessoal."
                          "\n 6 - Deletar Perfil. \n 7 - Voltar para o Menu Inicial\n\n Escolha uma opção: ")
        while opcao!='1'and opcao!='2'and opcao!='3'and opcao!='4'and opcao!='5'and opcao!='6'and opcao!='7':
            opcao = input("\n Opção inválida! Tente novamente\n Escolha uma opção: ")
        if opcao == '1':
            print("\n---------------------------\n"+"Contas Pessoais:")
            mostrar_emails(numero_conta)
        if opcao == '2':
            print("\n---------------------------")
            adicionar_email(numero_conta)
        if opcao == '3':
            print("\n---------------------------\n"+"Contas Pessoais:")
            modificar_senha(numero_conta)
        if opcao == '4':
            print("\n---------------------------\n"+"Contas Pessoais:")
            duplicar_conta(numero_conta)
        if opcao == '5':
            print("\n---------------------------\n"+"Contas Pessoais:")
            numero_conta = deletar_email(numero_conta)
        if opcao == '6':
            print("\n---------------------------")
            if (deletar_perfil(numero_conta) == True):
                return
    return


# In[8]:


#  Recebe o número do index do perfil e retorna a quantidade de contas pessoais que ele tem
def quantidade_de_contas_pessoais(conta):
    df = dataframe()
    quantidade_contas = df.groupby(['User']).size().reset_index(name='Count')
    i = 0
    while quantidade_contas.loc[i, 'User']  != df.loc[conta, 'User']:
        i += 1
    count = quantidade_contas.loc[i, 'Count']
    return count


# In[9]:


#  Recebe o número do index do perfil selecionado e exibe as suas contas e senhas pessoais
def mostrar_emails(conta):
    df = dataframe()
    count = quantidade_de_contas_pessoais(conta)
    
    j = 0
    i = 0
    while j < count:
        if (str(df.loc[conta, 'User']) == str(df.loc[i, 'User'])):
            if df.loc[i, 'Account'] == 'Sem cadastro' and j == 0:
                print("Não há contas cadastradas!")
                return False
            else:
                print("Conta", j + 1, "-", df.loc[i, 'Account'],
                      " -  Senha:", df.loc[i, 'Password'],
                      " -  Última modificação:", df.loc[i, 'Date'])
                df.loc[i, 'Shield'] = random.randint(1,1000000)
            j += 1
        i += 1
    df = encrypt_decrypt(df, False)
    df.to_csv('C:\Jupyter_Notebook_Python\Div\safe_box.csv', index=False)
    print("\n")
    return True


# In[10]:


#  Recebe o index da conta e adiciona no csv um novo account e password para o usuário
def adicionar_email(conta):
    df = dataframe()      

    i = 0
    while i < len(df) :
        if (df.loc[conta, 'User'] == df.loc[i, 'User']):
            if df.loc[i, 'Account'] == 'Sem cadastro':
                df.loc[i, 'Account'] = input("\nDigite o novo email: ")
                df.loc[i, 'Password'] = input("Digite a senha: ")
                df.loc[i, 'Date'] = str(date.today())
                df = encrypt_decrypt(df, False)
                df.to_csv('C:\Jupyter_Notebook_Python\Div\safe_box.csv', index=False)
                print("\nEmail salvo com sucesso!\n")
                return                
        i += 1
    
    df = df.append({'User' : df.loc[conta, 'User'] , 'Senha' : df.loc[conta, 'Senha'], 
                    'Account' : input("\nDigite a nova conta: ") , 'Password' : input("Digite a senha: "),
                    'Date' : str(date.today()), 'Shield' : random.randint(1,1000000)} , ignore_index=True)
    df.update(df.fillna("Sem cadastro"))
    df = encrypt_decrypt(df, False)
    df.to_csv('C:\Jupyter_Notebook_Python\Div\safe_box.csv', index=False)
    print("\nEmail salvo com sucesso!\n")
    return 


# In[11]:


#  Recebe o index do usuário e modifica no csv a senha de uma das contas dele
def modificar_senha(conta):
    if mostrar_emails(conta) == False:
        return
    senha = int(input("\nQual conta você deseja alterar a senha: "))
    df = dataframe()      
    count = quantidade_de_contas_pessoais(conta)
    
    j = 0
    i = 0
    while j < count:
        if (df.loc[conta, 'User'] == df.loc[i, 'User']):
            if (j + 1 == senha):
                df.loc[i, 'Password'] = input("Nova senha: ")
                df.loc[i, 'Date'] = str(date.today())
                df.loc[i, 'Shield'] = random.randint(1,1000000)
                df = encrypt_decrypt(df, False)
                df.to_csv('C:\Jupyter_Notebook_Python\Div\safe_box.csv', index=False)
                print("\nNova senha salva com sucesso!\n")
                return
            j += 1
        i += 1
    print("\nConta inexistente\n")
    return


# In[12]:


#  Recebe o index do usuário e duplica uma conta pessoal dele
def duplicar_conta(conta):
    if mostrar_emails(conta) == False:
        return

    duplicar = int(input("\nQual conta pessoal você deseja duplicar: "))
    df = dataframe()      
    count = quantidade_de_contas_pessoais(conta)
    
    j = 0
    i = 0
    while j < count:
        if (df.loc[conta, 'User'] == df.loc[i, 'User']):
            if (j + 1 == duplicar):
                df = df.append({'User' : df.loc[i, 'User'] , 'Senha' : df.loc[i, 'Senha'], 
                    'Account' : df.loc[i, 'Account'] , 'Password' : df.loc[i, 'Password'],
                    'Date' : str(date.today()), 'Shield' : random.randint(1,1000000)} , ignore_index=True)
                df.update(df.fillna("Sem cadastro"))
                df = encrypt_decrypt(df, False)
                df.to_csv('C:\Jupyter_Notebook_Python\Div\safe_box.csv', index=False)
                print("\nConta duplicada com sucesso!\n")
                return
            j += 1
        i += 1
    print("\nConta inexistente\n")
    return


# In[13]:


#  Recebe o index do usuário e deleta uma das contas dele
def deletar_email(conta):
    if mostrar_emails(conta) == False:
        return conta

    deletar = int(input("\nQual conta você deseja deletar: "))
    df = dataframe()      
    count = quantidade_de_contas_pessoais(conta)
    user = df.loc[conta, 'User']
    
    j = 0
    i = 0
    while j < count:
        if (str(user) == str(df.loc[i, 'User'])):
            if (j + 1 == deletar):
                if count == 1:
                    df.loc[i, 'Account'] = 'Sem cadastro'
                    df.loc[i, 'Password'] = 'Sem cadastro'
                    df.loc[i, 'Date'] = 'Sem cadastro'
                    df = encrypt_decrypt(df, False)
                    df.to_csv('C:\Jupyter_Notebook_Python\Div\safe_box.csv', index=False)
                    print("\nConta deletada com sucesso!\n")
                    return conta
                
                df = df.drop(df.index[i])  #  Deleta a linha com index i do dataframe
                df.to_csv('C:\Jupyter_Notebook_Python\Div\safe_box.csv', index=False)
                df = pd.read_csv('C:\Jupyter_Notebook_Python\Div\safe_box.csv', encoding='utf-8', dtype=str)
                df = encrypt_decrypt(df, False)
                df.to_csv('C:\Jupyter_Notebook_Python\Div\safe_box.csv', index=False)                
                print("\nConta deletada com sucesso!\n")
                conta = user_index(user)
                return conta
            j += 1
        i += 1
    print("\nConta inexistente")
    return conta    


# In[14]:


#  Recebe o nome do User do usuário e devolve o número do seu index
def user_index(user):
    df = dataframe()
    if type(df) is bool: 
        print("\nConta deletada com sucesso!\n")
        return False
    k = 0
    while k < len(df):
        if(str(user) == str(df.loc[k, 'User'])):
            return k
        k += 1
    print("\nConta deletada com sucesso!\n")
    return False


# In[15]:


#  Recebe o index do usuário e deleta todas as contas dele
def deletar_perfil(conta):
    print("Realmente deseja apagar todos os dados desta conta?\n")
    opcao = input("Digite s/n: ")
    while opcao != 's' and opcao != 'n':
        opcao = input("\n Opção inválida!\n Escolha s/n: ")
    if opcao == 'n': return False
     
    df = dataframe()
    user = df.loc[conta, 'User']
    num = user_index(user)
    
    while type(num) is not bool:
        df = df.drop(df.index[num])
        df.to_csv('C:\Jupyter_Notebook_Python\Div\safe_box.csv', index=False)
        df = pd.read_csv('C:\Jupyter_Notebook_Python\Div\safe_box.csv', encoding='utf-8', dtype=str)
        df = encrypt_decrypt(df, False)
        df.to_csv('C:\Jupyter_Notebook_Python\Div\safe_box.csv', index=False)
        df = dataframe()
        num = user_index(user)    
    return True


# In[16]:


#  Função que criptografa (crip_or_decr = False) e descriptografa (crip_or_decr = True) o dataframe
def encrypt_decrypt(df, crip_or_decr):
    col = ['User','Senha','Account','Password','Date']
    cont = 0
    
    if crip_or_decr is True:
        df.columns = df.columns.str.replace('CR', 'User')
        df.columns = df.columns.str.replace('YP', 'Senha')
        df.columns = df.columns.str.replace('TO', 'Account')
        df.columns = df.columns.str.replace('GR', 'Password')
        df.columns = df.columns.str.replace('AP', 'Date')
        df.columns = df.columns.str.replace('HY', 'Shield')
    
    while cont < len(df):
        cont_total = 0
        while cont_total < 5:   
            matriz = []
            nome = ''
            for palavra in str(df.loc[cont, col[cont_total]]):
                matriz.append(list(palavra))
            
            shield = crip(int(df.loc[cont, 'Shield']))
            shield2 = shield
            if crip_or_decr is True:
                shield = 63 - shield
            
            i = 0
            while i < len(matriz):
                j = 0
                if crip_or_decr is True and shield2 < 58:
                    shield -= shield2 + cont_total + 1
                    if shield < 0: shield = 63 + shield
                if crip_or_decr is False and shield2 < 58:
                    shield += shield2 + cont_total + 1
                    if shield > 63: shield = shield - 63
                while j < shield:
                    matriz[i][0] = codigo(matriz[i][0]) 
                    j += 1
                nome = nome + matriz[i][0]                    
                i += 1                            
            df.loc[cont, col[cont_total]] = nome
            cont_total += 1
        cont += 1
        
    if crip_or_decr is False:
        df.columns = df.columns.str.replace('User', 'CR')
        df.columns = df.columns.str.replace('Senha', 'YP')
        df.columns = df.columns.str.replace('Account', 'TO')
        df.columns = df.columns.str.replace('Password', 'GR')
        df.columns = df.columns.str.replace('Date', 'AP')
        df.columns = df.columns.str.replace('Shield', 'HY')
    
    return df    


# In[17]:


#  Retorna o resto de um número dividido por 63
def crip(num):      
    while num > 63:
        num = num % 63
    if num == 0:
        num = 1
    return num


# In[18]:


#  Modifica 63 simbolos diferentes para a criptografia
def codigo(x): # 63
    if x == 'a': return 'b'
    if x == 'b': return 'c'
    if x == 'c': return 'd'
    if x == 'd': return 'e'
    if x == 'e': return 'f'
    if x == 'f': return 'g'
    if x == 'g': return 'h'
    if x == 'h': return 'i'
    if x == 'i': return 'j'
    if x == 'j': return 'k'
    if x == 'k': return 'l'
    if x == 'l': return 'm'
    if x == 'm': return 'n'
    if x == 'n': return 'o'
    if x == 'o': return 'p'
    if x == 'p': return 'q'
    if x == 'q': return 'r'
    if x == 'r': return 's'
    if x == 's': return 't'
    if x == 't': return 'u'
    if x == 'u': return 'v'
    if x == 'v': return 'w'
    if x == 'w': return 'x'
    if x == 'x': return 'y'
    if x == 'y': return 'z'
    if x == 'z': return 'A'
    if x == 'A': return 'B'
    if x == 'B': return 'C'
    if x == 'C': return 'D'
    if x == 'D': return 'E'
    if x == 'E': return 'F'
    if x == 'F': return 'G'
    if x == 'G': return 'H'
    if x == 'H': return 'I'
    if x == 'I': return 'J'
    if x == 'J': return 'K'
    if x == 'K': return 'L'
    if x == 'L': return 'M'
    if x == 'M': return 'N'
    if x == 'N': return 'O'
    if x == 'O': return 'P'
    if x == 'P': return 'Q'
    if x == 'Q': return 'R'
    if x == 'R': return 'S'
    if x == 'S': return 'T'
    if x == 'T': return 'U'
    if x == 'U': return 'V'
    if x == 'V': return 'W'
    if x == 'W': return 'X'
    if x == 'X': return 'Y'
    if x == 'Y': return 'Z'
    if x == 'Z': return '1'
    if x == '1': return '2'
    if x == '2': return '3'
    if x == '3': return '4'
    if x == '4': return '5'
    if x == '5': return '6'
    if x == '6': return '7'
    if x == '7': return '8'
    if x == '8': return '9'
    if x == '9': return '-'
    if x == '-': return '@'
    if x == '@': return 'a'
    return x


main()

