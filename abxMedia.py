n: int
soma: float; media: float

n = int(input("Informe a quantidade de elemento para o vetor ? "))

vetor: [float] = [0 for x in range(n)]

for i in range(n):
	vetor[i] = float(input("Digite um numero: "))

soma = 0

for i in range(n):
	soma = soma + vetor[i]


media = soma / n

print(f"\nMedia do vetor = {media:.3f}")
print("Elementos abaixo da media:")

for i in range(n):
	if vetor[i] < media:
		print(f"{vetor[i]:.1f}")