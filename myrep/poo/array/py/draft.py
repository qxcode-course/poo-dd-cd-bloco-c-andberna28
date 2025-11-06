class Foo:
    def __init__(self, numero: int):
        self.numero: int = numero

    def __str__(self):
        return f"Foo({self.numero})"

    # def __repr__(self): #! Mostrar o objeto de forma útil em depuração
    #     return str(self.numero)
    
arrayVazio: list[int] = []
arrayPreenchido: list[int] = [1, 2, 3, 4, 5]
arrayObjetos: list[Foo] = [Foo(1), Foo(2), Foo(3), Foo(4), Foo(5)]

arrayPreenchido.append(1) #! Adicionar ao final
arrayPreenchido.pop() #! Remover do final
arrayPreenchido.insert(3, 0) #! Inidicar o indice para adicionar em qualquer posição do array
# arrayPreenchido.pop(0) #! Indicar o indice para remover qualquer elemento do array


tamanho = len(arrayPreenchido)
print(f"Tamanho do Array: {tamanho}")
print(arrayPreenchido)
print(arrayVazio)