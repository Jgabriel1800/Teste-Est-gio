"""2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 
2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e 
retorne uma mensagem avisando se o número informado pertence ou não a sequência."""

def fibonacci(n):
    x, y = 0, 1
    while y < n:
        x, y = y, x + y
    return y == n

n = int(input("Digite um número: "))
if fibonacci(n):
    print("O número  pertence a sequência de Fibonacci.")
else:
    print("O número  não pertence a sequência de Fibonacci ")