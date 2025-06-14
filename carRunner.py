import car

def main():
    year_model = input("What is the year model of the car")
    make = input("what is the make of the car")
    my_car = car.Car(year_model, make)
    for i in range(5):
        my_car.accelerate()

    for i in range(5):
        my_car.brake()

if __name__ == "__main__":
    main()
        
