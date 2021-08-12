def escolher_listaPortas():
    portas_top10 = [21, 22, 23, 25, 80, 110, 139, 443, 445, 3389]
    portas_top20 = [135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080]
    portas_top50 = [3389, 5060, 5666, 5900, 6001, 8000, 8080, 8443, 8888, 10000, 32768, 49152, 49154]

    print("\n\033[4;36;36mSelecione uma Lista de Portas:\033[m")
    print("\033[1;31;31m1 -->\033[m \033[4;36;36mLista top 10\033[m")
    print("\033[1;31;31m2 -->\033[m \033[4;36;36mLista top 20\033[m")
    print("\033[1;31;31m3 -->\033[m \033[4;36;36mLista top 50\033[m")

    escolha = input("\n\033[1;31;31m>>>\033[m ")

    lista_escolhida = []

    if (escolha == '1'):
        lista_escolhida = portas_top10
        return lista_escolhida
    elif (escolha == '2'):
        lista_escolhida = portas_top20
        return lista_escolhida
    else:
        lista_escolhida = portas_top50
        return lista_escolhida
