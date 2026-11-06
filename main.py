pontos = 0
tentativas = 3

while tentativas > 0:
    resposta = input('Quanto é 30 + 37?')

    if resposta == '67':
        print('Resposta correta!')
        pontos += 1
        break
    else:
        print(f'Errado, tente novamente! Tentativas restantes: {tentativas}')
        tentativas -= 1

print(f'Voce marcou {pontos} pontos!')