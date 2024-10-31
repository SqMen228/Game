import random

class Hero:
    def __init__(self, name, klass, level):
        self.name = name
        self.klass = klass
        if level == 'Easy':
            if klass == 'Воин':
                self.damage = 30
                self.hp = 150
                self.armor = 10
            if klass == 'Лучник':
                self.damage = 40
                self.hp = 120
                self.armor = 5
            if klass == 'Маг':
                self.damage = 50
                self.hp = 110
                self.armor = 2
        if level == 'Medium':
            if klass == 'Воин':
                self.damage = 25
                self.hp = 125
                self.armor = 70
            if klass == 'Лучник':
                self.damage = 32
                self.hp = 100
                self.armor = 3
            if klass == 'Маг':
                self.damage = 45
                self.hp = 90
                self.armor = 1
        if level == 'Hard':
            if klass == 'Воин':
                self.damage = 15
                self.hp = 100
                self.armor = 3
            if klass == 'Лучник':
                self.damage = 30
                self.hp = 85
                self.armor = 1
            if klass == 'Маг':
                self.damage = 40
                self.hp = 70
                self.armor = 0


    def __str__(self):
        return f"Имя: {self.name}\nHP: {self.hp}\nБроня: {self.armor}\nУрон: {self.damage}\nКласс: {self.klass}"

    def attack_monster(self, monster):
        krit = chance(30)
        if krit:
            self.damage += self.damage
        monster.hp = monster.hp - self.damage + monster.armor // 30
    def heal(self):
        k = 0
        if k >= 2:
            return print(f'Больше 2 раз нельзя')
        while 1:
            self.hp += self.hp // 30
            k+=1
            return self.hp






class Monster:
    def __init__(self, name, klass, level):
        self.name = name
        self.klass = klass
        if name == 'Червослиз':
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
        hero.hp = hero.hp - self.damage + hero.armor // 40

    def __str__(self):
        return f"Имя: {self.name}\nHP: {self.hp}\nБроня: {self.armor}\nУрон: {self.damage}\n"

#рандом
def chance(percentage):
    a = random.randint(0, 100)
    if percentage > a:
        return True
    return False

#выбор лвл
def input_level_difficulty():
    print('Выберите уровень сложности:\n')
    while 1:
        level_put= input('1) Если вы неуверенный в себе новичок выберите Easy\n2) Для обычного игрока подойдет Medium\n3) Для бывалых профи, любящих боль и страдания подойдет Hard\n')
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
            print('ошибочка, укажите цифру сложности которую хотите выбрать.\n')
#Klass
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

#Файт с монстром
def fight_monster(monster, hero):
    while 1:
        xod = input(f'{hero.name} Что ты выберешь\n1) Атаковать\n2) Лечение\n')
        if xod == '1':
            hero.attack_monster(monster)
            monster.attack_hero(hero)
            if monster.hp <= 0:
                print('YOU WIN')
                return None
            if hero.hp <= 0:
                print('YOU LOSE')
                return None
        elif xod == '2':
            hero.heal()
        else:
            print('Ошибка.Выбери еще раз.')


#Начало

print('\nДобро пожаловать в подземелье, вы были отправлены сюда для того чтобы выполнить очистку.\n')

level_difficulty = input_level_difficulty()
#создание перса
name_1 = input('Первый игрок, введите свое имя: ')
name_2 = input('Второй игрок, введите свое имя: ')
print(f'\n\n{name_1} и {name_2} посмотрим на что вы готовы ради выполнения мисси, за которую вам назначали не малое вознаграждения \n\n\n')

class_1 = input_choosing_class(name_1)
class_2 = input_choosing_class(name_2)


print('Вот ваша полная статистика:\n')
me_1 = Hero(name_1,class_1,level_difficulty)
me_2 = Hero(name_2,class_2,level_difficulty)


print(f'{me_1}\n---------------------------------------\n')
print(f'{me_2}\n---------------------------------------\n')
print('Ну господа, настало время спускаться в подземелье\n\n')


#Первый этаж

print('Мы спускаемся на 1 этаж подземелья, буд-те на чеку, ведь тут вас ждет местный обитатель,Червослиз.\nЭтот мерзкий и противный слизняк внешне похожий на червя, хоть и кажется опасным но на самом деле довольно слабый и беспомощный.\nОн не имеет защиты не от какого вида урона,просто тупой и вонючий кусок слизи.\n\n')

print('Начнем сражение\n\n')
print('!Сражение:\nСражаясь с монстрами на выбор у вас есть 3 действия:\n1) Вы можете атаковать монстра(урон от атак будет зависеть от вашего урона, брони монстра и его иммунитета.Также есть шанс выбить критическую атаку которая нанесет Х2 от вашего урона)\n2)Вы можете уклониться(уклонение позволяет вам либо уклониться, либо получить половину урона монстра)\n3) Вы можете вылечить себе 30% от вашего здоровья(не более 2 раз за сражение)\n')


name_monster_1 = 'Червослиз'
monster_1 = Monster(name_monster_1,class_1,level_difficulty)
print(f'{monster_1}----------------------------------------')

fight_monster(monster_1, me_1)

