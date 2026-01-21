class Member:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.visits = 0

    def pay(self, amount):
        self.balance += amount

    def visit(self):
        if self.balance >= 20000:
            self.balance -= 20000
            self.visits += 1
            print("Mashg‘ulot bajarildi")
        else:
            print("Balans yetarli emas")

    def info(self):
        return f"{self.name} | Balans: {self.balance} | Kelgan: {self.visits}"


class Gym:
    def __init__(self):
        self.members = []

    def add_member(self, m):
        self.members.append(m)

    def report(self):
        for m in self.members:
            print(m.info())


gym = Gym()

while True:
    print("\n1. A’zo qo‘shish")
    print("2. To‘lov")
    print("3. Mashg‘ulot")
    print("4. Hisobot")
    print("0. Chiqish")

    c = input(">>> ")

    if c == "1":
        n = input("Ism: ")
        gym.add_member(Member(n))

    elif c == "2":
        n = input("Ism: ")
        for m in gym.members:
            if m.name == n:
                m.pay(int(input("Summa: ")))

    elif c == "3":
        n = input("Ism: ")
        for m in gym.members:
            if m.name == n:
                m.visit()

    elif c == "4":
        gym.report()

    elif c == "0":
        break
