def editar(nome_arquivo, numero_linha, novo_item=''):
    with open(nome_arquivo, 'r') as file:
        lines = file.readlines()


    with open(nome_arquivo, 'w') as file:
        for index, line in enumerate(lines, start=1):
            if lines[numero_linha] == line:
                file.write(novo_item)
            else:
                file.write(line)

editar('temp.txt', -1, 'batata')
