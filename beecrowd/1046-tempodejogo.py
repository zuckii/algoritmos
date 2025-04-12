hora_inicial, hora_final = map(int, input().split())

if hora_final > hora_inicial:
    duracao = hora_final - hora_inicial

else:
    duracao = (24 - hora_inicial) + hora_final

print(f"O JOGO DUROU {duracao} HORA(S)")
