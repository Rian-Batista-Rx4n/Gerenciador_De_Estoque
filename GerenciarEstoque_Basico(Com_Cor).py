from time import sleep as s


def hud(titulo):
    print("\033[0;34m=\033[m" * 50)
    print(f"{titulo:^50}")
    print("\033[0;34m=\033[m" * 50)


def arq(nome):
    try:
        a = open(nome, "rt")
        a.close()
    except:
        print("Pelo jeito é sua primeira vez utilizando esse aplicativo...")
        s(4)
        print("Aqui você pode \033[0;32mcadastrar\033[m \033[4;33mprodutos\033[m e sua \033[4;33mquantia\033[m.")
        s(3)
        print("Vou criar um arquivo na raiz do seu \033[0;31mCELULAR\033[m ou \033[0;31mPC\033[m chamado \033[0;33m'coisas.csv'\033[m...")
        s(4)
        a = open(nome, "wt+")
        a.close()
        print("Arquivo criado com \033[1;30;42mSucesso!\033[m")
        s(2)
        print("Essas mensagens não irão re-aparecer mais!")
        s(3)
        print("\033[4;32mAproveite!\033[m")
        s(5)
        print("\n"*100)


def menu():
    print('''
\033[0;33m[1]\033[m Ver itens cadastrados
\033[0;33m[2]\033[m Cadastrar itens

\033[0;33m[9]\033[m Exit''')
    while True:
        try:
            opc = int(input('>> '))
        except:
            print("\033[0;31mValor Invalido!\033[m")
        else:
            return opc


def cadastrar(arquivo):
    try:
        a = open(arquivo, "at")
    except:
        print("\033[0;31mErro ao abrir arquivo\033[m")
    else:
        print("-"*50)
        while True:
            nome = str(input("Nome do produto: ")).title().strip()
            while True:
                try:
                    quantia = int(input("Quantia: "))
                except:
                    print("\033[0;31mValor Invalido!\033[m")
                else:
                    quantia = quantia
                    break
            a.write(f'{nome};{quantia}\n')
            opc = str(input("Continuar [S/N]? ")).upper().strip()
            if opc == "N":
                print("\n"*100)
                break


def ler(nome):
    print("-"*50)
    linhas = 0
    try:
        a = open(nome, 'rt')
        a.close()
    except:
        print("\033[0;31mErro ao ler o arquivo\033[m")
    else:
        a = open(nome, 'rt')
        for l in a:
            linhas += 1
            dado = l.split(';')
            dado[1] = dado[1].replace("\n", "")
            print(f"Nome: {dado[0]:<35} Quantia:{dado[1]}")
        a.close()
    finally:
        s(1)
        print("\n")
        print(f"Total de Linhas: {linhas}")
        s(1)
        input("Aperte \033[0;32mENTER\033[m para proseguir...")
        print("\n"*100)


arq("coisas.csv")
while True:
    hud("Cadastror 2.0")
    escolha = menu()
    if escolha == 1:
        ler("coisas.csv")
    elif escolha == 2:
        cadastrar("coisas.csv")
    else:
        break
print("\n"*100)
print("\033[0;30;42mObrigado por Utilizar meu sistema! \033[1;31;42mby=RX4N\033[m")
s(5)
