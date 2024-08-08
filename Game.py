# game.py

class Character:
    def __init__(self, name, route=None):
        self.name = name
        self.route = route
        self.experience = 0
        self.gold = 100
        self.level = 1
        self.subordinates = []
        self.bloodline = None
        self.kingdom = None

    def choose_route(self, route):
        if route in ['Mage', 'Knight', 'Thief', 'Healer']:
            self.route = route
            return f"{self.name} has chosen the route {self.route}."
        return "Invalid route. Choose 'Mage', 'Knight', 'Thief', or 'Healer'."

    def gather_gold(self, amount):
        self.gold += amount
        return f"{self.name} has gathered {amount} gold. Total gold: {self.gold}"

    def fight(self):
        if self.route == 'Knight':
            self.experience += 10
            self.gold += 5
            return f"{self.name} fought and gained 10 experience and 5 gold."
        elif self.route == 'Mage':
            self.experience += 8
            self.gold += 7
            return f"{self.name} used magic and gained 8 experience and 7 gold."
        elif self.route == 'Thief':
            self.experience += 6
            self.gold += 10
            return f"{self.name} stole and gained 6 experience and 10 gold."
        elif self.route == 'Healer':
            self.experience += 7
            self.gold += 5
            return f"{self.name} healed and gained 7 experience and 5 gold."
        return "Choose a route first."

    def show_status(self):
        status = f"\nName: {self.name}\nRoute: {self.route}\nExperience: {self.experience}\nGold: {self.gold}\nLevel: {self.level}"
        if self.bloodline:
            status += f"\nBloodline: {self.bloodline.name} ({self.bloodline.purity})"
        if self.kingdom:
            status += f"\n{self.kingdom.show_status()}"
        return status

    def level_up(self):
        required_experience = self.level * 100
        if self.experience >= required_experience:
            self.level += 1
            self.experience -= required_experience
            return f"{self.name} has leveled up to level {self.level}!"
        return f"Not enough experience. You need {required_experience - self.experience} more experience to level up."

class Bloodline:
    def __init__(self, name, cost, purity, stats):
        self.name = name
        self.cost = cost
        self.purity = purity
        self.stats = stats

class Shop:
    def __init__(self):
        self.bloodlines = [
            Bloodline("Dragon", 500, "Pure", {"strength": 10, "intelligence": 5}),
            Bloodline("Giant", 300, "Impure", {"strength": 8, "intelligence": 3}),
            Bloodline("Elf", 400, "Rare", {"strength": 5, "intelligence": 10}),
        ]

class Kingdom:
    def __init__(self, name, ruler):
        self.name = name
        self.ruler = ruler
        self.resources = {"wood": 100, "stone": 100, "food": 100}
        self.city_level = 1

    def show_status(self):
        resources = ", ".join(f"{k}: {v}" for k, v in self.resources.items())
        return f"Kingdom: {self.name}\nCity Level: {self.city_level}\nResources: {resources}"

    def develop_city(self):
        if self.resources["wood"] >= 50 and self.resources["stone"] >= 50:
            self.resources["wood"] -= 50
            self.resources["stone"] -= 50
            self.city_level += 1
            return f"{self.name} has developed to city level {self.city_level}."
        return "Not enough resources to develop city."

    def manage_resources(self, resource_type, amount):
        if resource_type in self.resources:
            self.resources[resource_type] += amount
            return f"Managed {amount} {resource_type}. Current {resource_type}: {self.resources[resource_type]}"
        return "Invalid resource type."
