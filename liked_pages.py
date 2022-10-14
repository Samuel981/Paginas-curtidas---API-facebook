import access_token as tk
import sys
import requests
import socket
import os
afddress = 'www.facebook.com'

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')


def clear(): return os.system('cls')


estilo = {'default': '\033[m', 'bold': '\033[1m'}


def soc():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # print("Socket criado")
    except socket.error as e:
        print("Falha na criacao do socket", (e))

    address = 'https://graph.facebook.com/'
    try:
        host_ip = socket.gethostbyname(afddress)
    except socket.gaierror:
        print("Erro no host")
        sys.exit()

    s.connect((host_ip, 80))
    # print("O socket conectou com o FB:", (host_ip))
    try:
        s.send(b"GET / HTTP/1.1\r\nHost:www.facebook.com\r\n\r\n")
    except Exception as e:
        print(e)
    response = s.recv(4096)
    s.close()
    # print(response.decode())


def likes_categoria():
    clear()
    print('\n----- LISTANDO CATEGORIAS -----\n')
    try:
        response = requests.get(
            'https://graph.facebook.com/me?fields=likes.limit(65){name, category}&access_token='+tk.ACCESS_TOKEN)
        responsejson = response.json()
        mylikes = responsejson['likes']['data']
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
            print('{}{}{}'.format(estilo['bold'],
                  str(i), estilo['default']), end="")
            print(espacador+categoria)
            i += 1
        opcaoCatg = int(input('Categoria (digite o número correspondente): '))
        clear()
        selecionada = categorias[opcaoCatg-1]
        print(str(opcaoCatg)+' - ', end="")
        print('{}{}{}'.format(estilo['bold'],
                              selecionada, estilo['default']))
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
    print('{}\n----- LISTANDO PAGINAS POR CATEGORIA -----{}\n'.format(
        estilo['bold'], estilo['default']))
    try:
        response = requests.get(
            'https://graph.facebook.com/me?fields=likes.limit('+limite+'){name, category}&access_token='+tk.ACCESS_TOKEN)
        responsejson = response.json()
        mylikes = responsejson['likes']['data']
        # for like in mylikes:
        #     print(like['name'])
        categorias = []
        for like in mylikes:
            categoriaResposta = like['category']
            if categoriaResposta not in categorias:
                categorias.append(like['category'])

        categorias.sort()
        lista = []
        for categoria in categorias:
            print('{}{}{}'.format(estilo['bold'],
                  categoria, estilo['default']))
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
    print('\n1 - Listar páginas de uma categoria \n2 - Listar todas as páginas por categoria\n3 - Sair\n')
    opcao = int(input('Opção: '))
    if opcao == 1:
        likes_categoria()
    elif opcao == 2:
        likes()
    else:
        print('Saindo...')
        exit()


clear()
soc()
print("{}Aplicação de coleta e organização de paginas do Facebook{}".format(
    estilo['bold'], estilo['default']))
menu()
