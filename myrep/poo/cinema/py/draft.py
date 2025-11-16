class Client:
    def __init__(self, id: str, phone: int):
        self.__id = id
        self.__phone = phone

    def getPhone(self):
        return self.__phone
    def setPhone(self, value: int):
        self.__phone = value
    def getId(self):
        return self.__id
    def setId(self, value: str):
        self.__id = value

    def __str__(self):
        return f"{self.__id}:{self.__phone}"
    
class Theater:
    def __init__(self):
        self.seats: list[Client | None] = []
        self.search: str

    def init(self, capacity: int = 0):
        self.seats = [None] * capacity

    def verifyIndex(self, index: int) -> bool:
        if index < 0 or index > len(self.seats):
            return False
        return True

    def reserve(self, index: int, cliente: Client):
        if self.verifyIndex(index) is False:
            print("fail: cadeira nao existe")
            return
        for client in self.seats:
            if client is not None and client.getId() == cliente.getId():
                print("fail: cliente ja esta no cinema")
                return
        if self.seats[index] is not None:
            print("fail: cadeira ja esta ocupada")
            return
        self.seats[index] = cliente
        
    def cancel(self, id: str):
        for i, client in enumerate(self.seats):
            if client is not None and client.getId() == id:
                self.seats[i] = None
                return
        print(f"fail: cliente nao esta no cinema")
        return

    def __str__(self):
        seats = " ".join(["-" if x is None else str(x) for x in self.seats])
        return f"[{seats}]"
    
def main():
    cinema = Theater()
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        if args[0] == "show":
            print(cinema)
        if args[0] == "init":
            capacity = int(args[1])
            cinema.init(capacity)
        if args[0] == "reserve":
            id = args[1]
            phone = int(args[2])
            index = int(args[3])
            client = Client(id, phone)
            cinema.reserve(index, client)
        if args[0] == "cancel":
            id = args[1]
            cinema.cancel(id)
            

main()