import json

ARQUIVO_JSON = 'estudantes.json'

def salvar_estudantes(estudantes):
    with open(ARQUIVO_JSON, 'w') as arquivo:
        json.dump(estudantes, arquivo)

def recuperar_estudantes():
    try:
        with open(ARQUIVO_JSON, 'r') as arquivo:
            estudantes = json.load(arquivo)
    except FileNotFoundError:
        estudantes = []
    return estudantes

cadastros = recuperar_estudantes()

def registrar_aluno():
    codigo = input('Digite o codigo:')
    nome = input('Digite o nome completo do aluno: ')
    cpf = input('Digite o cpf do aluno:')
    cadastro = {'Codigo': codigo, 'Nome': nome, 'CPF': cpf}
    cadastros.append(cadastro)
    print('Registro de aluno criado com sucesso.')

def listar_alunos():
    if not cadastros:
        print('Não há cadastros para consultar!')
    else:
        for cadastro in cadastros:
            print('Codigo:', cadastro['Codigo'], ', Nome:', cadastro['Nome'], ', CPF:', cadastro['CPF'])

def alterar_aluno():
    codigo = input('Digite o codigo que deseja alterar: ')
    for cadastro in cadastros:
        if cadastro['Codigo'] == codigo:
            novo_codigo = input('Digite o novo codigo do aluno: ')
            cadastro['Codigo'] = novo_codigo
            print('Codigo alterado com sucesso.')
            break
    else:
        print('Codigo não encontrado.')

def excluir_aluno():
    codigo = input ('Digite o codigo do aluno que desejar excluir:')
    for cadastro in cadastros:
        if cadastro['Codigo'] == codigo:
            cadastros.remove(cadastro)
            print('Dados de aluno excluídos com sucesso.')
            break
    else:
        print('Codigo não encontrado.')

def menu_estudantes():
    while True:
        print('Menu da opção Estudantes:\nSelecione uma das opções abaixo:\n')
        opcao = input('1. Registrar\n2. Listar\n3. Alterar\n4. Excluir\n0. Voltar\n\n')
        if opcao == '1':
            registrar_aluno()
        elif opcao == '2':
            listar_alunos()
        elif opcao == '3':
            alterar_aluno()
        elif opcao == '4':
            excluir_aluno()
        elif opcao == '0':
            salvar_estudantes(cadastros)
            print('Retornando ao menu principal.')
            break
        else:
            print('Opção invalida! Tente novamente.')

ARQUIVO_JSON1 = 'professores.json'  

def salvar_professores(professores):
    with open(ARQUIVO_JSON1, 'w') as arquivo:
        json.dump(professores, arquivo)

def recuperar_professores():
    try:
        with open(ARQUIVO_JSON1, 'r') as arquivo:
            professores = json.load(arquivo)
    except FileNotFoundError:
        professores = []
    return professores

professores = recuperar_professores()

def registrar_professores():
    codigo = int(input('Digite o código:'))
    nome = input('Digite o nome completo: ')
    cpf = input('Digite o CPF :')
    cadastro = {'Codigo': codigo, 'Nome': nome, 'CPF': cpf}
    professores.append(cadastro)
    print('Registro de professor(a) criado com sucesso.')

def listar_professores():
    if not professores:
        print('Não há cadastros para consultar!')
    else:
        for cadastro in professores:
            print('Codigo:', cadastro['Codigo'], ', Nome:', cadastro['Nome'], ', CPF:', cadastro['CPF'])

def alterar_professores():
    codigo = input('Digite o código do professor que deseja alterar: ')
    for cadastro in professores:
        if cadastro['Codigo'] == int(codigo):
            novo_codigo = input('Digite o novo código do professor: ')
            cadastro['Codigo'] = int(novo_codigo)
            print('Código alterado com sucesso.')
            break
    else:
        print('Código não encontrado.')

def excluir_professor():
    codigo = input('Digite o código do professor que deseja excluir: ')
    for cadastro in professores:
        if cadastro['Codigo'] == int(codigo):
            professores.remove(cadastro)
            print('Dados de professor excluídos com sucesso.')
            break
    else:
        print('Código não encontrado.')

def menu_professores():
    while True:
        print('Menu da opção Professores:\nSelecione uma das opções abaixo:\n')
        opcao = input('1. Registrar\n2. Listar\n3. Alterar\n4. Excluir\n0. Voltar\n\n')
        if opcao == '1':
            registrar_professores()
        elif opcao == '2':
            listar_professores()
        elif opcao == '3':
            alterar_professores()
        elif opcao == '4':
            excluir_professor()
        elif opcao == '0':
            salvar_professores(professores)
            print('Retornando ao menu principal.')
            break
        else:
            print('Opção inválida! Tente novamente.')

ARQUIVO_JSON2 = 'disciplinas.json'

def salvar_disciplinas(disciplinas):
    with open(ARQUIVO_JSON2, 'w') as arquivo:
        json.dump(disciplinas, arquivo)

def recuperar_disciplinas():
    try:
        with open(ARQUIVO_JSON2, 'r') as arquivo:
            disciplinas = json.load(arquivo)
    except FileNotFoundError:
        disciplinas = []
    return disciplinas

disciplinas = recuperar_disciplinas()

def cadastrar_disciplina():
    codigo = input('Digite o código da disciplina: ')
    nome = input('Digite o nome da disciplina: ')
    disciplina = {'Codigo': codigo, 'Nome': nome}
    disciplinas.append(disciplina)
    print('Disciplina cadastrada com sucesso.')

def listar_disciplinas():
    if not disciplinas:
        print('Não há disciplinas cadastradas!')
    else:
        for disciplina in disciplinas:
            print('Código:', disciplina['Codigo'], ', Nome:', disciplina['Nome'])

def alterar_disciplina():
    codigo = input('Digite o código da disciplina que deseja alterar: ')
    for disciplina in disciplinas:
        if disciplina['Codigo'] == codigo:
            novo_codigo = input('Digite o novo código da disciplina: ')
            novo_nome = input('Digite o novo nome da disciplina: ')
            disciplina['Codigo'] = novo_codigo
            disciplina['Nome'] = novo_nome
            print('Disciplina alterada com sucesso.')
            break
    else:
        print('Disciplina não encontrada.')

def excluir_disciplina():
    codigo = input('Digite o código da disciplina que deseja excluir: ')
    for disciplina in disciplinas:
        if disciplina['Codigo'] == codigo:
            disciplinas.remove(disciplina)
            print('Disciplina excluída com sucesso.')
            break
    else:
        print('Disciplina não encontrada.')

def menu_disciplinas():
    while True:
        print('Menu da opção Disciplinas:\nSelecione uma das opções abaixo:\n')
        opcao = input('1. Registrar\n2. Listar\n3. Alterar\n4. Excluir\n0. Voltar\n\n')
        if opcao == '1':
            cadastrar_disciplina()
        elif opcao == '2':
            listar_disciplinas()
        elif opcao == '3':
            alterar_disciplina()
        elif opcao == '4':
            excluir_disciplina()
        elif opcao == '0':
            salvar_disciplinas(disciplinas)
            print('Retornando ao menu principal.')
            break
        else:
            print('Opção inválida! Tente novamente.')

ARQUIVO_JSON3 = 'turmas.json'

def salvar_turmas(turmas):
    with open(ARQUIVO_JSON3, 'w') as arquivo:
        json.dump(turmas, arquivo)

def recuperar_turmas():
    try:
        with open(ARQUIVO_JSON3, 'r') as arquivo:
            turmas = json.load(arquivo)
    except FileNotFoundError:
        turmas = []
    return turmas

turmas = recuperar_turmas()

def registrar_turmas():
    codigo = input('Digite o código da turma: ')
    nome = input('Digite o nome da turma: ')
    turma = {'Codigo': codigo, 'Nome': nome}
    turmas.append(turma)  
    print('Registro de Turma criado com sucesso.')

def listar_turmas():
    if not turmas:
        print('Não há turmas cadastradas!')
    else:
        for cadastro in turmas :
            print('Código:', cadastro['Codigo'], ', Nome:', cadastro['Nome'])

def alterar_turmas():
    codigo_turma = input('Digite o código que deseja alterar: ')
    for cadastro in turmas:
        if cadastro['Codigo'] == codigo_turma:
            novo_codigo = input('Digite o novo código da turma: ')
            cadastro['Codigo'] = novo_codigo
            print('Código alterado com sucesso.')
            break
    else:
        print('Código não encontrado.')

def excluir_turmas():
    codigo = input ('Digite o código da turma que deseja excluir:')
    for cadastro in turmas:
        if cadastro['Codigo'] == codigo:
            turmas.remove(cadastro)
            print('Turma excluída com sucesso.')
            break
    else:
        print('Turma não encontrada.')

def menu_turmas():
    while True:
        print('Menu da opção Professores:\nSelecione uma das opções abaixo:\n')
        opcao = input('1. Registrar\n2. Listar\n3. Alterar\n4. Excluir\n0. Voltar\n\n')
        if opcao == '1':
            registrar_turmas()
        elif opcao == '2':
            listar_turmas()
        elif opcao == '3':
            alterar_turmas()
        elif opcao == '4':
            excluir_turmas()
        elif opcao == '0':
            salvar_turmas(turmas)
            print('Retornando ao menu principal.')
            break
        else:
            print('Opção invalida! Tente novamente.')



ARQUIVO_JSON4 = 'matriculas.json'

def salvar_matriculas(turmas):
    with open(ARQUIVO_JSON4, 'w') as arquivo:
        json.dump(matriculas, arquivo)

def recuperar_matriculas():
    try:
        with open(ARQUIVO_JSON4, 'r') as arquivo:
            matriculas = json.load(arquivo)
    except FileNotFoundError:
        matriculas = []
    return matriculas

matriculas= recuperar_matriculas()

def registrar_matriculas():
    codigo = input('Digite o código da turma: ')
    nome = input('Digite o nome da turma: ')
    matricula = {'Codigo': codigo, 'Nome': nome}
    matriculas.append(matricula)  
    print('Registro de Turma criado com sucesso.')

def listar_matriculas():
    if not matriculas:
        print('Não há turmas cadastradas!')
    else:
        for matricula in matriculas :
            print('Código:', matricula['Codigo'], ', Nome:', matricula['Nome'])

def alterar_matriculas():
    codigo_matriculas= input('Digite o código que deseja alterar: ')
    for cadastro in matriculas:
        if cadastro['Codigo'] == codigo_matriculas:
            novo_codigo = input('Digite o novo código da turma: ')
            cadastro['Codigo'] = novo_codigo
            print('Código alterado com sucesso.')
            break
    else:
        print('Código não encontrado.')

def excluir_matriculas():
    codigo = input ('Digite o código da turma que deseja excluir:')
    for cadastro in matriculas :
        if cadastro['Codigo'] == codigo:
            matriculas.remove(cadastro)
            print('Turma excluída com sucesso.')
            break
    else:
        print('Turma não encontrada.')

def menu_matriculas():
    while True:
        print('Menu da opção Professores:\nSelecione uma das opções abaixo:\n')
        opcao = input('1. Registrar\n2. Listar\n3. Alterar\n4. Excluir\n0. Voltar\n\n')
        if opcao == '1':
            registrar_matriculas()
        elif opcao == '2':
            listar_matriculas()
        elif opcao == '3':
            alterar_matriculas()
        elif opcao == '4':
            excluir_matriculas()
        elif opcao == '0':
            salvar_matriculas(matriculas)
            print('Retornando ao menu principal.')
            break
        else:
            print('Opção invalida! Tente novamente.')
            
while True:
    print('Menu principal\n')
    print('Selecione umas das opções abaixo:\n')
    opcao = input('1. Estudantes\n2. Disciplinas\n3. Professores\n4. Turmas\n5. Matriculas.\n6. Sair\n\n')
    if opcao == '1':
        menu_estudantes()
    elif opcao == '2':
        menu_disciplinas()
    elif opcao == '3':
        menu_professores()
    elif opcao == '4':
        menu_turmas()
    elif opcao == '5':
        menu_matriculas()
    elif opcao == '6':
        print('Saindo do programa.')
        break
    else:
        print('Opção invalida! Tente novamente.')
