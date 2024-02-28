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
        inserir(pendentes, 'Voltar')

        while True:
            opc = gerenciador.menu('Tarefas Pendentes', exibir(pendentes), 'Marcar como concluída: ')

            
            if exibir(pendentes)[opc-1] == exibir(pendentes)[-1]:
                break


            elif exibir(pendentes)[opc-1] == exibir(pendentes)[-2]:
                editar(pendentes, leiaint('Editar qual tarefa? ', gerenciador.num_opc-2)-1, input('Qual a nova tarefa? ')+'\n')
                print('Tarefa editada com sucesso')
            

            else:
                inserir(concluidas, exibir(pendentes)[opc-1].replace('\n', ''))
                editar(pendentes, opc-1)
        editar(pendentes, -2)
        editar(pendentes, -1)
    
    elif opc == 3:
        try:
            gerenciador.exibe_lista('Tarefas concluídas', exibir(concluidas))
        except:
            print('Nenhuma tarefa concluída ainda')


    elif opc == 4:
        break
