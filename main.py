import requests
import time


RED = "\033[1;31m"
BLUE = "\033[1;34m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"


def introducao():
    global linhas
    linhas = BLUE + "-" * 50 + RESET
    titulo = "Quer sair da rotina nessas férias com a namorada?\n \
       Então você está no lugar certo!".upper()

    print(linhas)
    print(titulo.center(50))
    print(linhas)

    time.sleep(1.5)

    print()
    print("Vou buscar os melhores lugares para vocês!".center(50))
    print("Mas antes me diga...".center(50))
    print()

    time.sleep(1.5)

    print(BLUE + "Vocês são PRAIANOS ou preferem mais DIVERSÃO?".center(50) + RESET)

    time.sleep(1.5)
    return


def praias():
    url = "https://61d37a63b4c10c001712b9a3.mockapi.io/praias"
    response = requests.get(url)
    praias = response.json()

    print()
    print(GREEN + "Vejo só esses lugares que encontrei para vocês!".upper() + RESET)
    print()

    for i in range(len(praias)):
        print(f'{i + 1}ª praia: {GREEN + praias[i]["name"] + RESET}')
        print(f'Localiza-se em {praias[i]["cidade"]}')
        print(linhas)
    return


introducao()
escolha = input('Digite "P" para praia ou "D" para mais diversão: ').lower()[0]
print()
print(linhas)

if escolha == "p":
    praias()
    print()
    ver_imagem = input("Gostaria de ver as fotos dessas praias? [SIM/NÃO]").lower()[0]
    print()

    if ver_imagem == "s":
        url = "https://61d37a63b4c10c001712b9a3.mockapi.io/praias"
        response = requests.get(url)
        praias = response.json()
        for i in range(5):
            print(f'Clique no link para ver a foto de {GREEN + praias[i]["name"]}:')
            print(praias[i]["avatar"])
            print(linhas)

    elif ver_imagem == "n":
        print("Okay")

    else:
        print(RED + "ERRO! A opção digitada não existe.".center(50))


elif escolha == "d":
    print(
        RED
        + """
    Ops...
    Infelizmente esta função não está liberada.
    o desenvolvedor ficou com preguiça e dormiu :/
    
    Mas não se preocupe, antes de o demitirmos 
    ele desenvolveu a parte praiana :)
    Para aproveitar, basta reiniciar o 
    programa e digitar "P" quando for pedido.
    """
        + RESET
    )


else:
    print(RED + "ERRO! A opção digitada não existe.".center(50))
