print("Bem vindo à calculadora de média IBMR Laureate!")

# N1 se trata do trabalho
N1 = float(input("Quanto você tirou na N1?\n"))

# N2 se trata da prova
N2 = float(input("Quanto você tirou na N2?\n"))

# Nf se trata da nota final
Nf = (N1*0.4) + (N2*0.6)

#Uma maneira de exibir a resposta da conta:
Nota = "Sua nota foi: {}".format(Nf)
#Uma maneira mais facil:
Nota2 = f"Sua nota foi: {Nf}"

if Nf > 6.0:
    print(Nota2)
    print("Você foi aprovado! :)")

elif Nf < 6.0:
    print(Nota2)
    print("Você foi reprovado :(")

print("FIM")
