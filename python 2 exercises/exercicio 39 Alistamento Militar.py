question = int(input("Digite o ano de nascimento: "))
if question == 2008:
    print("Você deve se alistar esse ano.")
elif question < 2008:
    years_ago = 2008 - question
    print(f"Você já passou do tempo de alistamento! "
          f"Seu alistamento foi há {years_ago} anos.")
elif question > 2008:
    print("Você ainda não precisa se alistar.")