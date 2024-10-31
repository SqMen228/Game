class Item:
    id = 1
    name: str
    price: int


class Hero:
    def __init__(self):
        self.balance = 100
        self.weapon = Weapon("Рука", 5, 0)

    def __str__(self):
        return f"Герой баланс: {self.balance}, оружие: {self.weapon.name}"


class Shop:
    def __init__(self, items: list[Item] | None = None):
        self.items = [] if items is None else items.copy()

    def add_item(self, item: Item):
        self.items.append(item)

    def buy(self, hero: Hero, item: Item):
        if hero.balance - item.price > 0:
            hero.balance -= item.price
            self.items.remove(item)
            print(f"Вы купили {item.name}. Остаток: {hero.balance}")
        else:
            print("Недостаточно денег")

    def __getitem__(self, n: int):
        for item in self.items:
            if item.id == n:
                return item
        print("Нет предмета с этим ID")

    def __str__(self):
        string = "---------------------------------------------\n"
        string += "Предметы в магазине:\n"
        for item in self.items:
            string += str(item) + "\n"
        string += "---------------------------------------------"
        return string


class Weapon(Item):
    def __init__(self, name: str, damage: int, price: int):
        self.name = name
        self.damage = damage
        self.price = price
        self.id = Weapon.id
        Weapon.id += 1

    def __str__(self):
        string = f"{self.name} (номер: {self.id})\nУрон: {self.damage}\nЦена: {self.price}"
        return string


knife = Weapon("Нож", 10, 10)
sword = Weapon("Меч", 15, 30)

shop = Shop([knife, sword])



hero = Hero()

print(hero)
print(shop)
shop.buy(hero, knife)
print(hero)
print(shop)

