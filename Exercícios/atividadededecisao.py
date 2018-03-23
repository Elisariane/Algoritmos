# #2 Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
# print('Exercício 1')
# valor= int (input ('Digite um valor: '))
# if valor > 0 :
#     print (valor,'é número positivo')
# else:
#     print(valor,'é um número negativo')
# print('Exercício 2')
# #1 Faça um Programa que peça dois números e imprima o maior deles.
# valor1= int (input ('Primeiro valor: ') )
# valor2= int (input ('Segundo valor: ') )
# if valor1 > valor2 :
#     print (valor1, 'é o maior número.')
# elif valor2 > valor1 :
#     print (valor2, 'é o maior número.')
# else:
#     print(valor1, 'e', valor2, 'são iguais')
# print('Exercício 3')
# #Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor que C.
# a= int (input ('Digite o valor de A: '))
# b= int (input ('Digite o valor de B: '))
# c= int (input ('Digite o valor de C: '))
# if (a+b)< c:
#     print(a+b, 'é menor que', c)
# elif (a+b)== c:
#     print(a+b,'é igual a', c)
# else:
#     print(a+b,'é maior que', c)
# print('Exercício 4')
# 3 Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
# sexo = input ('Qual seu sexo? ')
# if sexo ==  'F' or sexo== 'f' :
#         print ('Feminino')
# elif sexo == 'M' or sexo== 'm':
#     print ('Masculino')
# else:
#     print ('Sexo inválido')
#Faça um Programa que peça um número inteiro e determine se ele é par ou ímpar. Dica: utilize o operador módulo (resto da divisão).
# print('Exercício 5')
# n= int (input ('Digite um número inteiro:'))
# if n%2 == 0:
#     print (n,'é um número par.')
# else:
#     print(n,'é um número ímpar.')
# print('Exercício 6')
# # #Faça um algoritmo que leia um número e some 5 caso seja par ou some 8 caso seja ímpar. Por fim, imprima o resultado desta soma.
# n= int (input ('Digite um número: '))
# if n%2== 0:
#     s=n+5
#     print ('A soma é', s)
# elif n%2== 1:
#     s= n+8
#     print ('A soma é', s)
# print('Exercício 7')
# #Crie um programa que peça uma nota de trabalho e uma de prova (as duas de 0 a 100).
# # Se a média aritmética das notas for maior ou igual a 60, escreva “Aprovado”, se não, “Reprovado”.
# t= float (input ('Nota do tabalho: '))
# p= float (input ('Nota da prova: '))
# nf= (t+p)/2
# if nf== 60:
#     print ('Aprovado!')
# elif nf> 60:
#     print ('Aprovado!')
# else:
#     print ('Reprovado.')
# print('Exercício 8')
# #Construa um programa que recebe três valores, A, B e C. Em seguida, apresente na tela somente o maior deles.
# a= int (input ('Digite o valor de A: '))
# b= int (input ('Digite o valor de B: '))
# c= int (input ('Digite o valor de C: '))
# if a>b and a>c:
#     print(a, 'é maior')
# elif b>a and b>c:
#     print(b, 'é maior')
# else:
#     print(c, 'é maior')
# print('Exercício 9')
 #Construa um programa que recebe três valores, A, B e C. Em seguida, apresente na tela os números em ordem decrescente.
# a= int (input ('Digite o valor de A: '))
# b= int (input ('Digite o valor de B: '))
# c= int (input ('Digite o valor de C: '))
# if a>b and a>c and b>c:
#     print(a,b,c)
# elif a>b and a>c and c>b:
#     print(a,c,b)
# elif b>a and b>c and a>c:
#     print(b,a,c)
# elif b>a and b>c and c>a:
#     print(b,c,a)
# elif c>a and c>b and a>b:
#     print (c,a,b)
# else:
#     print (c,b,a)
# print('Exercício 10')
#Construa um programa que mostre menu exatamente como o exemplo abaixo e implemente as funções necessárias:
#     == Menu de Opções ==
#     1. Somar 2 números
#     2. Potência de um número
# 3. Raiz de grau N
# == Opção escolhida:
# print('== Menu de Opções ==')
# print('1. Somar 2 números')
# print('2. Potência de um número')
# print('3. Raiz de grau N')
# op= int (input('== Opção escolhida:'))
# if op==1:
#     n1= float (input('Digite o primeiro número :'))
#     n2= float (input('Digite o segundo número: '))
#     s= n1+n2
#     print ('A soma é',s)
# elif op==2:
#     n= int (input("Digite um número: "))
#     p= int (input("Digite a potência: "))
#     r=(n**p)
#     print('A potência de', n, 'é',r)
# elif op==3:
#     num= int (input ('Digite um número: '))
#     raiz= int (input('Digite um número para a raiz: '))
#     r= num**(1/raiz)
#     print ('O resultado é', r)
# else:
#     print ('Escolha entre 1, 2 e 3')
# print('Exercício 11')
# #Uma loja está com uma promoção de 10% desconto em todos os seus produtos.
# #Faça um programa que receba um valor, calcule e imprima o valor do desconto (em reais) e o valor final do produto após aplicar o desconto.
# preco= float (input('Indique o valor do produto: '))
# d10= (preco * (10/100))
# print('O valor do produto é',preco - d10)
print('Exercício 12')
#Faça um programa que calcule o valor de imposto a ser pago a partir de um salário bruto.
# Se o salário for maior que R$3.000,00 deverá ser cobrado 15% de imposto e se for menor, 7,5%.
#Por fim, apresente o salário bruto (total), o valor de imposto e o salário líquido (o bruto menos o imposto).
sal= float (input('Digite seu salário: '))
im15= sal*(15/100)
im7= sal * (7.5/100)
if sal>= 3000.00:
    print('Salário total=', sal)
    print('Valor do imposto=',im15)
    print('Salário líquido=', sal-im15)
else:
    print('Salário total=', sal)
    print('Valor do imposto=',im7)
    print('Salário líquido=', sal-im7)
