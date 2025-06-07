# ULTIMA GOTA - PYTHON
# Integrantes:
    # - Thomaz Vasconcelos Mendes - RM564805
    # - Breno Henrique Bortoloti Santos - RM562856
    # - Pedro Henrique dos Santos - RM564188
    
    
# iniciando o sistema e definindo variaveis
# importando a biblioteca datetime para calcular a idade
from datetime import date
import pandas as pd

# configurando o pandas para exibir todo o csv no console
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', 1000)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 200)   # 

contas = [{
"nome": "Teste da Silva",
"cpfCnpj": "00000000000",
"telefone": '11940129027',
"dataNascimento": "26/08/2006",
"email": "teste@gmail.com",
"senha": "senha123"
}] # lista de contas
avatares = [{
     "numero": 1,
     "nome": "Juninho, o ratinho timido"
     },
    {
     "numero": 2,
     "nome": "Marquinhos, o rato rápido "
    },
    {
     "numero": 3,
     "nome": "Cleitinho, o rato forte"
    },
]
usuario = None # variavel para verificar se o usuario esta logado
tema = "padrão" # variavel para definir o tema atual do site
avatarAtual = {
     "numero": 1,
     "nome": "Juninho, o ratinho timido"
 } # variavel para definir qual o avatar atual


print("Olá, seja bem vindo ao sistema do ULTIMA GOTA") 

# função para exibir o menu de opções inicial
def menuInicial():
    global avatarAtual
    print("                                ")
    print("                                ")
    print("                                ")
    print("--------------------------------")
    print("Menu Inicial")
    print("--------------------------------")
    print("                                ")
    print("                                ")
    print("                                ")
    print(" ")
    if usuario is not None:
        print(f"Bem vindo, {usuario['nome']}")
    print(" ")
    print(f"Tema atual: {tema}")
    print(f"Avatar atual: {avatarAtual['nome']}")
    print("--------------------------------")
    print("Para prosseguir, selecione uma opção:")   
    print("1 - Alternar tema")
    if usuario is None:
        print("2 - Cadastrar conta")
        print("3 - Entrar com uma conta")
    else:
        print("2 - Acessar perfil")
        print("3 - Sair")
    print("4 - Acessar seção de explorar")
    print("--------------------------------")
    print("5 - Encerrar sistema")
# Função para alternar o tema do site, aonde pega o novo tema inserido na chamada da função e altera a variavel tema
def alternar_tema():
    while True:
        global tema
        print("                                ")
        print("                                ")
        print("                                ")
        print("--------------------------------")
        print("ALTERNAR TEMA")
        print("--------------------------------")
        print("                                ")
        print("                                ")
        print("                                ")
        print("Tema atual: ", tema)
        print("--------------------------------")
        print("Para prosseguir, selecione uma opção:")
        print("1 - Padrão")
        print("2 - Alternativo")
        print("3 - Escuro")
        try:
            novoTema = int(input("Digite o novo tema: "))
            if(novoTema == 1): # se o novo tema for 1, o tema é alterado para Padrão
                tema = "Padrão"
            elif(novoTema == 2): # se o novo tema for 2, o tema é alterado para Alternativo
                tema = "Alternativo"
            elif(novoTema == 3): # se o novo tema for 3, o tema é alterado para Escuro  
                tema = "Escuro"
            else:
                raise ValueError("Digite uma das opções!")
            menuInicial()
            break
        except ValueError:
            print("                                ")
            print("                                ")
            print("                                ")
            print("--------------------------------")
            print("Número invalido")
            print("--------------------------------")
            print("                                ")
            print("                                ")
            print("                                ")
# Função para cadastrar uma conta
def cadastrar_conta():
    # Função para calcular a idade do usuario, aonde chamo a biblioteca datetime para calcular a idade. Primeiro separo a variavel dataNascimento em dia, mes e ano, e converto para o tipo date com a biblioteca. Verifico a data atual e a data de nascimento do usuario. Declaro a idade como o ano atual menos o ano de nascimento do usuario. Se o mes atual for menor que o mes de nascimento ou o mes atual for igual ao mes de nascimento e o dia atual for menor que o dia de nascimento, subtraio 1 da idade. Por fim, retorno a idade.

    def calcular_idade(dataNascimento):
        # Se a data de nascimento for invalida ou alguns dos itens não forem numeros, retorno 0 e exibo uma mensagem de erro
        try:
            dataNascimento = dataNascimento.split("/")
            dataNascimento = date(int(dataNascimento[2]), int(dataNascimento[1]), int(dataNascimento[0]))
        except ValueError:
            return 0 # se a data de nascimento for invalida, retorno 0
        except IndexError:
            return 0 # se a data de nascimento for invalida, retorno 0
        # Declaro a data atual
        dataHoje = date.today()
        # Declaro a idade como o ano atual menos o ano de nascimento do usuario
        idade = dataHoje.year - dataNascimento.year
        #   Verifico se ele ja fez aniversario esse ano, caso não tenha, subtraio 1 da idade
        if dataHoje.month < dataNascimento.month or (dataHoje.month == dataNascimento.month and dataHoje.day < dataNascimento.day):
            idade -= 1
        return idade
    # valido se o cpf ou cnpj é valido, aonde verifico se o cpf ou cnpj tem 11 ou 14 caracteres. Se tiver, retorno True, caso contrario, retorno False.
    def validar_cpf(cpfCnpj):
        if len(cpfCnpj) == 11:
            return True
        elif len(cpfCnpj) == 14:
            return True
        else:
            return False
    

    # Faço um loop infinito para que o usuario possa inserir os dados da conta
    while True:
        print("                                ")
        print("                                ")
        print("                                ")
        print("--------------------------------")
        print("CADASTRO DE CONTA")
        print("--------------------------------")
        print("                                ")
        print("                                ")
        print("                                ")
        nome = input("Digite o nome da conta: ")
        print(f"Nome: {nome}")
        cpfCnpj = input("Digite o CPF ou CNPJ da conta: ")
        print(f"CPF ou CNPJ: {cpfCnpj}")
        telefone = input("Digite o telefone da conta: ")
        print(f"Telefone: {telefone}")
        dataNascimento = input("Digite a data de nascimento da conta: ")
        print(f"Data de nascimento: {dataNascimento}")
        email = input("Digite o email da conta: ")
        print(f"Email: {email}")
        senha = input("Digite a senha da conta: ")
        print(f"Senha: {senha}")
        # Se algum dos campos estiver vazio, exibo uma mensagem de erro
        if(nome == "" or cpfCnpj == "" or telefone == "" or dataNascimento == "" or email == "" or senha == ""):
            print("Erro: Todos os campos são obrigatórios")
            print("--------------------------------")
        # Se a idade do usuario for menor que 16 anos, exibo uma mensagem de erro
        elif calcular_idade(dataNascimento) == 0:
            print("Erro: Data de nascimento inválida")
            print("--------------------------------")
        # Se a idade do usuario for menor que 16 anos, exibo uma mensagem de erro
        elif calcular_idade(dataNascimento) < 16:
            print("Erro: A conta não pode ser cadastrada pois o usuario é menor de 16 anos")
            print("--------------------------------")
        # Se o cpf ou cnpj não for valido, exibo uma mensagem de erro
        elif not validar_cpf(cpfCnpj):
            print("Erro: CPF ou CNPJ inválido")
            print("--------------------------------")
        # Por fim, depois de todas as validações, exibo uma mensagem de sucesso, adiciono a conta na lista de contas, saio do loop e vou para o login de usuario
        else:
            print("Conta cadastrada com sucesso")
            print("--------------------------------")
            contas.append({
                "nome": nome,
                "cpfCnpj": cpfCnpj,
                "telefone": telefone,
                "dataNascimento": dataNascimento,
                "email": email,
                "senha": senha
            })
            login_conta()
            break
# Função para editar os dados de uma conta
def editar_conta():
    global usuario

    # Defino a variavel global usuario e crio uma função para atualizar o item da lista contas que tenha o msm email
    def atualizar_contas(usuarioNovo):
        global contas
        for conta in contas:
            if(conta['email'] == usuarioNovo["email"]):
                conta = usuarioNovo
    # Faço um loop infinito para que o usuario possa editar os novos dados da conta
    while True:
        print("                                ")
        print("                                ")
        print("                                ")
        print("--------------------------------")
        print("EDITAR PERFIL")
        print("--------------------------------")
        print("                                ")
        print("                                ")
        print("                                ")
        # Peço para o usuario colocar os novos dados do usuario, 
        # faço uma validação para ver se eles não estão vazios, senão estiverem eu atualizo o perfil na variavel usuario e na lista de contas
        nome = input("Digite o novo nome da conta: ")
        print(f"Nome: {nome}")
        telefone = input("Digite o novo telefone da conta: ")
        print(f"Telefone: {telefone}")
        senha = input("Digite a nova senha da conta: ")
        print(f"Senha: {senha}")
        # Se algum dos campos estiver vazio, exibo uma mensagem de erro
        if(nome == "" or telefone == "" or senha == ""):
            print("Erro: Todos os campos são obrigatórios")
            print("--------------------------------")
        # Senão, atualizo o perfil
        else:
            print("Perfil atualizado com sucesso")
            usuario = {
                "nome": nome,
                "cpfCnpj": usuario['cpfCnpj'],
                "telefone": telefone,
                "dataNascimento": usuario['dataNascimento'],
                "email": usuario['email'],
                "senha": senha
            }
            
            atualizar_contas(usuario)
            break
# Função para login de uma conta
def login_conta():
    # Aqui eu crio um loop infinito. Após isso, defino a variavel global usuario e peço para o usuario digitar o email e a senha.
      print("                                ")
      print("                                ")
      print("                                ")
      print("--------------------------------")
      print("ENTRAR NO SISTEMA")
      print("--------------------------------")
      print("                                ")
      print("                                ")
      print("                                ")
      print("Para prosseguir, insira os dados da sua conta:")
      while True:
        global usuario
        email = input("Digite o email da conta: ")
        print(f"Email: {email}")
        senha = input("Digite a senha da conta: ")
        print(f"Senha: {senha}")
        # aqui crio uma conta para verificar se existe algum item da lista contas que tem o msm email que o digitado,
        # Se tiver. ele retorna esse item, senão, retorna None
        def verificar_conta(email):
            for conta in contas:
                if conta["email"] == email:
                    return conta
            return None
        
        conta = verificar_conta(email)
        
        
        
        # Se algum dos campos estiver vazio, exibo uma mensagem de erro
        if email == "" or senha == "":
            print("Erro: Email e senha são obrigatórios")
            print("--------------------------------")
        # Senao existir uma conta exibo um erro
        elif not conta:
            print("Erro: Email inválido")
            print("--------------------------------")
        # Se a senha estiver errada
        elif conta["senha"] != senha:
            print("Erro: Senha inválida")
            print("--------------------------------")
        # Por fim, se ele passar de todas as validações, ele realiza o login e define a variavel global usuario como a conta encontrada
        else:
            print("Login realizado com sucesso")
            print("--------------------------------")
            usuario = conta
            print("--------------------------------")
            break
# Função para finalizar sessão de uma conta
def logout_conta():
    # Eu puxo a variavel global usuario e defino ela igual None
    global usuario
    usuario = None
    print("                                ")
    print("--------------------------------")
    print("Logout realizado com sucesso    ")
    print("--------------------------------")
    print("                                ")
# Função para exibir perfil
def perfil():
    global avatarAtual
    while True:
        if usuario is None:
            menuInicial()
            break
        else:
            print("                                ")
            print("                                ")
            print("                                ")
            print("--------------------------------")
            print("PERFIL")
            print("--------------------------------")
            print("                                ")
            print("                                ")
            print("                                ")
            print("Dados pessoais")
            print(f"Nome: {usuario['nome']}")
            print(f"CPF/CNPJ: {usuario['cpfCnpj']}")
            print(f"Telefone: {usuario['telefone']}")
            print(f"Data de nascimento: {usuario['dataNascimento']}")
            print(f"E-mail: {usuario['email']}")
            print(f"Avatar Atual: {avatarAtual['nome']}")
            print("                                ")
            print("--------------------------------")
            print("O que deseja fazer?")
            print("--------------------------------")
            print("                                ")
            print("1 - Editar Dados")    
            print("2 - Escolher avatar")   
            print("3 - Voltar")
                        
            try:
                opcao = int(input("Digite uma opção: "))
                if opcao == 1:
                    editar_conta()
                elif opcao == 2:
                    escolher_avatar()
                elif opcao == 3:
                    menuInicial()
                    return
            except ValueError:
                print("Digite um número válido!")
            
def escolher_avatar():
    global avatares
    global avatarAtual
    print(" ")
    for avatar in avatares:
        print(f"{avatar['numero']} - {avatar['nome']}")
    print(" ")
    while True:
        try:
            novoAvatar = int(input("Escolha o avatar: "))
            for avatar in avatares:
                if(avatar['numero'] == novoAvatar):
                    avatarAtual = avatar
                    perfil()
                    return
            
            raise ValueError("")
        except ValueError:
            print("Digite um valor válido!") 
# Função para acessar os canais no arquivo csv
def acessarCanais():
    # Lê o CSV de canais (que está no mesmo diretório de index.py)
    canais = pd.read_csv("Canais.csv")
    # Exibe no console
    print("--- Canais--------------------------------")
    print(canais)  # to_string mostra todas as colunas/linhas tabuladas
    print("------------------------------------------")
    input("Pressione Enter para voltar ao menu...")  # pausa para o usuário ler
# Função para acessar as postagens no arquivo csv
def acessarPostagens():
    # Lê o CSV de postagens
    postagens = pd.read_csv("Postagens.csv")
    # Exibe no console
    print("--- Postagens --------------------------------")
    print(postagens)
    print("------------------------------------------")
    input("Pressione Enter para voltar ao menu...") 

def acessar_canal_especifico():
    df_canais = pd.read_csv("Canais.csv")
    termo = input("Digite o nome exato do canal: ").strip()
    resultado = df_canais[df_canais["título"].str.lower() == termo.lower()]
    if resultado.empty:
        print(f"Nenhum canal encontrado com nome '{termo}'.")
    else:
        print("\nInformações completas do canal:\n")
        print(resultado.to_string(index=False))
    input("\nPressione Enter para voltar...")

def acessar_postagem_especifica():
    df_postagens = pd.read_csv("Postagens.csv")
    termo = input("Digite o nome exato da postagem: ").strip()
    resultado = df_postagens[df_postagens["título"].str.lower() == termo.lower()]
    if resultado.empty:
        print(f"Nenhuma postagem encontrada com nome '{termo}'.")
    else:
        print("\nInformações completas da postagem:\n")
        print(resultado.to_string(index=False))
    input("\nPressione Enter para voltar...")

# função para pesquisar as postagens no arquivo csv
def pesquisar():
    # carrega ambos os CSVs só uma vez
    df_canais = pd.read_csv("Canais.csv")
    df_postagens = pd.read_csv("Postagens.csv")

    while True:
        print("O que você quer pesquisar?")
        print("1 – Canais")
        print("2 – Postagens")
        print("3 – Voltar")
        opcao = input("Digite a opção: ")
        if opcao == "1":
            termo = input("Digite palavra-chave para título de canal: ").strip()
            
            resultado = df_canais[df_canais["título"].str.contains(termo, case=False, na=False)]
            print(f"\nCanais encontrados para '{termo}':")
            if resultado.empty:
                print("  — nenhum canal encontrado.")
            else:
                print(resultado.to_string(index=False))
            input("\nPressione Enter para continuar...")
        elif opcao == "2":
            termo = input("Digite palavra-chave para título de postagem: ").strip()
            resultado = df_postagens[df_postagens["título"]
                                     .str.contains(termo, case=False, na=False)]
            print(f"\nPostagens encontradas para '{termo}':")
            if resultado.empty:
                print("  — nenhuma postagem encontrada.")
            else:
                print(resultado.to_string(index=False))
            input("\nPressione Enter para continuar...")
        elif opcao == "3":
            return
        else:
            print("Opção inválida. Tente novamente.")
# Função para exibir a parte de explorar
def explorar():
    while True:
        print("                                ")
        print("                                ")
        print("                                ")
        print("--------------------------------")
        print("EXPLORAR")
        print("--------------------------------")
        print("                                ")
        print("                                ")
        print("                                ")
        print("Qual opção você deseja? ")
        print("1 - Acessar Canais mais acessados")
        print("2 - Acessar Postagens mais acessadas")
        print("3 - Pesquisar por Postagens ou canais")
        print("4 - Acessar canal especifico")
        print("5 - Acessar postagem especifica")
        print("6 - Voltar")
              
        try:
            opcao = int(input("Digite a opção: "))
            if opcao == 1 :
                acessarCanais()
            elif opcao == 2:
                acessarPostagens()
            elif opcao == 3:
                pesquisar()
            elif opcao == 4:
                acessar_canal_especifico()
            elif opcao == 5:
                acessar_postagem_especifica()
            elif opcao == 6:
                menuInicial()
                break
            else:
                raise ValueError("Digite um valor válido!")
        except ValueError:
            print("Digite um valor válido!") 

# Faço um loop infinito para que o menu inicial seja exibido continuamente até que o usuario escolha a opção 5 (encerrar sistema)
while True:    
    menuInicial()
    try:
        opcao = int(input("Digite a opção desejada: "))
    except ValueError:
        print(" ")
        print("--------------------------------")
        print("Opção inválida")
        print("--------------------------------")
        print(" ")
        continue
    
    # Função para alternar o tema do site, aonde pega o novo tema inserido na chamada da função e altera a variavel tema    
    
    if opcao == 1:
        alternar_tema()
    elif opcao == 2:
        if usuario is None:
            cadastrar_conta()
        else:
            perfil()
    elif opcao == 3:
        if usuario is None:
            login_conta()
        else:
            logout_conta()
    elif opcao == 4:
         explorar()    
        
    elif opcao == 5:
        print("Encerrando sistema...")
        break
    else:
        print("Opção inválida")

