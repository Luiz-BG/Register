usuario = []
id = []

def menu():
    print('******************************************')
    print('[1] Cadastro')
    print('[2] Mostrar Banco de Dados')
    print('[3] Reiniciar pagina')
    print('[4] Buscar usuário')
    print('[0] Sair')
    print('******************************************')

def cadastro():
    usuario_nome = input('Digite seu nome: ')
    usuario_dn = input('Digite sua data de nascimento: ')
    usuario_telefone = input('Digite seu telefone: ')
    usuario_email = input('Digite seu email: ')
    usuario_id1 = int(input('Você é um: \n 1 - Visitante/Atendido/Voluntario \n 2 - Funcionario \n 3 - Doador \nEscolha > [1][2][3]: '))
    usuario_dados = (usuario_nome, usuario_dn, usuario_telefone, usuario_email)
    usuario.append(usuario_dados)  # fixa todos os dados ao array
    if usuario_id1 == 1:
        intercalavel()

    elif usuario_id1 == 2:
        id_usuario = ('Ja é funcionário')
        fun_numero = int(input("Qual o seu ID de trabalho?: "))
        fun_cart = input("Nome do seu surpervisor: ")
        fun_afilial = input("Qual o nome da sua filial de trabalho? \nResposta: ")
        fun_dados = (id_usuario, fun_numero, fun_cart, fun_afilial)
        id.append(fun_dados)
        print('Bem vindo Funcionário')

    elif usuario_id1 == 3:
        id_usuario = ('Doar')
        doa_info = input("Nós agradecemos a sua intenção, usaremos 100% desse dinheiro para a manutenção da ONG, seja para os funcionários, os alunos ou a estrutura da ONG em si, dependendo \nda necessidade, concorda em nos ajudar? (S/N): \n")
        doa_pag = input("Gostaria de pagar com cartão de crédito ou débito? (C/D) \nResposta: ")
        doa_cartao = int(input("Digite o número de seu cartão: "))
        doa_dados = (id_usuario, doa_info, doa_pag, doa_cartao)
        id.append(doa_dados)
        print('Bem vindo Doador')

def intercalavel():
    usuario_id2 = int(input("Defina seu objetivo:\n 1 - Visitar o site\n 2 - Quero me voluntariar\n 3 - Gostaria de ser atendido \nEscolha > [1][2][3]: "))
    if usuario_id2 == 1:
        id_usuario = ('Visitar')
        vis_ft = input("É sua primeira vez no site? (S/N)\nResposta: ")
        vis_origem = input("Por onde conheceu nosso site? \nResposta: ")
        vis_comp = input("Pode compartilhar nossas informações para outras pessoas em redes sociais? Seria de grande agrado (S/N):\nResposta: ")
        vis_dados = (id_usuario, vis_ft, vis_origem, vis_comp)
        id.append(vis_dados)
        print('Bem vindo Visitante')
        retorno()

    elif usuario_id2 == 2:
        id_usuario = ('Voluntariar')
        vol_afi = input("Você possue afinidade com crianças? (S/N): ")
        vol_exp = input("Você já trabalhou em uma ONG? Se sim qual?: ")
        vol_resp = input("Você reconhece a responsabilidade que você terá sobre essas crianças? Você esta disposto a isto? (PDF do Termo de responsabilidade da impresa) (S/N): \n")
        vol_dados = (id_usuario, vol_afi, vol_exp, vol_resp)
        print('Bem vindo Voluntário')
        retorno()

    elif usuario_id2 == 3:
        id_usuario = ('Ser Atendido pela ong')
        ate_cpf = int(input("Digite seu cpf completo: "))
        ate_rg = int(input("Digite seu RG completo: "))
        ate_rf = float(input("Digite sua receita familiar: "))
        ate_qntF = int(input("Digite a quantidade de filhos(as) que possue: "))
        ate_escF = input("Seus filho(os) frequenta(am) a escola? (S/N): ")
        ate_dados = (id_usuario, ate_cpf, ate_rg, ate_rf, ate_qntF, ate_escF)
        id.append(ate_dados)
        print('Bem vindo Atendido')
        retorno()

def retorno():
    retorno = int(input("Gostaria de:\n 1 - Ainda se voluntariar/ser atendido\n 0 - Voltar para o menu:\n Escolha > [1][0]: "))
    if retorno == 1:
        intercalavel()

    elif retorno == 0:
        menu()

def banco():
    print('')
    print('Nome, Aniversário, Telefone, Email:')
    print(usuario)
    print('')
    print('Ação principal e Respostas do formulário:')
    print(id)

def busca():
    print('')
    i = input("Escreva o nome do usuário: ")
    for i in usuario:
        print("Usuário encontrado!\n")
        print('Nome, Aniversário, Telefone, Email:')
        print(usuario)
        print('')
        print(id)
menu()
while True:
    x = int(input('Escolha: [1][2][3][4][0]\nResposta: '))
    while x > 4 or x < 0:
        x = int(input('[Erro, tente novamente!] Escolha uma opção: '))
    if x == 1:
        cadastro()
    elif x == 2:
        banco()
    elif x == 3:
        menu()
    elif x == 4:
        busca()
    else:
        break