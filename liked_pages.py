from ensurepip import version
from pickle import TRUE
import urllib3
import facebook
import requests
import access_token as token
import os
import sys

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

# Inicializadno o objeto
try:
    graph = facebook.GraphAPI(token.ACCESS_TOKEN, version=3.1)
    myfbgraph = facebook.GraphAPI(token.ACCESS_TOKEN)
except Exception as e:
    print(e)


def clear(): return os.system('cls')


def likes_categoria():
    clear()
    print('\n----- LISTANDO CATEGORIAS -----\n')
    try:
        mylikes = myfbgraph.get_connections(
            id="me", connection_name="likes", fields="name,category", limit=60)['data']
        # Dividir categorias
        categorias = []
        for like in mylikes:
            categoriaResposta = like['category']
            if categoriaResposta not in categorias:
                categorias.append(like['category'])

        i = 1
        categorias.sort()
        for categoria in categorias:
            espacador = ' - '
            if i < 10:
                espacador = '  - '
            print(str(i)+espacador+categoria)
            i += 1
        opcaoCatg = int(input('Categoria: '))
        clear()
        selecionada = categorias[opcaoCatg-1]
        print(str(opcaoCatg)+' - '+selecionada)
        print('-'*40)
        lista = []
        for like in mylikes:
            if like['category'] == selecionada:
                # adiciona paginas na lista
                lista.append(like['name'])
            # ordena paginas
            lista.sort()
            # lista paginas daquela categoria
        for elemento in lista:
            print(elemento)
        print('\n')

    except Exception as e:
        print(e)
    menu()


def likes():
    clear()
    limite = input('Limite a quantidade de páginas (0-100): ')
    clear()
    print('\n----- LISTANDO PAGINAS POR CATEGORIA -----\n')
    try:
        mylikes = myfbgraph.get_connections(
            id="me", connection_name="likes", fields="name,category", limit=limite)['data']
        # for like in mylikes:
        #     print(like['name'], like['category'])
        # Dividir categorias
        categorias = []
        for like in mylikes:
            categoriaResposta = like['category']
            if categoriaResposta not in categorias:
                categorias.append(like['category'])

        categorias.sort()
        lista = []
        for categoria in categorias:
            print(categoria)
            print('-'*40)
            for like in mylikes:
                if like['category'] == categoria:
                    # adiciona paginas na lista
                    lista.append(like['name'])
            # ordena paginas
            lista.sort()
            # lista paginas daquela categoria
            for elemento in lista:
                print(elemento)
            print('\n')
            lista.clear()
    except Exception as e:
        print(e)
    menu()


def menu():
    print('\n1 - Listar páginas de uma categoria específica\n2 - Listar todas as páginas por categoria\n3 - Sair\n')
    opcao = int(input('Opção: '))
    if opcao == 1:
        likes_categoria()
    elif opcao == 2:
        likes()
    else:
        print('Saindo...')
        exit()


clear()
print("Aplicação de coleta e organização de paginas do Facebook")
menu()
