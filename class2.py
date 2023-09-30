class BUS():
    def __init__(self, seat):
        self.seat = seat
        self.passengers = []

    def add_passenger(self, name):
        if self.open_seat() == 0:
            return False

        self.passengers.append(name)
        return True

    def open_seat(self):
        return self.seat - len(self.passengers)

ride = BUS(3)
people = ['kash', 'bash', 'cash', 'sash', 'dash']

for person in people:
    success = ride.add_passenger(person)

    if success:
        print(f"Added {person} to bus successfully")
    else:
        print(f"No available seat for {person}")
