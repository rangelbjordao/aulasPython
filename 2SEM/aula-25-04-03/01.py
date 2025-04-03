import cx_Oracle


def pega_credenciais():
    # em vez de pegar por input, pode colocar suas credenciais aqui direto
    print('Insira suas credenciais no Oracle da FIAP!')
    user = 'RM560547'
    senha = '270900'
    return user, senha


def abre_conexao(user, senha):
    # dsn é "data source name", um descritor de onde vamos acessar o BD
    dsn = cx_Oracle.makedsn(host='oracle.fiap.com.br',
                            port=1521, service_name='ORCL')
    return cx_Oracle.connect(user, senha, dsn)


def busca_tudo(cursor, tabela):
    query = f'SELECT * FROM {tabela}'
    cursor.execute(query)
    return cursor.fetchall()  # pega todos os resultados da query acima!


def insere_funcionario(cursor, pessoa):
    # pessoa é dicionário com campos "id", "nome" e "ano_ingresso"
    query = f"""
        INSERT INTO funcionarios(id, nome, ano_ingresso)
        VALUES (:1, :2, :3)
    """
    cursor.execute(
        query, (pessoa['id'], pessoa['nome'], pessoa['ano_ingresso']))


def main():
    user, senha = pega_credenciais()
    try:
        conexao = abre_conexao(user, senha)
        print(f'Conexão bem-sucedida com user {conexao.username} do BD.')
    except Exception as e:
        print('Erro ao conectar com o BD Oracle:', {e})
        exit()

    cursor = conexao.cursor()

    em_execucao = True
    while em_execucao:
        print('Escolha uma das opções:')
        print('1 - Mostrar dados existentes')
        print('2 - Inserir novo dado (funcionário)')
        print('3 - Encerra o programa')

        opcao = input('Opção: ')

        if opcao == '1':
            resultados = busca_tudo('funcionarios')
            for resultado in resultados:
                print(resultado)

        elif opcao == '2':
            print('Insira as informacoees para inserir no banco:')
            pessoa = {
                'id': int(input('ID: ')),
                'nome': input('Nome: '),
                'ano_ingresso': int(input('Ano de ingresso: '))
            }
            insere_funcionario(cursor, pessoa)
            conexao.commit()

        else:
            em_execucao = False

    cursor.close()
    conexao.close()


main()
