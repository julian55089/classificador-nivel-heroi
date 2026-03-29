while True:
    nome = input("Digite o nome do herói: ")
    xp = int(input("Digite a quantidade de XP do herói: "))

    #Validação
    if xp < 0:
        print("XP inválido. Por favor, insira um valor não negativo.")
        continue

    #Classificação do herói    
    if  xp < 1000:
        nivel = "Ferro"
    elif xp <= 2000:
        nivel = "Bronze"
    elif xp <= 5000:
        nivel = "Prata"
    elif xp <= 7000:
        nivel = "Ouro"
    elif xp <= 8000:
        nivel = "Platina"
    elif xp <= 9000:
        nivel = "Ascendente"
    elif xp <= 10000:
        nivel = "Imortal"
    else:
        nivel = "Radiante"

    print(f"\nO Herói de nome {nome} está no nível de {nivel}")

    continuar = input("\nDeseja classificar outro herói? (s/n): ").lower()
    if continuar != "s":
        break
