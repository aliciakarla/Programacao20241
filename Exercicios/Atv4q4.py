Agenda = {}

def IncluiContato(Nome, Telefones):
    if Nome in Agenda:
        print(f"Contato '{Nome}' já existe.")
    else:
        Agenda[Nome] = Telefones
        print(f"Contato '{Nome}' adicionado com sucesso.")
def IncluiTelefone(Nome, Telefone):
    if Nome in Agenda:
        if Telefone not in Agenda[Nome]:
            Agenda[Nome].append(Telefone)
            print(f"Telefone '{Telefone}' adicionado ao contato '{Nome}'.")
        else:
            print(f"Telefone '{Telefone}' já está registrado para o contato '{Nome}'.")
    else:
        print(f"Contato '{Nome}' não encontrado.")
def ExcluiTelefone(Nome, Telefone):
    if Nome in Agenda:
        if Telefone in Agenda[Nome]:
            Agenda[Nome].remove(Telefone)
            if not Agenda[Nome]:
                del Agenda[Nome]
            print(f"Telefone '{Telefone}' removido do contato '{Nome}'.")
        else:
            print(f"Telefone '{Telefone}' não encontrado para o contato '{Nome}'.")
    else:
        print(f"Contato '{Nome}' não encontrado.")
def ExcluiContato(Nome):
    if Nome in Agenda:
        del Agenda[Nome]
        print(f"Contato '{Nome}' removido da agenda.")
    else:
        print(f"Contato '{Nome}' não encontrado.")
def ConsultaTelefone(Nome):
    if Nome in Agenda:
        return Agenda[Nome]
    else:
        return f"Contato '{Nome}' não encontrado."
def menu():
    while True:
        print("\nMenu:")
        print("1. Incluir Contato")
        print("2. Incluir Telefone")
        print("3. Excluir Telefone")
        print("4. Excluir Contato")
        print("5. Consultar Telefone")
        print("6. Sair")

        opcao = input("Escolha uma opção (1-6): ")
        if opcao == '1':
            Nome = input("Digite o nome do contato: ")
            Telefones = input("Digite os telefones separados por vírgula: ").split(',')
            Telefones = [tel.strip() for tel in Telefones]
            IncluiContato(Nome, Telefones)
        elif opcao == '2':
            Nome = input("Digite o nome do contato: ")
            Telefone = input("Digite o telefone a ser adicionado: ")
            IncluiTelefone(Nome, Telefone)
        elif opcao == '3':
            Nome = input("Digite o nome do contato: ")
            Telefone = input("Digite o telefone a ser removido: ")
            ExcluiTelefone(Nome, Telefone)
        elif opcao == '4':
            Nome = input("Digite o nome do contato a ser removido: ")
            ExcluiContato(Nome)
        elif opcao == '5':
            Nome = input("Digite o nome do contato: ")
            Telefones = ConsultaTelefone(Nome)
            if isinstance(Telefones, list):
                print(f"Telefones de '{Nome}': {', '.join(Telefones)}")
            else:
                print(Telefones)
        elif opcao == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 6.")

menu()
