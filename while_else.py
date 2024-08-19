numero = int(input("Digite um número maior que 1 e menor ou igual a 100: "))
if 1 < numero <= 100:
    divisor = 2
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            print(f"{numero} não é um número primo.")
            break
        divisor += 1
    else:
        print(f"{numero} é um número primo.")
else:
    print("Número fora do intervalo permitido.")