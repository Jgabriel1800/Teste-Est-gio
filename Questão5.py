"""5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;"""

frase = "Hello World!"
frase_invertida = ""
for i in range(len(frase)-1, -1, -1):
    frase_invertida += frase[i]
print(frase_invertida)