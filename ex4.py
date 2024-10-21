
nota = float(input("Digite a nota do aluno (de 0 a 10): "))

if nota >= 7:
    print("Aprovado")
elif nota <= 4:
    print("Reprovado")
elif 4 < nota < 7:
    print("Recuperação")
else:
    print("Nota inválida. A nota deve estar entre 0 e 10.")
