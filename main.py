import lib.formatar as formatar
from lib.logica import *

gerenciador = formatar.formatar()
pendentes = 'pendentes.txt'
concluidas = 'concluidas.txt'


while True:
    opc = gerenciador.menu('Gerenciador de tarefas', ['Adicionar tarefa', 'Ver tarefas pendentes', 'Ver tarefas concluídas', 'Sair'])

    # Adicionar Tarefa

    if opc == 1:
        inserir(pendentes, input('Digite a nova tarefa: '))
        print('Tarefa adicionada com sucesso')


    elif opc == 2:
        inserir(pendentes, 'Editar')
        
        opc = gerenciador.menu('Tarefas Pendentes', exibir(pendentes), 'Marcar como concluída: ')

        editar(pendentes, -1)

    
    elif opc == 3:
        gerenciador.exibe_lista('Tarefas concluídas', exibir(concluidas))


    elif opc == 4:
        break
