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
            print(f"Вы купили {item.name}. Остаток: {hero.balance}")
            return item
        else:
            print("Недостаточно денег!")
            return None

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
        Item.id += 1

    def __str__(self):
        string = f"{self.name} (номер: {self.id}) | Урон: {self.damage} | Цена: {self.price}"
        return string


class Armor(Item):
    def __init__(self, name: str, armor: int, extra_hp: int, price: int):
        self.name = name
        self.armor = armor
        self.extra_hp = extra_hp
        self.price = price
        self.id = Item.id
        Item.id += 1

    def __str__(self):
        string = f"{self.name} (номер: {self.id}) | Доп. HP: {self.extra_hp} | Броня: {self.armor} | Цена: {self.price}"
        return string






