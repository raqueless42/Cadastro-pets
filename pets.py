def limpar_tela():
    import os
    temp = os.system('cls')




def menu():
    voltarMenu = 's'
    while voltarMenu == 's':
        limpar_tela()
        opcao = input('''
        
    
                                     CADASTRO DE ANIMAIS INTERNOS
        MENU:
    
        [1]CADASTRO DE ANIMAIS
        [2]LISTAR ANIMAIS
        [3]DELETAR ANIMAL
        [4]BUSCAR ANIMAL
        [5]SAIR
    
        ESCOLHA UMA OPÇÃO:
        ''')
        if opcao == "1":
            cadastrarPet()
        elif opcao == "2":
            listarPet()
        elif opcao == "3":
            deletarPet()
        elif opcao == "4":
            buscarPet()
        elif opcao == "5":
            sair()
        voltarMenu = input("Voltar ao menu? s/n: ").lower()

def cadastrarPet():
    id = input("Nome do pet: ").capitalize()
    raca = input("Raça do pet: ")
    cor = input("Cor do pet: ")
    especie = input("Espécie: ")
    try:
        cadastro = open("cadastros.txt", "a")
        dados = (f'{id};{raca};{cor};{especie}\n')
        cadastro.write(dados)
        cadastro.close()
        print(f'Pet cadastrado com sucesso!!')

    except:
        print("Erro no cadastro")

def listarPet():
    cadastro = open("cadastros.txt", "r")
    for id in cadastro:
        print(id)
    cadastro.close()

def deletarPet():
    petDeletado = input("Delete: ").capitalize()
    cadastro = open("cadastros.txt", "r")
    aux = []
    aux2 = []
    for i in cadastro:
        aux.append(i)
    for i in range(0, len(aux)):
        if petDeletado not in aux[i].capitalize():
            aux2.append(aux[i])
        cadastro = open("cadastros.txt", "w")
    for i in aux2:
            cadastro.write(i)
    print(f'Pet deletado com sucesso')
    listarPet()

def buscarPet():
    nome = input(f'Digite o nome do pet: ').capitalize()
    cadastro = open("cadastros.txt", "r")
    for id in cadastro:
        if nome in id.split(";")[0].capitalize():
            print(id)
    cadastro.close()

def sair():
    exit()

def main():

    menu()

main()


       


