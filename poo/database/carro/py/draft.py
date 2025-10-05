class Carro:
    def __init__(self):
        self.passageiro = 0
        self.km = 0
        self.passMax = 2
        self.gas = 0
        self.gasMax = 100

    def __str__(self):
        return f"pass: {self.passageiro}, gas: {self.gas}, km: {self.km}"

    def enter(self):
        if self.passageiro < self.passMax:
            self.passageiro += 1
        else:
            print("fail: limite de pessoas atingido")

    def leave(self):
        if self.passageiro > 0:
            self.passageiro -= 1
        else:
            print("fail: nao ha ninguem no carro")

    def fuel(self, increment: int):
        if self.gas + increment <= self.gasMax:
            self.gas += increment
        else:
            self.gas = self.gasMax

    def drive(self, distance: int):
        if self.passageiro == 0:
            print("fail: nao ha ninguem no carro")
        elif self.gas == 0:
            print("fail: tanque vazio")
        elif distance > self.gas:
            print(f"fail: tanque vazio apos andar {self.gas} km")
            self.km += self.gas
            self.gas = 0
        else:
            self.km += distance
            self.gas -= distance

def main():
    carro = Carro()
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(carro)
        elif args[0] == "enter":
            carro.enter()
        elif args[0] == "leave":
            carro.leave()
        elif args[0] == "fuel":
            increment = int(args[1])
            carro.fuel(increment)
        elif args[0] == "drive":
            carro.drive(int(args[1]))
        else: 
            print ("fail: comando desconhecido")

main()