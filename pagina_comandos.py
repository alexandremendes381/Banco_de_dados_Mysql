from pastabase.conn import DbConnection

continuar = True
while continuar == True:
    
    print('TABELA DE GERENCIAMENTO DE PESSOAS')

    menu = """
    (1) adicionar clientes

    (2) excluir clientes 
    """
    print(menu)


    modalidade = int(input('Qual das opções acima deseja utilizar ? '))
    if modalidade > 2:
        print('Opção inexistente')

    if modalidade == 1:
        print('Adicionar clientes')
        nome = str(input('Qual a nome ? '))
        idade = int(input('Qual idade ? '))
        sexo = str(input('Qual sexo ? '))
        peso = float(input('Qual peso ? '))
        altura = float(input('Qual altura ? '))
        nacionalidade = str(input('Qual nacionalidade ? '))

        app = DbConnection()
        app.insert(nome=nome, nacionalidade=nacionalidade, altura=altura, peso=peso, idade=idade, sexo=sexo)
        print('PRODUTO ADICIONADO AO ESTOQUE COM SUCESSO')
    

    if modalidade == 2:
        print('excluir cliente')
        nome = str(input('Qual cliente gostaria de excluir ? '))
        app = DbConnection()
        app.delete(nome)
        print('exclusão feita com sucesso')
    
    recebe = int(input('gostaria de fazer novamente ?\n 1 (sim)\n 2 (não)\n : '))
    print('ok')
    if recebe == 1:
        continuar = True
        print(' iremos reiniciar o sistema')
     
    elif recebe == 2:
        continuar = False
        print('ok obrigado')
    