import random

def attack_monstr():
    damage = 10
    monster_armor = 2
    monster_hp = 100
    monster_hp = monster_hp - damage + monster_armor // 30
    if monster_hp <= 0:
        print("WIN")
def fight_monster(name_hero, monster, me):
    while 1:
        xod = input(f'{name_hero}Что ты выберешь\n1) Атаковать\n2) Уклонение\n3) Лечение')
        if xod == '1':
            xod = me.attack_monstr(monster)
            return xod
        if xod == '2':
            xod = me.evasion(monster)
            return xod
        if xod == '3':
            xod = me.heal(me)
            return xod

name = 'Kirill'

a = fight_monster