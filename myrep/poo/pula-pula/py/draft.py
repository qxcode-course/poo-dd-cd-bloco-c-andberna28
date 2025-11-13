class Kid:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def get_name(self) -> str:
        return self.__name
    def get_age(self) -> int:
        return self.__age
    def set_name(self, value: str):
        self.__name = value
    def set_age(self, value: int):
        self.__age = value

    def __str__(self):
        return f"{self.__name}:{self.__age}"
    
class Trampoline:
    def __init__(self):
        self.playing: list[Kid] = []
        self.waiting: list[Kid] = []

    def arrive(self, kid: Kid):
        self.waiting.insert(0, kid)
    
    def enter(self):
        if len(self.waiting) > 0:
            kid = self.waiting.pop()
            self.playing.insert(0, kid)

    def leave(self):
        if len(self.playing) > 0:
            kid = self.playing.pop()
            self.waiting.insert(0, kid)

    def remove(self, name: str):
        if self.waiting != None:
            for i, kid in enumerate(self.waiting):
                if kid.get_name() == name:
                    del self.waiting[i]
                    return
        if self.playing != None:
            for i, kid in enumerate(self.playing):
                if kid.get_name() == name:
                    del self.playing[i]
                    return
        print(f"fail: {name} nao esta no pula-pula")
        return

    def __str__(self):
        playing_str = ", ".join("[]" if x == [] else str(x) for x in self.playing)
        waiting_str = ", ".join(["" if x == [] else str(x) for x in self.waiting])
        return f"[{waiting_str}] => [{playing_str}]"

def main():
    trampolim = Trampoline()
    while True:
        line: str = input()
        print("$" + line)
        args: list[str]  = line.split(" ")
        if args[0] == "end":
            break
        if args[0] == "show":
            print(trampolim)
        if args[0] == "arrive":
            nome = args[1]
            idade = args[2]
            kid = Kid(nome, idade)
            trampolim.arrive(kid)
        if args[0] == "enter":
            trampolim.enter()
        if args[0] == "leave":
            trampolim.leave()
        if args[0] == "remove":
            nome = args[1]
            trampolim.remove(nome)

main()