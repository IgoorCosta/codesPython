#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import os
import re
from datetime import date


# In[2]:


# Interface inicial
def main(): 
    opcao = '1'
    while opcao != '6':
        print("\n-------- English --------\n\n"
              " 1 - View all words.\n 2 - Search word."
              "\n 3 - Add word.\n 4 - Delete word.\n 5 - Load file.\n 6 - Exit.")
        opcao = input(" Enter an option: ")
        while opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4' and opcao != '5' and opcao != '6' and opcao != 'DATAFRAME' and opcao != 'DATAFRAME2':
            print("\nInvalid option! Enter an option: ")
            opcao = input()
        if opcao == '1':
            print("\n-------- English --------\n")
            mostrar_palavras()
            
        if opcao == '2':
            print("\n-------- English --------\n")
            word = input("\nWhat word do you want to search:")
            encontrar_palavra(word)
            
        if opcao == '3':
            print("\n-------- English --------\n")
            df = dataframe(1)
            w = input("New Word: ")
            c = input("\n1 - Noun.\n2 - Adjective.\n3 - Verb.\n4 - Adverb.\n5 - Preposition."
                      "\n6 - Conjuction.\n7 - Pronoun.\n8 - Interjection.\n9 - Article.\n10 - Text.\n\nWhich class does the word belong to: ") 
            if c == "1": cl = "noun"
            elif c == "2": cl = "Adjective"
            elif c == "4": cl = "Adverb"
            elif c == "5": cl = "Preposition"
            elif c == "6": cl = "Conjuction"
            elif c == "7": cl = "Pronoun"
            elif c == "8": cl = "Interjection"
            elif c == "3": cl = "Verb"
            elif c == "9": cl = "Article"
            if c == "10": 
                cl = "text"
                df = df.append({'Words' : w, 'Class' : cl,'Translations' : input("Text: "),
                            'Times' : 1, 'Date' : str(date.today())} , ignore_index=True)
            
            else: df = df.append({'Words' : w, 'Class' : cl,'Translations' : input("Translation: "),
                            'Times' : 1, 'Date' : str(date.today())} , ignore_index=True)
            df.to_csv('C:\Jupyter_Notebook_Python\Div\English.csv', index=False)
            
        if opcao == '4':
            print("\n-------- English --------\n")
            deletar_palavra()
            
        if opcao == '5':
            print("\n-------- English --------\n")
            compara()
            
        if opcao == 'DATAFRAME':  
            df = dataframe(1)
            print (df)
        if opcao == 'DATAFRAME2': 
            df = le_texto()
            print (df)
            
    print("\n-------- English --------\n")
    return


# In[4]:


def dataframe(opc):
    if (not os.path.exists('C:\Jupyter_Notebook_Python\Div') or not os.path.exists('C:\Jupyter_Notebook_Python\Div\English.csv')):  # Caso não exista o diretório ou o csv
        if not os.path.exists('C:\Jupyter_Notebook_Python\Div'):
            os.mkdir('C:\Jupyter_Notebook_Python\Div')
        df = pd.DataFrame(columns = ['Words','Class', 'Translations', 'Times', 'Date'])
        df.to_csv('C:\Jupyter_Notebook_Python\Div\English.csv', index=False)
            
    df = pd.read_csv('C:\Jupyter_Notebook_Python\Div\English.csv', encoding='utf-8', dtype=str)
    df.update(df.fillna("No Record"))
    df = df.apply(lambda x: x.astype(str).str.lower())
    if (opc == 1 or opc == 5):
        dx = df.sort_values(by='Words', ignore_index=True)
    if (opc == 2):
        dx = df.sort_values(by='Class', ignore_index=True)
    if (opc == 3):
        dx = df.sort_values(by='Times', ascending=False, ignore_index=True)
    if (opc == 4):
        dx = df.sort_values(by='Date', ascending=False, ignore_index=True)
    
    return dx


# In[5]:


def dataframe2():
    if (not os.path.exists('C:\Jupyter_Notebook_Python\Div') or not os.path.exists('C:\Jupyter_Notebook_Python\Div\Texto.txt')):  # Caso não exista o diretório ou o csv
        if not os.path.exists('C:\Jupyter_Notebook_Python\Div'):
            os.mkdir('./Div')
        df = pd.DataFrame(columns = ['Cole o texto aqui embaixo:'])
        df.to_csv('C:\Jupyter_Notebook_Python\Div\Texto.txt', index=False)
            
    df = pd.read_csv('C:\Jupyter_Notebook_Python\Div\Texto.txt', encoding='utf-8', dtype=str, delimiter = "\t")
    df = df.apply(lambda x: x.astype(str).str.lower())
    return df


# In[6]:


def le_texto():
    df= dataframe2()

    sentenca = []
    frase = []
    palavras = []
    w = []
    a = 0
    while a < len(df):
        b = 0
        sentenca = separa_sentencas(df.loc[a, 'Cole o texto aqui embaixo:'])
        while b < len(sentenca):
            c = 0
            frase = separa_frases(sentenca[b])
            while c < len(frase):
                d = 0
                palavras = separa_palavras(frase[c])
                while d < len(palavras):
                    
                    x = palavras[d].replace('.', '').replace('ç', 'c').replace('ô', 'o').replace('é', 'e').replace('\"','')
                    x = x.replace('—','').replace('”','').replace('“','').replace('”	','').replace('–','')
                    x = x.replace('?','').replace('!','').replace('‘','').replace('’','').replace('(','').replace(')','')
                    x = x.replace('-','').replace('0','').replace('1','').replace('2','').replace('3','').replace('4','')
                    x = x.replace('5','').replace('6','').replace('7','').replace('8','').replace('9','').replace('*','')
                    x = x.replace('&','').replace('%','').replace('$','').replace('[','').replace(']','').replace('±','')
                    x = x.replace("'",'').replace('#','').replace('@','').replace('°','').replace('ª','').replace('σ','')
                    if x != "":
                        w.append(x)
                    d += 1
                c += 1
            b += 1
        a += 1
        
    dn = pd.DataFrame(columns = ['Text'])
    dn.loc[:,'Text'] = w
    ds = dn.groupby(['Text']).size().reset_index(name='Count')
    ds = ds.sort_values(by='Count', ascending=False, ignore_index=True)
    return ds


# In[7]:


def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?\']-—+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;"]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()


# In[8]:


def mostrar_palavras():
    x = int(input("Do you want to view:\n 1 - Alphabetically\n 2 - Class\n 3 - Times viewed\n 4 - Date\n 5 - Text\n\nEnter an option: "))
    print("\n")
    df = dataframe(x)
    
    if df.empty is True:  # Verifica se o dataframe não está vazio
        print("\nThere is no vocabulary on this computer.\n")
        return False
    
    i = 0
    j = 0
    if x == 5:
         while i < len(df):
            if df.loc[i, 'Class'] == "text":
                print(df.loc[i, 'Words'],"\n ", df.loc[i, 'Translations'], "\n\n")
                j += 1
            i += 1
    else:
        while i < len(df):
            if df.loc[i, 'Class'] != "text":
                print(df.loc[i, 'Words'],
                      " - Class:", df.loc[i, 'Class'],
                      " -  Translation:", df.loc[i, 'Translations'],
                      " - Times searched :", df.loc[i, 'Times'],
                      " - Date:", df.loc[i, 'Date'])
                j += 1
            i += 1
    
    print("\nTotal:", j)
        
    print("\n")
    return True


# In[9]:


def encontrar_palavra(word):
    df = dataframe(1)
    if df.empty is True:  # Verifica se o dataframe não está vazio
        print("\nThere is no vocabulary on this computer.\n")
        return False
    
    i = 0
    while i < len(df):
        if (word == str(df.loc[i, 'Words'])):
            df.loc[i, 'Times'] = int(df.loc[i, 'Times']) + 1
            
            print("Known Word:\n")
            print("Word -", df.loc[i, 'Words'],
                  " - Class:", df.loc[i, 'Class'],
                  " -  Translation:", df.loc[i, 'Translations'],
                  " -  Times searched:", df.loc[i, 'Times'], 
                  " - Date:", df.loc[i, 'Date'], "\n")
            df.to_csv('C:\Jupyter_Notebook_Python\Div\English.csv', index=False)
            return i
        i += 1
    print("\nUnknown word")
    print("\n")
    return False


# In[10]:


def compara():
    op = int(input("Do you want to download the file via terminal (1) or via .txt (2)? "))
    if (op != 1 and op != 2):
        return
    if op == 1:
        text = input("Copy and paste the text here: \n")
        if (not os.path.exists('./Div')): 
            os.mkdir('./Div')
        df = pd.DataFrame(columns = ['Cole o texto aqui embaixo:'])
        df.loc[0, 'Cole o texto aqui embaixo:'] = text
        df.to_csv('C:\Jupyter_Notebook_Python\Div\Texto.txt', index=False)
    else: 
        print("Copy and paste the text into the 'Texto.txt' file!")
        input("\nClick enter when finished: \n")        
    
    print("\n------------- English -------------\n")
    dtexto = le_texto()
    df = dataframe(1)
    dn = pd.DataFrame(columns = ['Words', 'Count'])
    
    count = 0
    i = 0
    while i < len(dtexto):
        j = 0
        yes = 0
        while j < len(df):
            if (dtexto.loc[i, 'Text'] == df.loc[j, "Words"]):
                yes = 1
            j += 1
        if (yes == 0):
            dn.loc[count, 'Words'] = dtexto.loc[i,'Text']
            dn.loc[count, 'Count'] = dtexto.loc[i,'Count']
            count += 1
        i += 1
    
    print("Exist", (len(dtexto) - count), "familiar words of", len(dtexto),
          " - ", (len(dtexto) - count)/len(dtexto)*100, "%")
    d = int(input("\nHow many words do you want to know? "))
    print("\n\n")
    i = 0
    while i < d:
        print("Word", i + 1, "-", dn.loc[i, 'Words'],
              " -  Count:", dn.loc[i, 'Count'])
        i += 1
        if i == len(dn):
            return dn
    return dn


# In[11]:


def deletar_palavra():
    deletar = input("\nWhat word do you want to delete: ")
    w = encontrar_palavra(deletar)
    if type(w) is bool:
        return 
    
    df = dataframe(1)      
    df = df.drop(df.index[w])
    df.to_csv('C:\Jupyter_Notebook_Python\Div\English.csv', index=False)
    print("\nWord deleted successfully!\n")
    return

main()



