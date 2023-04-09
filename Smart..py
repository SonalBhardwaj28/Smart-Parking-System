import time

class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.available_spots = capacity
        self.parked_cars = []
        
    def park(self):
        if self.available_spots > 0:
            self.available_spots -= 1
            self.parked_cars.append(time.time())
            print("Car parked successfully.")
        else:
            print("No available spots.")
    
    def unpark(self, car_id):
        if car_id in self.parked_cars:
            self.parked_cars.remove(car_id)
            self.available_spots += 1
            print("Car unparked successfully.")
        else:
            print("Car not found.")
    
    def get_parked_cars(self):
        return self.parked_cars
    
    def get_available_spots(self):
        return self.available_spots
    
    def get_capacity(self):
        return self.capacity

class Car:
    def __init__(self, car_id):
        self.car_id = car_id
    
    def get_car_id(self):
        return self.car_id


def main():
    parking_lot = ParkingLot(5) # create a parking lot with 5 spots

    # simulate cars entering and exiting the parking lot
    car1 = Car(1)
    car2 = Car(2)
    car3 = Car(3)
    car4 = Car(4)
    car5 = Car(5)
    car6 = Car(6)

    parking_lot.park()
    parking_lot.park()
    parking_lot.park()
    parking_lot.park()
    parking_lot.park()

    print("Available spots:", parking_lot.get_available_spots())
    print("Parked cars:", parking_lot.get_parked_cars())

    parking_lot.unpark(car3.get_car_id())
    parking_lot.unpark(car5.get_car_id())

    print("Available spots:", parking_lot.get_available_spots())
    print("Parked cars:", parking_lot.get_parked_cars())

    parking_lot.park()

if __name__ == '__main__':
    main()
