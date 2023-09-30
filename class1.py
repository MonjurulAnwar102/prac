class Flight():
    def __init__(self,capacity):
        self.capacity=capacity
        self.passenger=[]


    def add_passanger(self,name):
        if not self.open_seats():
            return False
        self.passenger.append(name)
        return True

    def open_seats(self):
        return self.capacity-len(self.passenger)
    

flight=Flight(2)
person=["A","B","C","D"]

for people in person:
    success=flight.add_passanger(people)

    if success:
        print(f"Added {people} to flight successfully ")

    else:
        print(f"No availale seat for {people}")