# Listas em Python
# Listas são estruturas de dados mutáveis, ou seja,seus elementos podem ser alterados após a criação.
# São definidas usando colchetes [] e podem conter elementos de diferentes tipos.
# São úteis quando você deseja armazenar uma coleção de itens que podem mudar ao longo do tempo


## •	Lista: coleção ordenada e mutável — frutas = [ "maça", "banana", "uva", "morango", "abacaxi", "laranja", "kiwi", "melancia"]
## •	Indexação: frutas[0] → "maçã" / frutas[-1] → "uva" (negativo conta do fim)
## •	Fatiamento: frutas[0:2] → ["maçã", "banana"] / frutas[::2] → de 2 em 2
## •	Métodos essenciais: append(x), pop(), pop(i), insert(i,x), sort(), reverse(), len(), count(x), index(x)


## Complete cada exercício antes de avançar para o próximo:
## 1.	Crie uma lista com 5 linguagens de programação que você conhece
linguagens = ["Python", "JavaScript", "Java", "C#", "Ruby"]

## 2.	Adicione "Scala" com append() e "Go" com insert(0, "Go") no início
linguagens.append("Scala")
linguagens.insert(0, "Go")

## 3.	Remova a última com pop() e imprima o que foi removido
ultima_linguagem = linguagens.pop()
print(f"A ultima linguagem removida foi: {ultima_linguagem}")

## 4.	Ordene a lista em ordem alfabética com sort() e imprima
linguagens.sort()
print(f"Lista ordenada: {linguagens}")

## 5.	Fatie para pegar só as 3 primeiras linguagens
primeiras_linguagens = linguagens[:3]
print(f"Primeiras linguagens: {primeiras_linguagens}")


# frutas = [ "maça", "banana", "uva", "morango", "abacaxi", "laranja", "kiwi", "melancia"]

# frutas.append("cereja")

# print(frutas)