from lib.logica import leiaint

class formatar():
    def __init__(self):
        self.num_opc = 0

    def cabecalho(self, txt='Cabeçalho'):
        print('-'*35)
        print(txt.center(35))
        print('-'*35)


    def menu(self, tittle='Menu', items=list, msg='Escolha uma opção: '):
        self.cabecalho(tittle)
        self.num_opc = len(items)
        for i, v in enumerate(items):
            print(f'[ {i+1} ] {v.replace('\n', '')}')
        print('-'*35)
        return leiaint(msg, self.num_opc)
    
    
    def exibe_lista(self, tittle='Lista', items=list):
        self.cabecalho(tittle)
        for v in items:
            print(v)
        print('-'*35)
        input('Pressione ENTER para voltar...')



    