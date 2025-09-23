class Father:
    def skills(self):
        return "Farming and Gardening"
class Son(Father):
    def skills(self):
        return "Sports, " + super().skills()
print(Son().skills())