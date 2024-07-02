nVitorias = None
while (nVitorias == None):
	nVitorias = input("Quantidade de vitórias: ")
	try:
		nVitorias = int(nVitorias)
	except:
		nVitorias = None
		print("Entrada de quantidade de vitórias inválida!\nFavor inserir a quantidade de vitórias em numeros inteiros...\n")
nDerrotas = None
while (nDerrotas == None):
	nDerrotas = input("Quantidade de derrotas: ")
	try:
		nDerrotas = int(nDerrotas)
	except:
		nDerrotas = None
		print("Entrada de quantidade de derrotas inválida!\nFavor inserir a quantidade de derrotas em numeros inteiros...\n")

saldoVitorias = nVitorias - nDerrotas
def checkLevel(saldoVitorias):
        if (saldoVitorias<=10):
                return("Ferro")
        elif (saldoVitorias<=20):
                return("Bronze")
        elif (saldoVitorias<=50):
                return("Prata")
        elif (saldoVitorias<=80):
                return("Ouro")
        elif (saldoVitorias<=90):
                return("Diamante")
        elif (saldoVitorias<=100):
                return("Lendário")
        else :
                return("Imortal")

print("O Herói tem de saldo de ", saldoVitorias, " está no nível de ", checkLevel(saldoVitorias))
