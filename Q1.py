while True:
        x=0
        ant=0
        prox=1
        num = input("Digite um número:")
        while True:
            try:
                valor = float(num)
                if valor.is_integer() and valor>=0:
                    if(x<1):
                        x=1
                        print("Sequência de Fibonacci:")
                        print(f"{ant}\n{prox}")
                    resultado = ant+prox
                    ant = prox
                    prox = resultado
                    print(resultado)
                    if resultado == valor:
                        print(f"\n{int(valor)} Faz parte da sequência de Fibonacci\n")
                        break
                    elif resultado > valor:
                        print(f"\n{int(valor)} Não faz parte da sequência de Fibonacci\n")
                        break
                else:
                    print("Digite um número inteiro maior ou igual a 0:")
                    break
            except ValueError:
                 print("Entrada de dados inválida")
                 break
