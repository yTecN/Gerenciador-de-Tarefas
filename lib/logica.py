def leiaint(msg=str, max=1):
    while True:
        n = input(msg)
        try:
            int(n)
        except (TypeError, ValueError):
            print('Erro! Digite um número inteiro válido!')
        else:
            if int(n) > max or int(n) < 1:
                print('Erro! Por favor insira uma opção válida!')
            else:
                return int(n)


def exibir(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='UTF-8') as file:
        return file.readlines()


def inserir(nome_arquivo, item):
    with open(nome_arquivo, 'a', encoding='UTF-8') as file:
        file.write(item+'\n')
        file.seek(0, 2)


def editar(nome_arquivo, numero_linha, novo_item=''):
    with open(nome_arquivo, 'r') as file:
        lines = file.readlines()


    with open(nome_arquivo, 'w') as file:
        for index, line in enumerate(lines, start=1):
            if lines[numero_linha] == line:
                file.write(novo_item)
            else:
                file.write(line)
