## 1.	Crie uma tupla com (nome, idade, cidade) e faça desempacotamento em 3 variáveis
nome, idade, cidade = ("Derick", 30, "Rio de Janeiro")
print(f"Nome: {nome}, Idade: {idade}, Cidade: {cidade}")

## 2.	Tente modificar a tupla e leia o erro — entenda o que significa TypeError

cursos = ("Python", "JavaScript", "Java")
try:
    cursos[0] = "C#"
except TypeError as e:
    print(f"Erro ao tentar modificar a tupla: {e}")