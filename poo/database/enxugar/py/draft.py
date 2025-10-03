class Towel:
    def __init__(self, color: str, size:str):
        self.color: str = color
        self.size: str = size
        self.wetness: int = 0

    def dry(self, amount: int):
        self.wetness += amount
        if self.wetness >= self.getMaxWetness():
            print("toalha encharcada")
            self.wetness = self.getMaxWetness()
    
    def isDry(self): 
        return self.wetness == 0

    def WringOut(self):
        self.wetness = 0

    def getMaxWetness(self):
        if self.size == "P":
            return 10
        elif self.size == "M":
            return 20
        elif self.size == "G":
            return 30

    def __str__(self):
        return f"Cor: {self.color}, Tamanho: {self.size}, Umidade: {self.wetness}"

def main():
    toalha = Towel("", "")
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "criar":
            color = args[1]
            size = args[2]
            toalha = Towel(color, size)
        elif args[0] == "mostrar":
            print (toalha)
        elif args[0] == "enxugar":
            amount = (int(args[1]))
            toalha.dry(amount)
        elif args[0] == "seca":
            print("sim" if toalha.isDry() else "nao")
        elif args[0] == "torcer":
            toalha.WringOut()
        else:
            print("fail: comando desconhecido")
main()