if __name__ == '__main__':

    numero_magico = 115

    print("Você tem 3 chances para acertar o número!")
    for i in range(3):
        print(f'Tentativa {i +1}')
        numero_informado = int(input("Informe o numero: "))
        if numero_magico < numero_informado:
            print("Errou! Tente um número menor!!")
        elif numero_magico > numero_informado:
            print("Errou! Tente um número maior!")
        else:
            print("Você acertou!")
            break