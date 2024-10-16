# importando o módulo
from calculos import potencia, raiz_quadrada

# programa principal
if __name__ == "__main__":
    while True:
        print("\nEscolha uma opção:")
        print("0 - Sair do programa")
        print("1 - Calcular Potência")
        print("2 - Calcular Raiz Quadrada")

        opcao = int(input("Digite a opção desejada: "))

        if opcao == 0:
            print("Saindo do programa...")
            break
        elif opcao == 1:
            try:
                base = float(input("Informe a base: ").replace(",", "."))
                expoente = float(input("Informe o expoente: ").replace(",", "."))
                resultado = potencia(base, expoente)
                print(f"O resultado de {base} elevado a {expoente} é {resultado}.")
            except Exception as e:
                print(f"Erro ao calcular a potência: {e}")
        elif opcao == 2:
            try:
                numero = float(input("Informe o número: ").replace(",", "."))
                resultado = raiz_quadrada(numero)
                print(f"A raiz quadrada de {numero} é {resultado}.")
            except Exception as e:
                print(f"Erro ao calcular a raiz quadrada: {e}")
        else:
            print("Opção inválida. Tente novamente.")
