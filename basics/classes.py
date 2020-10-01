class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passangers = []

    def add_passanger(self, name):
        if not self.open_seats():
            return False

        self.passangers.append(name)
        return True
    
    def open_seats(self):
        return self.capacity - len(self.passangers)


flight = Flight(3)
people = ["harry","ron", "hermione", "ginny"]

for person in people:
    if flight.add_passanger(person):
        print(f"added {person}")
    else:
        print(f"cannot add {person}")

#p = Point(2,8)
#print(p.x)
#print(p.y)