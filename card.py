
class Card:
    def __init__(self, type, number):
        self.type = type
        self.number = number

    def show(self):
        print self.type, self.number
