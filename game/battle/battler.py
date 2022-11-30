import json

class Battler:
    def __init__(self, name, playable):
        # TODO:Ensure name is valid before creating Battler
        self.name = name
        if playable:
            with open('./characters.json', 'r') as f:
                characters = json.load(f)
                character = characters[name]
                self.type = character['type']
                self.stats = character['stats']
                self.attacks = character['attacks']
        else:
            with open('./opponents.json', 'r') as f:
                characters = json.load(f)
                character = characters[name]
                self.type = character['type']
                self.stats = character['stats']
                self.attacks = character['attacks']

    def update_hp(self, change):
        self.stats[0] += change

    def buff(self, stat, change):
        if stat == "atk":
            self.stats[1] *= change
        elif stat == "def":
            self.stats[2] *= change

    def debuff(self, stat, change):
        if stat == "atk":
            self.stats[1] *= change
        elif stat == "def":
            self.stats[2] *= change

    def has_attack(self, attack):
        return attack in self.attacks

    def __str__(self):
        name = self.name
        type = self.type
        stats = f"HP: {self.stats[0]}\nATK: {self.stats[1]}\nDEF: {self.stats[2]}"
        attacks = f"{self.attacks[0]}, {self.attacks[1]}, {self.attacks[2]}, {self.attacks[3]}"
        return_str = f"{name}:\n\tType: {type}\n\tStats: {stats}\n\tAttacks: {attacks}"
        return return_str