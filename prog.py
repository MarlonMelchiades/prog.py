print("Olá, Mundo!")

soma = 6 + 23 + 56
# resultado = (87 – 9) * 4
media = 0
numero = 7
aluno1 = "Lucas da Silva"
resultadoDaSoma = soma + numero

s1 = "a soma de "
s2 = " + "
s3 = " é "

s = s1 + str(soma) + s2 + str(numero) + s3 + str(resultadoDaSoma)

num = input("Digite um número:")
print(soma)
# print(resultado)
print(( 9 - ( 1 + 2 ) ) / 3.0)
print(aluno1)
print(soma + numero)
print(s)
print("o número digitado foi: " + str(num))

nome = input("Digite o nome do aluno:")
nota1 = input("Digite a primeira nota de " + str(nome) + ":")
nota2 = input("Digite a segunda nota de " + str(nome) + ":")
media = (float(nota1) + float(nota2))/2

if media >= 7.0:
    print("Aluno aprovado. Parabéns! A média de " + str(nome) + " foi de " + str(media))
else:
    print("Aluno reprovado. Precisa estudar mais! A média de " + str(nome) + " foi de " + str(media))

alunos = ['João', 'Maria', 'Gabriel', 'Carolina']
print(alunos)
for element in alunos:
    print(element)

contador = 10
while contador >= 1:
    print(contador)
    contador = contador - 1
    if contador == 0:
        print("feliz ano novo!")
