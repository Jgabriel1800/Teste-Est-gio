"""4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
• SP – R$67.836,43
• RJ – R$36.678,66
• MG – R$29.229,88
• ES – R$27.165,48
• Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que 
cada estado teve dentro do valor total mensal da distribuidora."""

total= 67836.43 + 36678.66 + 29229.88 + 27165.48 + 19849.53
SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
Outros = 19849.53

percentual_SP = (SP/total)*100
percentual_RJ = (RJ/total)*100
percentual_MG = (MG/total)*100
percentual_ES = (ES/total)*100
percentual_Outros = (Outros/total)*100

print("O percentual de representação de SP é de:",percentual_SP,"%")
print("O percentual de representação de RJ é de:",percentual_RJ,"%")
print("O percentual de representação de MG é de:",percentual_MG,"%")
print("O percentual de representação de ES é de:",percentual_ES,"%")
print("O percentual de representação de Outros é de:",percentual_Outros,"%")

