class Person:
    def __init__(self, nome: str):
        self.__nome = nome

    def getNome(self):
        return self.__nome
    def setNome(self, value: str):
        self.__nome = value

    def __str__(self):
        return f"nome: {self.__nome}"

class Market:
    def __init__(self):
        self.__counters: list[Person | None] = []
        self.__queue: list[Person] = []

    def init(self, qtd_counters: int = 0):
        for _ in range(qtd_counters):
            self.__counters.append(None)

    def arrive(self, person: Person):
        self.__queue.append(person)

    def call(self, index: int):
        if index < 0 or index >= len(self.__counters):
            print("fail: caixa nao existe")
            return
        if self.__counters[index] is not None:
            print("fail: caixa ocupado")
            return
        if len(self.__queue) == 0:
            print("fail: sem clientes")
            return
        self.__counters[index] = self.__queue[0]
        del self.__queue[0]

    def finish(self, index: int):
        if index < 0 or index >= len(self.__counters):
            print("fail: caixa inexistente")
            return
        if self.__counters[index] is None:
            print("fail: caixa vazio")
            return
        self.__counters[index] = None

    def give_up(self, name: str) -> Person | None:
        for i, person in enumerate(self.__queue):
            if person.name == name:
                aux = self.__queue[i]
                del self.__queue[i]
                return aux

    def __str__(self):
        counters = ", ".join(["-----" if x is None else str(x) for x in self.__counters])
        queue = ", ".join([str(x) for x in self.__queue])
        return f"Caixas: [{counters}]\nEspera: [{queue}]"

def main():
    budega = Market()
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(budega)
        elif args[0] == "init":
            budega.init(int(args[1]))
        elif args[0] == "arrive":
            person = args[1]
            budega.arrive(person)
        elif args[0] == "call":
            budega.call(int(args[1]))
        elif args[0] == "finish":
            budega.finish(int(args[1]))
        elif args[0] == "giveup":
            budega.give_up(args[1])

main()