print("Bem-vindo, esse é o sistema de software de gerenciamento de Contatos Comerciais!")  # [EXIGÊNCIA DE CÓDIGO 1 de 8]
print("Desenvolvido por Alan Teixeira Freires.")

lista_contatos = []  # [EXIGÊNCIA DE CÓDIGO 2 de 8] e [EXIGÊNCIA DE CÓDIGO 7 de 8]
id_global = 5568119  # [EXIGÊNCIA DE CÓDIGO 2 de 8]

def cadastrar_contato(id_para_usar):  # [EXIGÊNCIA DE CÓDIGO 3 de 8]
    nome = input("Digite o nome: ")
    atividade = input("Digite a atividade: ")
    telefone = input("Digite o telefone: ")
    
    contato = {
        "id": id_para_usar,
        "nome": nome,
        "atividade": atividade,
        "telefone": telefone
    }
    lista_contatos.append(contato.copy())  # Usando copy() como exigido
    print("Contato cadastrado com sucesso!")

def consultar_contatos():  # [EXIGÊNCIA DE CÓDIGO 4 de 8]
    while True:
        print("\n--- Menu de Consulta ---")
        print("1. Consultar Todos")
        print("2. Consultar por Id")
        print("3. Consultar por Atividade")
        print("4. Retornar ao menu")
        
        opcao_consulta = input("Escolha a opção: ")
        
        if opcao_consulta == "1":
            if not lista_contatos:
                print("Nenhum contato cadastrado.")
            else:
                for contato in lista_contatos:
                    print(f"ID: {contato['id']}")
                    print(f"Nome: {contato['nome']}")
                    print(f"Atividade: {contato['atividade']}")
                    print(f"Telefone: {contato['telefone']}\n")
                    
        elif opcao_consulta == "2":
            try:
                id_busca = int(input("Digite o ID para consulta: "))
                encontrado = False
                for contato in lista_contatos:
                    if contato["id"] == id_busca:
                        print(f"Contato encontrado:")
                        print(f"ID: {contato['id']}")
                        print(f"Nome: {contato['nome']}")
                        print(f"Atividade: {contato['atividade']}")
                        print(f"Telefone: {contato['telefone']}")
                        encontrado = True
                        break
                if not encontrado:
                    print("ID não encontrado!")
            except ValueError:
                print("Digite um número válido!")
                
        elif opcao_consulta == "3":
            atividade_busca = input("Digite a atividade para consulta: ")
            encontrados = []
            for contato in lista_contatos:
                if contato["atividade"].lower() == atividade_busca.lower():
                    encontrados.append(contato)
            if not encontrados:
                print("Nenhum contato encontrado com essa atividade.")
            else:
                for contato in encontrados:
                    print(f"\nContato encontrado:")
                    print(f"ID: {contato['id']}")
                    print(f"Nome: {contato['nome']}")
                    print(f"Atividade: {contato['atividade']}")
                    print(f"Telefone: {contato['telefone']}")
                    
        elif opcao_consulta == "4":
            return  # Retorna ao menu principal
        else:
            print("Opção inválida!")

def remover_contato():  # [EXIGÊNCIA DE CÓDIGO 5 de 8]
    while True:
        try:
            id_remover = int(input("Digite o ID do contato a ser removido: "))
            for i, contato in enumerate(lista_contatos):
                if contato["id"] == id_remover:
                    lista_contatos.pop(i)
                    print("Contato removido com sucesso!")
                    return
            print("ID inválido! Tente novamente.")
        except ValueError:
            print("Digite um número válido!")

# Menu Principal [EXIGÊNCIA DE CÓDIGO 6 de 8]
print("\n" + "="*60)
print("SISTEMA DE GERENCIAMENTO DE CONTATOS COMERCIAIS")
print("="*60)

while True:
    print("\n--- Menu Principal ---")
    print("1. Cadastrar Contato")
    print("2. Consultar Contato")
    print("3. Remover Contato")
    print("4. Encerrar Programa")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        cadastrar_contato(id_global)
        id_global += 1  # Incrementa o ID global
        
    elif opcao == "2":
        consultar_contatos()
        
    elif opcao == "3":
        remover_contato()
        
    elif opcao == "4":
        print("Encerrando o programa...")
        break
        
    else:
        print("Opção inválida!")