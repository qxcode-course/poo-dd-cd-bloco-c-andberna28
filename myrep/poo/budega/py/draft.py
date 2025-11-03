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
        self.__queue: list[Person]

    def __str__(self):
        return f"Caixas: {self.__counters} // Espera: {self.__queue}"

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

main()