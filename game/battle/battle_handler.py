import battler

class BattleHandler:
    def __init__(self, user_chars, ai_char):
        self.user_chars = self.init_chars(user_chars)
        self.ai_char = self.init_ai_char(ai_char)
        self.running = True

    def init_chars(self, char_list):
        battlers = []
        for name in char_list:
            battlers.append(battler.Battler(name, playable=True))
        return battlers

    def init_ai_char(self, char):
        ai_battler = battler.Battler(char, playable=False)
        return ai_battler

    def run(self):
        while self.running:
            pass
            # TODO: start working on the battle itself