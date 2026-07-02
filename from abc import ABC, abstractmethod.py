#publish subscribe model in python
from abc import ABC, abstractmethod


# ----------------------------
# News Model
# ----------------------------
class News:
    def __init__(self, title, description):
        self.title = title
        self.description = description


# ----------------------------
# Subscriber Interface
# ----------------------------
class Subscriber(ABC):

    @abstractmethod
    def update(self, news):
        pass


# ----------------------------
# Notification Service
# ----------------------------
class NotificationService:

    @staticmethod
    def send(user, news):
        print(f"\n📱 Notification sent to {user.username}")
        print(f"Title: {news.title}")
        print(f"Description: {news.description}")


# ----------------------------
# Concrete Subscriber
# ----------------------------
class User(Subscriber):

    def __init__(self, username):
        self.username = username

    def update(self, news):
        NotificationService.send(self, news)


# ----------------------------
# Publisher
# ----------------------------
class NewsPublisher:

    def __init__(self):
        self.subscribers = []

    def subscribe(self, user):
        if user not in self.subscribers:
            self.subscribers.append(user)
            print(f"{user.username} subscribed.")

    def unsubscribe(self, user):
        if user in self.subscribers:
            self.subscribers.remove(user)
            print(f"{user.username} unsubscribed.")

    def notify(self, news):
        print("\nSending notifications to subscribers...\n")
        for subscriber in self.subscribers:
            subscriber.update(news)

    def publish_news(self, title, description):
        print("\n===================================")
        print("Publishing New News")
        print("===================================")

        # New object created
        news = News(title, description)

        print(f"News Created: {news.title}")

        # Notify all subscribers
        self.notify(news)


# ----------------------------
# Driver Code
# ----------------------------
if __name__ == "__main__":

    # Create publisher
    publisher = NewsPublisher()

    # Create users
    user1 = User("Ali")
    user2 = User("Sara")
    user3 = User("Ahmed")

    # Subscribe users
    publisher.subscribe(user1)
    publisher.subscribe(user2)
    publisher.subscribe(user3)

    # Publish first news
    publisher.publish_news(
        "Pakistan Wins Cricket Match",
        "Pakistan defeated Australia by 5 wickets."
    )

    # Unsubscribe one user
    print("\n-----------------------------")
    publisher.unsubscribe(user2)
    print("-----------------------------")

    # Publish another news
    publisher.publish_news(
        "Gold Prices Drop",
        "Gold prices decreased by Rs. 2,500 per tola."
    )
    
# assignment q2

from collections import Counter


# ---------------------------------
# Car Component Classes
# ---------------------------------
class Seat:

    def __init__(self, material="Fabric Seats"):
        self.material = material

    def __str__(self):
        return self.material


class Engine:

    def __init__(self, type_name="1.5L Petrol Engine"):
        self.type_name = type_name

    def __str__(self):
        return self.type_name


class Door:

    def __init__(self, count=4):
        self.count = count

    def __str__(self):
        return str(self.count)


class Multimedia:

    def __init__(self, system="Basic Multimedia"):
        self.system = system

    def __str__(self):
        return self.system


class Suspension:

    def __init__(self, type_name="Standard Suspension"):
        self.type_name = type_name

    def __str__(self):
        return self.type_name


class ElectricalSystem:

    def __init__(self, system="Standard Electrical System"):
        self.system = system

    def __str__(self):
        return self.system


# ---------------------------------
# Car Class
# ---------------------------------
class Car:

    def __init__(
        self,
        seats=None,
        engine=None,
        doors=None,
        multimedia=None,
        suspension=None,
        electrical_system=None
    ):

        self.seats = seats if seats is not None else Seat()
        self.engine = engine if engine is not None else Engine()
        self.doors = doors if doors is not None else Door()
        self.multimedia = multimedia if multimedia is not None else Multimedia()
        self.suspension = suspension if suspension is not None else Suspension()
        self.electrical_system = (
            electrical_system if electrical_system is not None else ElectricalSystem()
        )

    def __str__(self):
        return (
            f"Car("
            f"Seats={self.seats}, "
            f"Engine={self.engine}, "
            f"Doors={self.doors}, "
            f"Multimedia={self.multimedia}, "
            f"Suspension={self.suspension}, "
            f"Electrical={self.electrical_system})"
        )


# ---------------------------------
# Singleton Factory
# ---------------------------------
class CarFactory:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CarFactory, cls).__new__(cls)
            cls._instance.cars = []
        return cls._instance

    # Factory Method
    def create_car(
        self,
        seats=None,
        engine=None,
        doors=None,
        multimedia=None,
        suspension=None,
        electrical_system=None
    ):

        car = Car(
            seats=seats,
            engine=engine,
            doors=doors,
            multimedia=multimedia,
            suspension=suspension,
            electrical_system=electrical_system
        )

        self.cars.append(car)

        print("Car Created Successfully!")
        return car

    # Get all cars
    def get_all_cars(self):
        return self.cars

    # Count cars by full configuration
    def get_car_counts(self):
        return Counter(str(car) for car in self.cars)


# ---------------------------------
# Driver Code
# ---------------------------------
if __name__ == "__main__":

    # Singleton check
    factory1 = CarFactory()
    factory2 = CarFactory()

    print("Same Factory Instance:", factory1 is factory2)

    print("\n----------------------------")

    # Default Car
    car1 = factory1.create_car()

    # Luxury Car
    car2 = factory1.create_car(
        seats=Seat("Leather Seats"),
        engine=Engine("2.0L Turbo Engine"),
        multimedia=Multimedia("12-inch Touch Screen"),
        suspension=Suspension("Sport Suspension"),
        electrical_system=ElectricalSystem("Premium Electrical System")
    )

    # Electric Car
    car3 = factory1.create_car(
        seats=Seat("Premium Leather"),
        engine=Engine("Electric Motor"),
        multimedia=Multimedia("Tesla Style Display"),
        suspension=Suspension("Adaptive Suspension"),
        electrical_system=ElectricalSystem("800V Electrical System")
    )

    print("\n========== Cars Produced ==========" + "\n")

    for i, car in enumerate(factory1.get_all_cars(), start=1):
        print(f"Car {i}")
        print(car)
        print()

    print("========== Production Count ==========")

    counts = factory1.get_car_counts()

    for car_description, count in counts.items():
        print(f"{count} x {car_description}")
