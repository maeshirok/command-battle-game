'''
ドラクエのようなコマンド式のバトルを再現

# 1vs1
# 素早さにより先行後攻が可変
# 自身の攻撃力と敵の防御力によりダメージが可変
'''
import random
import questionary
from questionary import Choice

class Character:
    def __init__(self, name, hit_point, attack_point, defence_point, dexterity_point):
        self.name = name
        self.hit_point = hit_point
        self.defence_point = defence_point
        self.dexterrity_point = dexterity_point
        self.attack_point = attack_point

    def is_dead(self):
        return self.hit_point <= 0

    def attack(self, defender, enemy_defence_point):
        print()
        print(f'{self.name}の攻撃！')
        defender.defend(
            round((self.attack_point - enemy_defence_point / 2)/2) + random.randint(0, 3))

    def defend(self, damage):
        if damage <= 0:
            print(f'{self.name}は攻撃をかわした！')
            return
        self.hit_point -= damage
        print(f'{self.name}は{damage}のダメージを受けた！(残りHP:{self.hit_point})')
        if self.is_dead():
            print(f'{self.name}は力尽きた')


MONSTERS = [
    # (name, hp, atk, def, dex)
    Character('スライム', 5, 5, 3, 1),
    Character('スライムベス', 7, 7, 3, 1),
    Character('ゴースト', 9, 11, 8, 4),
    Character('りゅうおう', 130, 140, 200, 0),
]


def main():
    hero = Character('勇者', 26, 7, 5, 3)
    monster = random.choice(MONSTERS)
    print(f'{monster.name}が現れた！')

    if hero.dexterrity_point >= monster.dexterrity_point:
        attacker, defender = hero, monster
    else:
        attacker, defender = monster, hero
    while not attacker.is_dead():
        if attacker == hero:
            select = questionary.select(
                'どうする？',
                choices=[
                    Choice(title="こうげき", value='attack'),
                    Choice(title="ぼうぎょ", value='defense'),
                    Choice(title="にげる", value='escape'),
                ],
            ).ask()
            if select == 'attack':
                attacker.attack(defender, monster.defence_point)
                attacker, defender = defender, attacker
            elif select == 'defense':
                attacker.attack(defender, monster.defence_point)
                attacker, defender = defender, attacker
            else:
                break
        else:
            attacker.attack(defender, monster.defence_point)
            attacker, defender = defender, attacker

    print()
    if monster.is_dead():
        print('勇者は戦闘に勝った！')
    else:
        print('勇者は戦闘に負けた！')


if __name__ == '__main__':
    main()
