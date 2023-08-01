
def imprimirDados(nome, anoNascimento):
    idade = 2023 - anoNascimento
    print("Seu nome é " , nome , " e você tem " , idade , " anos")

def info():
    while True:
        try:
            nome = input("Insira seu nome completo:")
            anoNascimento = int(input("Seu ano de nascimento:"))

            if anoNascimento >= 1922 and anoNascimento <= 2023:
                imprimirDados(nome, anoNascimento)
                break
            else:
                print("Ano inválido!")
        except:
            print("Dados instáveis, tente novamente.")

info()