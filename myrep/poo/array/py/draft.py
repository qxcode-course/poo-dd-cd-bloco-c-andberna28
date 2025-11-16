import random
class Foo:
    def __init__(self, numero: int):
        self.numero: int = numero

    def __str__(self):
        return f"Foo({self.numero})"

    # def __repr__(self): #! Mostrar o objeto de forma útil em depuração
    #     return str(self.numero)
    
arrayVazio: list[int] = []
arrayPreenchido: list[int] = [1, 2, 3, 4, 5]
arrayNomes: list[str] = ["Ronaldo", "Romario", "Claudio", "Luana", "Bella"]
arrayObjetos: list[Foo] = [Foo(1), Foo(2), Foo(3), Foo(4), Foo(5)]

arrayPreenchido.append(1) #! Adicionar ao final
arrayPreenchido.pop() #! Remover do final
arrayPreenchido.insert(3, 0) #! Inidicar o indice para adicionar em qualquer posição do array
# arrayPreenchido.pop(0) #! Indicar o indice para remover qualquer elemento do array

# #* Criando array com elementos em sequencia de zero a N
# n = 10
# array = list(range(0, n + 1))
# print(f"Array de zero a N: {array}")

# #* Array com valores aleatorios
# array = [random.randint(0, 100) for _ in range(10)]
# print(array)

# print(f"Tamanho do Array: {len(arrayPreenchido)}") #! len() conta o tamanho do array
# print(", ".join(arrayNomes)) #! .join() para formatar o array
# print(", ".join(map(str, arrayPreenchido))) #! .join.(map(str, NomeDaVariavel)) para caso de array de int
# print(arrayPreenchido)
# print(arrayPreenchido[1]) #! Indicando o indice é possivel acessar apenas o elemento presente no indice indicado
# print(arrayVazio)

#* Percorrer elementos utilizando for-range
# array = [10, 20, 30, 40]

# for i in range(len(array)):
#     print(i, array[i])

#* Percorrer elementos utilizando for indexado
# lista = [10, 20, 30, 40]

# for i, valor in enumerate(lista):
#     print(i, valor)

#* Procurar um elemento X usando laço
# lista = [10, 20, 30]
# x = 20
# print(lista)
# for v in lista:
#     if v == x:
#         print(f"{x} Existe")
#         break
# else:
#     print(f"{x} não existe")

#* Procurar um elemento X usando função nativa
# lista = [10, 20, 30, 40]
# x = 80
# print(lista)
# if x in lista:
#     print(f"{x} Existe")
# else:
#     print(f"{x} não existe")

#* Criar um novo array com elementos filtrados
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# pares = [n for n in numeros if n % 2 == 0]

# print(pares)

#* Criar um novo array com elementos transformados
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# transformados = [n**2 for n in numeros]

# print(transformados)

#* Buscar e remover um elemento X
# lista = [10, 20, 30, 20]
# print(lista)
# x = 20
# lista.remove(x)
# print(lista)

#* Remover todos os elementos com valor X da lista
lista = [10, 20, 30, 20]
print(lista)
x = 20
lista = [item for item in lista if item != x]
print(lista)
