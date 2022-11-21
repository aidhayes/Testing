init python:
    class Char:
        def __init__(self, stats={"hp": 100, "atk": 50, "def": 25}):
            self.stats = stats

        def apply_boost(self, character):
            self.stats.update({character.rship_boost_type: self.stats.get("hp") + character.rship_boost[character.rship_lvl]})
        

    mc = Char()


    class NPC:
        def __init__(self, name, stats, datable, rship_boost_type, rship_boost, relationship = 0, rship_lvl = 0):
            self.name = name
            self.relationship = relationship
            self.rship_lvl = rship_lvl
            self.stats = stats
            self.datable = datable
            self.rship_boost_type = rship_boost_type
            self.rship_boost = rship_boost


        def relationship_up(self, change):
            if self.rship_lvl is not 5:
                self.relationship += change
                renpy.notify("Relationship with " + self.name + " increased by " + str(change) + ". Current progress: (" + str(self.relationship) + "/100)")

            if self.relationship >= 5:
                self.rship_lvl = 1
                mc.apply_boost(self)
                renpy.notify("You have reached relationship level 1 with " + self.name)
            if self.relationship >= 20:
                self.rship_lvl = 2
                mc.apply_boost(self)
                renpy.notify("You have reached relationship level 2 with " + self.name)
            if self.relationship >= 40:
                self.rship_lvl = 3
                mc.apply_boost(self)
                renpy.notify("You have reached relationship level 3 with " + self.name)
            if self.rship_lvl >= 65:
                self.rship_lvl = 4
                mc.apply_boost(self)
                renpy.notify("You have reached relationship level 4 with " + self.name)
            if self.rship_lvl >= 100:
                self.relationship = 100
                mc.apply_boost(self)
                self.rship_lvl = 5
                renpy.notify("You have reached relationship level 5 with " + self.name)