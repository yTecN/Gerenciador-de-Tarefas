import lib.formatar as formatar
from lib.logica import *

gerenciador = formatar.formatar()
gerenciador.pendentes = ['Lavar louça', 'Tomar banho', 'Guardar louça', 'Voltar']


while True:
    opc = gerenciador.menu('Gerenciador de tarefas', ['Adicionar tarefa', 'Ver tarefas pendentes', 'Ver tarefas concluídas', 'Sair'])

    # Adicionar Tarefa

    if opc == 1:
        gerenciador.pendentes.insert(-1, input('Digite a nova tarefa: ').strip())
        print('Tarefa adicionada com sucesso')


    elif opc == 2:
        gerenciador.pendentes.insert(-1, 'Editar lista')
        while True:
            opc = gerenciador.menu('Tarefas Pendentes', gerenciador.pendentes, 'Marcar como concluída: ')
            if opc-1 == gerenciador.pendentes.index('Voltar'):
                break
            elif opc-1 == gerenciador.pendentes.index('Editar lista'):
                task = leiaint('Qual tarefa você deseja editar? ', len(gerenciador.pendentes))
                gerenciador.pendentes[task-1] = input('Nova tarefa: ')
            else:
                gerenciador.concluidas.append(gerenciador.pendentes[opc-1])
                gerenciador.pendentes.pop(opc-1)
        gerenciador.pendentes.pop(gerenciador.pendentes.index('Editar lista'))
    
    # elif opc == 3:
    #         gerenciador.pendentes[-1] = 'Cancelar'
    #         opc = gerenciador.menu('Tarefas Pendentes', gerenciador.pendentes, 'Selecione para editar: ')
    #         if gerenciador.pendentes[opc-1] == gerenciador.pendentes[-1]:
    #             pass
    #         else:
    #             gerenciador.pendentes[opc-1] = input('Nova Tarefa: ')
    #             print('Alterado com sucesso')
    #         gerenciador.pendentes[-1] = 'Voltar'

    
    elif opc == 3:
        gerenciador.exibe_lista('Tarefas concluídas', gerenciador.concluidas)


    elif opc == 4:
        break