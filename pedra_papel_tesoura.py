import random

pontos_user = 0
pontos_maquina = 0

opcoes = ["r", "t", "p"]

print("\n\n\tBEM VINDO(A) AO JOGO PEDRA PAPEL E TESOURA!")

while True: 
    escolha_user = input("\n\tEscolha: \n\t\t'R' - pedra\n\t\t'T' - tesoura\n\t\t'P' - papel\n\t\t'Q' - sair do programa\n\t\t> ").lower()

    if escolha_user == 'q':
        break

    if escolha_user not in opcoes:
        continue

    escolha_maquina = random.randint(0, 2)
    # 0 : R, 1 : T, 2 : P

    opcao_maquina = opcoes[escolha_maquina]

    print("\n\tA maquina escolheu: " + opcao_maquina)

    if escolha_user == opcao_maquina:
        print("\t- Empate!")

    elif escolha_user == "r" and opcao_maquina == "t":
        print("\t- Você ganhou!")

        pontos_user = pontos_user + 1
    elif escolha_user == "p" and opcao_maquina == "r":
        print("\t- Você ganhou!")

        pontos_user = pontos_user + 1
    elif escolha_user == "t" and opcao_maquina == "p":
        print("\t- Você ganhou!")
        pontos_user = pontos_user + 1
    
    else:
        print("\t- Você perdeu!")
        pontos_maquina = pontos_maquina + 1


print("\n\n--------------------------")
print("PLACAR FINAL")
print("--------------------------")
print("- Sua pontuação: " + str(pontos_user))
print("- Pontuação da maquina: " + str(pontos_maquina))
print("--------------------------")

if pontos_maquina > pontos_user:
    print("\tDerrota!")
elif pontos_maquina == pontos_user:
    print("\tEmpate.")
else:
    print("\tVitoria!")

    

print("\n\nFim de programa")

