import random
from shop import *


class Hero:
    def __init__(self, name, klass):
        self.name = name
        self.klass = klass
        self.balance = 0
        self.heal_count = 0

        if klass == 'Воин':
            self.max_hp = 125
            self.armor = 70
            self.weapon = Weapon("Палка", 20, 0)
        if klass == 'Лучник':
            self.max_hp = 100
            self.armor = 3
            self.weapon = Weapon("Деревянный лук", 34, 0)
        if klass == 'Маг':
            self.max_hp = 90
            self.armor = 1
            self.weapon = Weapon("Волшебный жезл", 45, 0)

        self.hp = self.max_hp


    def __str__(self):
        return f"Имя: {self.name}\nHP: {self.hp}\nБроня: {self.armor}\nУрон: {self.weapon.damage}\nКласс: {self.klass}\nБаланс: {self.balance}\nОружие: {self.weapon.name}"

    def attack_monster(self, monster):
        krit = chance(30)
        damage = self.weapon.damage
        if krit:
            damage += self.weapon.damage
        monster.hp = monster.hp - damage + monster.armor // 30

    def heal(self):
        if self.heal_count >= 2:
            print('Больше 2-ух раз нельзя')
        else:
            self.hp += int(self.hp * 0.3)
            self.heal_count += 1

    def earn_money(self, money):
        money = random.randint(int(money * 0.7), int(money * 1.5))
        self.balance += money
        print(f"{self.name} получил в награду {money}")

    def refresh_stats(self):
        self.hp = self.max_hp
        self.heal_count = 0


class Monster:
    def __init__(self, name, klass, level, prize):
        self.name = name
        self.klass = klass
        self.prize = prize

        if level == 'Easy':
            self.damage = 10
            self.hp = 100
            self.armor = 0
        if level == 'Medium':
            self.damage = 13
            self.hp = 100
            self.armor = 0
        if level == 'Hard':
            self.damage = 15
            self.hp = 100
            self.armor = 0

    def attack_hero(self, hero):
        hero.hp = hero.hp - self.damage + int(hero.armor * 0.4)
        print(f"{self.name} атаковал {hero.name}")

    def __str__(self):
        return f"Имя: {self.name}\nHP: {self.hp}\nБроня: {self.armor}\nУрон: {self.damage}\n"


# рандом
def chance(percentage):
    a = random.randint(0, 100)
    if percentage > a:
        return True
    return False


# выбор лвл
def input_level_difficulty():
    print('Выберите уровень сложности:\n')
    while 1:
        level_put = input('1) Если вы неуверенный в себе новичок выберите Easy\n2) Для обычного игрока подойдет Medium\n3) Для бывалых профи, любящих боль и страдания подойдет Hard\n')
        if level_put == '1':
            level = 'Easy'
            print(f'Ваша сложность Easy\nУдачной игры)\n\n\n')
            return level
        if level_put == '2':
            level = 'Medium'
            print(f'Ваша сложность Medium\nУдачной игры)\n\n\n')
            return level
        if level_put == '3':
            level = 'Hard'
            print(f'Ваша сложность Hard\nУдачной игры)\n\n\n')
            return level
        else:
            print('Ошибочка, укажите цифру сложности которую хотите выбрать.\n')


# Klass
def input_choosing_class(name):
    while 1:
        klass = input(f'{name} на выбор у тебя есть 3 класса:\n1) Воин\n2) Лучник\n3) Маг\n')
        if klass == '1':
            klass = 'Воин'
            print(f'{name} поздравляем вас, вы начнете игру за класс Война.\nПреймущество вашего класса заключается в большом количестве брони и здоровья.\nНе бойтесь подставить себя под удар помогая союзнику.\n\n')
            return klass
        if klass == '2':
            klass = 'Лучник'
            print(f'{name} неплохой выбор, вы начнете игру за класс Лучника.\nПреймущество вашего класса заключается в средних параметрах урона, хп и защиты\nМожете не бояться ударов врага но и не забывайте наносить дамаг.\n\n')
            return klass
        if klass == '3':
            klass = 'Маг'
            print(f'{name} любишь играть с огоньком? За класс Мага ты можешь позволить себе и не такое\nПреймущества мага заключается в огромном уроне.\nНе подставляйся под удары и вноси максимальный дамаг в врагов.\n\n')
            return klass
        else:
            print('Ошибка, попробуй еще раз\n\n')


# Файт с монстром
def fight_monster(monster, hero1, hero2):
    heroes = [hero1, hero2]

    while 1:
        for hero in heroes:
            xod = input(f'{hero.name} Что ты выберешь\n1) Атаковать\n2) Лечение\n')
            if xod == '1':
                hero.attack_monster(monster)
                if monster.hp <= 0:
                    print('YOU WIN')
                    return True
            elif xod == '2':
                hero.heal()
                print(hero.hp)
            else:
                print('Ошибка,выберите другую цифру.')
        hero_for_attack = random.choice(heroes)
        monster.attack_hero(hero_for_attack)
        print(hero_for_attack)
        if hero_for_attack.hp <= 0:
            print('YOU LOSE')
            return False


def hero_buy_item_in_shop(hero, shop):
    print(f"{hero.name}, ваш баланс: {hero.balance}")
    print(shop)

    while 1:
        hero_input = input(f"{hero.name}, выберите номер предмета, или '0' если хотите выйти из магазина")

        if hero_input == "0":
            return
        else:
            item_id = int(hero_input)
            item = shop[item_id]
            if item != None:
                item = shop.buy(hero, item)
                if item != None:
                    hero.weapon = item


# Начало
print('\nДобро пожаловать в подземелье, вы были отправлены сюда для того чтобы выполнить очистку.\n')
level_difficulty = input_level_difficulty()

# создание перса
name_1 = input('Первый игрок, введите свое имя: ')
name_2 = input('Второй игрок, введите свое имя: ')
print(f'\n\n{name_1} и {name_2} посмотрим на что вы готовы ради выполнения мисси, за которую вам назначали не малое вознаграждения \n\n\n')

class_1 = input_choosing_class(name_1)
class_2 = input_choosing_class(name_2)


print('Вот ваша полная статистика:\n')
me_1 = Hero(name_1,class_1)
me_2 = Hero(name_2,class_2)


print(f'{me_1}\n---------------------------------------\n')
print(f'{me_2}\n---------------------------------------\n')
print('Ну господа, настало время спускаться в подземелье\n\n')


# Первый этаж
print('Мы спускаемся на 1 этаж подземелья, буд-те на чеку, ведь тут вас ждет местный обитатель,Червослиз.\nЭтот мерзкий и противный слизняк внешне похожий на червя, хоть и кажется опасным но на самом деле довольно слабый и беспомощный.\nОн не имеет защиты не от какого вида урона,просто тупой и вонючий кусок слизи.\n\n')

print('Начнем сражение\n\n')
print('!Сражение:\nСражаясь с монстрами на выбор у вас есть 3 действия:\n1) Вы можете атаковать монстра(урон от атак будет зависеть от вашего урона, брони монстра и его иммунитета.Также есть шанс выбить критическую атаку которая нанесет Х2 от вашего урона)\n2)Вы можете уклониться(уклонение позволяет вам либо уклониться, либо получить половину урона монстра)\n3) Вы можете вылечить себе 30% от вашего здоровья(не более 2 раз за сражение)\n')


name_monster_1 = 'Червослиз'
monster_1 = Monster(name_monster_1,class_1,level_difficulty, 30)
print(f'{monster_1}----------------------------------------')

if fight_monster(monster_1, me_1, me_2) is True:
    me_1.refresh_stats()
    me_2.refresh_stats()

    me_1.earn_money(monster_1.prize)
    me_2.earn_money(monster_1.prize)
else:
    print("Начните заново")
    exit()

hero_buy_item_in_shop(me_1, shop1)
hero_buy_item_in_shop(me_2, shop1)

print(me_1)
print(me_2)
