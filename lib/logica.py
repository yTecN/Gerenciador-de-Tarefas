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


# def cria_pendentes():
#     pass


# def cria_concluidas():
#     pass


# def adiciona():
#     pass


# def remove():
#     pass