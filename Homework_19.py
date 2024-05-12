class Buiding:
    def __init__(self):
        self.numberOfFloors = 10
        self.buildingType = 'десять'

    def __eq__(self, other):
        other.numberOfFloors = 10
        other.buildingType = 'десять'
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


my_buiding1 = Buiding()
my_buiding2 = Buiding()

if my_buiding1 == my_buiding2:
    print('Одинаковые')
if my_buiding1 != my_buiding2:
    print('Не одинаковые')