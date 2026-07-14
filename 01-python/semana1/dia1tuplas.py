# Tuplas em Python são estruturas de dados imutáveis, ou seja, 
# uma vez criadas, seus elementos não podem ser alterados. 
# Elas são definidas usando parênteses () e podem conter elementos de diferentes tipos.
# São úteis quando você deseja garantir que os dados permaneçam constantes ao longo do tempo.

## •	Tupla: coleção ordenada e IMUTÁVEL — ponto = (10, 20). Tente modificar e veja o TypeError
## •	Quando usar tupla: coordenadas, configurações fixas, retorno múltiplo de funções, chaves de dicionário
## •	Desempacotamento: x, y = (10, 20) — funciona em listas e tuplas



## 1.	Crie uma tupla com (nome, idade, cidade) e faça desempacotamento em 3 variáveis
nome, idade, cidade = ("Derick", 30, "Rio de Janeiro")
print(f"Nome: {nome}, Idade: {idade}, Cidade: {cidade}")

## 2.	Tente modificar a tupla e leia o erro — entenda o que significa TypeError

cursos = ("Python", "JavaScript", "Java")
try:
    cursos[0] = "C#"
except TypeError as e:
    print(f"Erro ao tentar modificar a tupla: {e}")