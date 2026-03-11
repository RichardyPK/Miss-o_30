# Definir a situação do aluno
def resultado(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5 and media < 7:
        return "Recuperação"
    else:
        return "Reprovado"


# Calcular média das três notas
def calcular_media(notas):
    return (notas[0] + notas[1] + notas[2]) / 3


# Ler as 3 notas do aluno
def ler_notas():
    notas = []
    contador = 0

    while contador < 3:
        nota = float(input("Digite uma nota entre 0 e 10: "))

        if nota < 0 or nota > 10:
            print("Nota inválida. Digite novamente.")
            continue

        notas.append(nota)
        contador = contador + 1

    return notas


# Cadastrar um aluno
def cadastrar_aluno():
    print("Cadastro do aluno")
    nome = input("Digite o nome do aluno: ")

    notas = ler_notas()
    media = calcular_media(notas)
    situacao = resultado(media)

    return [nome, notas[0], notas[1], notas[2], media, situacao]


# Mostrar todos os alunos
def mostrar_alunos(alunos):
    print("Quantidade total de alunos cadastrados:", len(alunos))

    contador = 0
    while contador < len(alunos):
        aluno = alunos[contador]

        print("Nome:", aluno[0],
              "Nota1:", aluno[1],
              "Nota2:", aluno[2],
              "Nota3:", aluno[3],
              "Média:", aluno[4],
              "Situação:", aluno[5])

        contador = contador + 1


# Função principal (apenas controle do programa)
def main():
    alunos = []
    quantidade = int(input("Digite a quantidade de alunos (mínimo 10): "))
    if quantidade < 10:
        print("Número de alunos menor que 10. Execute o programa novamente.")
        return
    contador = 0
    while contador < quantidade:
        alunos.append(cadastrar_aluno())
        contador = contador + 1
    mostrar_alunos(alunos)


# Executar programa
main()