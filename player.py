# The player and their stats class

NEN_TYPES = ["ENHANCEMENT", "TRANSMUTATION", "CONJURATION", "SPECIALIZATION", "MANIPULATION", "EMISSION"]
adjacent = 0.8
second_adjacent = 0.6
third_adjacent = 0.4
specialization = 0.0


class Player:
    def __init__(self, name, abilities, nen_type):
        self.name = name
        self.abilities = abilities
        self.nen_type = nen_type

    def create_ability(self, abilityName, abilityDesc, abilityType):
        self.abilities.append({abilityName : [abilityDesc, abilityType]})

    def print_abilities(self):
        for ability in self.abilities:
            print("".join(list(ability.keys())))

    def get_effectiveness(self, ability_type):
        nen_type_index = NEN_TYPES.index(self.nen_type)
        ability_index = NEN_TYPES.index(ability_type)

        if self.nen_type == "SPECIALIZATION":
            return 0

        distance = abs(nen_type_index - ability_index)
        if distance == 0:
            return 1.0
        elif distance == 1:
            return 0.8
        elif distance == 2:
            return 0.6
        elif distance == 3:
            return 0.4
        else:
            return 0
