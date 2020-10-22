'''
Faça uma lista de tarefas com as seguintes opções:
    add tarefa;
    listar tarefas;
    opção de desfazer (a cada vez que chamarmos, desfaz a ultima açao)
    opção de refazer (a cada vez que chamarmos, desfaz a ultima açao)
    ex:
        ['Tarefa1','Tarefa2']
        ['Tarefa1] <- desfazer
        ['Tarefa1','Tarefa2']<- refazer

        input <- nova tarefa

'''
#undo = desfazer
#redo = refazer
#ls = listar

def show_op(tarefa_list):
    print()
    print('Tarefas: ')
    print(tarefa_list)
    print()

def do_undo(tarefa_list, redo_list):
    if not tarefa_list:
        print('Nada a desfazer')
        return
    last_tarefa = tarefa_list.pop()
    redo_list.append(last_tarefa)


def do_redo(tarefa_list, redo_list):
    if not redo_list:
        print('Nada a refazer')
        return
    last_redo = redo_list.pop()
    tarefa_list.append(last_redo)


def do_add(tarefa, tarefa_list):
    tarefa_list.append(tarefa)


if __name__ =='__main__':
    tarefa_list = []
    redo_list = []

    while True:
        tarefa = input('Digite uma tarefa ou undo, redo, ls: ')

        if tarefa == 'ls':
            show_op(tarefa_list)
            continue
        elif tarefa == 'undo':
            do_undo(tarefa_list, redo_list)
            continue
        elif tarefa == 'redo':
            do_redo(tarefa_list, redo_list)
            continue
        do_add(tarefa, tarefa_list)























