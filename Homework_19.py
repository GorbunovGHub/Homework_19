class Buiding:
    def __init__(self):
        self.numberOfFloors = 10
        self.buildingType = 'десять'

    def __eq__(self, other):
        return self.numberOfFloors == other.buildingType


my_buiding = Buiding()

if Buiding.__eq__(self=my_buiding, other=my_buiding):
    print('True')
else:
    print('False')