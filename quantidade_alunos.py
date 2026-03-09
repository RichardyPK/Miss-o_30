def main():

    # Lista que irá guardar todos os alunos cadastrados
    alunos = []

    # Loop inicial do programa
    while True:

        # Solicitar a quantidade de alunos
        quantidade_alunos = int(input("Digite a quantidade de alunos (mínimo 10): "))

        # Verificar se a quantidade é menor que 10
        if quantidade_alunos < 10:
            print("Número de alunos menor que 10. Execute o programa novamente.")
            break

        # Contador para controlar o cadastro de alunos
        contador = 0

        # Loop para cadastrar cada aluno
        while contador < quantidade_alunos:

            print("Cadastro do aluno")

            # Solicitar o nome do aluno
            nome = input("Digite o nome do aluno: ")

            # Lista para guardar as notas do aluno
            notas = []

            # Contador das notas
            contador_notas = 0

            # Loop para receber as 3 notas
            while contador_notas < 3:

                # Solicitar uma nota
                nota = float(input("Digite uma nota entre 0 e 10: "))

                # Validar se a nota está entre 0 e 10
                if nota < 0 or nota > 10:
                    print("Nota inválida. Digite novamente.")
                    continue

                # Adicionar a nota na lista
                notas.append(nota)

                # Aumentar o contador de notas
                contador_notas = contador_notas + 1

            # Calcular a média das notas
            media = (notas[0] + notas[1] + notas[2]) / 3

            # Definir a situação do aluno
            if media >= 7:
                situacao = "Aprovado"
            elif media >= 5 and media < 7:
                situacao = "Recuperação"
            else:
                situacao = "Reprovado"

            # Adicionar os dados do aluno na lista de alunos
            alunos.append([nome, notas[0], notas[1], notas[2], media, situacao])

            # Aumentar o contador de alunos
            contador = contador + 1

        # Finaliza o loop principal após cadastrar os alunos
        break

    # Mostrar quantidade total de alunos cadastrados
    print("Quantidade total de alunos cadastrados:", len(alunos))

    # Contador para percorrer a lista de alunos
    contador = 0

    # Loop para mostrar os dados de cada aluno
    while contador < len(alunos):

        aluno = alunos[contador]

        # Exibir informações do aluno
        print("Nome:", aluno[0],
              "Nota1:", aluno[1],
              "Nota2:", aluno[2],
              "Nota3:", aluno[3],
              "Média:", aluno[4],
              "Situação:", aluno[5])

        # Passar para o próximo aluno
        contador = contador + 1


# Executar o programa
main()