from shop import Weapon, Armor, Shop


# Оружие для Воина
iron_sword = Weapon(name="Железный Меч", damage=15, price=30)
steel_sword = Weapon(name="Стальной Меч", damage=17, price=33)
knight_blade = Weapon(name="Клинок Рыцаря", damage=19, price=36)
berserker_blade = Weapon(name="Клинок Берсерка", damage=21, price=40)
dragon_slayer = Weapon(name="Драконий Убийца", damage=23, price=44)
warrior_sword = Weapon(name="Меч Воина", damage=25, price=48)
dark_blade = Weapon(name="Темный Клинок", damage=27, price=53)
demon_edge = Weapon(name="Клинок Демона", damage=30, price=58)
blood_fang = Weapon(name="Кровавый Клык", damage=33, price=63)
soul_reaver = Weapon(name="Похититель Душ", damage=36, price=69)
firebrand = Weapon(name="Огненный Меч", damage=39, price=76)
shadow_edge = Weapon(name="Клинок Тени", damage=42, price=83)
wrath_scythe = Weapon(name="Коса Ярости", damage=46, price=91)
hell_blade = Weapon(name="Клинок Ада", damage=50, price=100)
doom_sword = Weapon(name="Меч Судьбы", damage=55, price=110)
abyssal_blade = Weapon(name="Клинок Бездны", damage=60, price=121)
titan_sword = Weapon(name="Меч Титана", damage=66, price=133)
godslayer = Weapon(name="Убийца Богов", damage=72, price=146)
eternal_edge = Weapon(name="Вечный Клинок", damage=79, price=161)
ragnarok = Weapon(name="Рагнарёк", damage=87, price=177)

# Оружие для Стрелка
hunter_bow = Weapon(name="Охотничий Лук", damage=15, price=30)
longbow = Weapon(name="Длинный Лук", damage=17, price=33)
composite_bow = Weapon(name="Композитный Лук", damage=19, price=36)
elven_bow = Weapon(name="Эльфийский Лук", damage=21, price=40)
eagle_bow = Weapon(name="Лук Орла", damage=23, price=44)
shadow_bow = Weapon(name="Лук Тени", damage=25, price=48)
dragon_bow = Weapon(name="Драконий Лук", damage=27, price=53)
dark_bow = Weapon(name="Темный Лук", damage=30, price=58)
soul_bow = Weapon(name="Лук Души", damage=33, price=63)
fire_bow = Weapon(name="Огненный Лук", damage=36, price=69)
death_shot = Weapon(name="Выстрел Смерти", damage=39, price=76)
sniper_bow = Weapon(name="Снайперский Лук", damage=42, price=83)
chaos_bow = Weapon(name="Лук Хаоса", damage=46, price=91)
phoenix_bow = Weapon(name="Лук Феникса", damage=50, price=100)
wrath_bow = Weapon(name="Лук Ярости", damage=55, price=110)
inferno_bow = Weapon(name="Лук Инферно", damage=60, price=121)
thunder_bow = Weapon(name="Громовой Лук", damage=66, price=133)
divine_bow = Weapon(name="Божественный Лук", damage=72, price=146)
eternity_bow = Weapon(name="Лук Вечности", damage=79, price=161)
stardust_bow = Weapon(name="Лук Звездной Пыли", damage=87, price=177)

# Оружие для Мага
magic_staff = Weapon(name="Магический Посох", damage=15, price=30)
crystal_staff = Weapon(name="Кристальный Посох", damage=17, price=33)
arcane_staff = Weapon(name="Арканный Посох", damage=19, price=36)
elemental_staff = Weapon(name="Посох Стихий", damage=21, price=40)
flame_staff = Weapon(name="Посох Пламени", damage=23, price=44)
lightning_staff = Weapon(name="Грозовой Посох", damage=25, price=48)
frost_staff = Weapon(name="Ледяной Посох", damage=27, price=53)
void_staff = Weapon(name="Посох Пустоты", damage=30, price=58)
necromancer_staff = Weapon(name="Посох Некроманта", damage=33, price=63)
firestorm_staff = Weapon(name="Посох Огненного Шторма", damage=36, price=69)
soul_staff = Weapon(name="Посох Души", damage=39, price=76)
shadow_staff = Weapon(name="Посох Тени", damage=42, price=83)
chaos_staff = Weapon(name="Посох Хаоса", damage=46, price=91)
demon_staff = Weapon(name="Демонический Посох", damage=50, price=100)
heaven_staff = Weapon(name="Посох Небес", damage=55, price=110)
eternal_staff = Weapon(name="Вечный Посох", damage=60, price=121)
astral_staff = Weapon(name="Астральный Посох", damage=66, price=133)
stardust_staff = Weapon(name="Посох Звездной Пыли", damage=72, price=146)
cosmic_staff = Weapon(name="Космический Посох", damage=79, price=161)
apocalypse_staff = Weapon(name="Посох Апокалипсиса", damage=87, price=177)

# Броня для всех классов
old_shirt = Armor(name="Старая Рубашка", armor=3, extra_hp=5, price=30)
leather_vest = Armor(name="Кожаный Жилет", armor=4, extra_hp=6, price=33)
iron_armor = Armor(name="Железная Броня", armor=5, extra_hp=7, price=36)
knight_armor = Armor(name="Рыцарские Латы", armor=6, extra_hp=8, price=40)
reinforced_armor = Armor(name="Укрепленная Броня", armor=7, extra_hp=9, price=44)
dragon_scale = Armor(name="Драконья Чешуя", armor=8, extra_hp=10, price=48)
shadow_armor = Armor(name="Броня Тени", armor=9, extra_hp=11, price=53)
holy_armor = Armor(name="Священная Броня", armor=10, extra_hp=12, price=58)
blood_mail = Armor(name="Кровавый Доспех", armor=11, extra_hp=13, price=63)
fire_plate = Armor(name="Огненный Доспех", armor=12, extra_hp=14, price=69)
dark_plate = Armor(name="Темная Латная Броня", armor=13, extra_hp=15, price=76)
soul_armor = Armor(name="Броня Души", armor=14, extra_hp=16, price=83)
storm_armor = Armor(name="Броня Шторма", armor=15, extra_hp=17, price=91)
eternal_plate = Armor(name="Вечная Латная Броня", armor=16, extra_hp=18, price=100)
ragnarok_armor = Armor(name="Броня Рагнарёка", armor=18, extra_hp=20, price=110)
warrior_plate = Armor(name="Доспех Воина", armor=20, extra_hp=22, price=121)
divine_armor = Armor(name="Божественная Броня", armor=22, extra_hp=24, price=133)
titan_mail = Armor(name="Доспех Титана", armor=24, extra_hp=26, price=146)
apocalypse_armor = Armor(name="Броня Апокалипсиса", armor=26, extra_hp=28, price=161)
god_plate = Armor(name="Доспех Богов", armor=29, extra_hp=30, price=177)


# Магазины
shop1 = Shop(
    items=[
        iron_sword,
        steel_sword,
        hunter_bow,
        longbow,
        magic_staff,
        crystal_staff,
        old_shirt,
        leather_vest,
    ]
)

shop2 = Shop(
    items=[
        steel_sword,
        knight_blade,
        longbow,
        composite_bow,
        crystal_staff,
        arcane_staff,
        leather_vest,
        iron_armor,
    ]
)
