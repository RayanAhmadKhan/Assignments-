# #publish subscribe model in python

# from abc import ABC, abstractmethod


# # News Model , storing title and description
# class News:
#     def __init__(self, title, description):
#         self.title = title
#         self.description = description


# # Subscriber abstract class
# class Subscriber(ABC):

#     @abstractmethod
#     def update(self, news):
#         pass


# # Notification Service, Display the content 
# class NotificationService:

#     @staticmethod
#     def send(user, news):
#         print(f"\n📱 Notification sent to {user.username}")
#         print(f"Title: {news.title}")
#         print(f"Description: {news.description}")


# # User as real Subscriber
# class User(Subscriber):

#     def __init__(self, username):
#         self.username = username

#     def update(self, news):
#         NotificationService.send(self, news)


# # Publisher (can be news channel lets say)
# class NewsPublisher:

#     def __init__(self):
#         self.subscribers = []

#     def subscribe(self, user): #subscriberss 
#         if user not in self.subscribers:
#             self.subscribers.append(user)
#             print(f"{user.username} subscribed.")

#     def unsubscribe(self, user):
#         if user in self.subscribers:
#             self.subscribers.remove(user)
#             print(f"{user.username} unsubscribed.")

#     def notify(self, news): #notifications
#         print("\nSending notifications to subscribers...\n")
#         for subscriber in self.subscribers:
#             subscriber.update(news)

#     def publish_news(self, title, description):  #adding news
#         print("\n===================================")
#         print("Publishing New News")
#         print("===================================")

#         # New object created
#         news = News(title, description)

#         print(f"News Created: {news.title}")

#         # Notify all subscribers
#         self.notify(news)


# #main code to test the implementation
# if __name__ == "__main__":

#     # Create publisher
#     publisher = NewsPublisher()

#     # Create users
#     user1 = User("Ali")
#     user2 = User("Sara")
#     user3 = User("Ahmed")

#     # Subscribe users
#     publisher.subscribe(user1)
#     publisher.subscribe(user2)
#     publisher.subscribe(user3)

#     # Publish first news
#     publisher.publish_news(
#         "Pakistan Wins Cricket Match",
#         "Pakistan defeated Australia by 5 wickets."
#     )

#     # Unsubscribe one user
#     print("\n-----------------------------")
#     publisher.unsubscribe(user2)
#     print("-----------------------------")

#     # Publish another news
#     publisher.publish_news(
#         "Gold Prices Drop",
#         "Gold prices decreased by Rs. 2,500 per tola."
#     )


#assignemnt q2 

from collections import Counter


# Car Class (defining the car object)

class Car:

    #constructor.
    def __init__(
        self,
        seats="Fabric Seats",
        engine="1.5L Petrol Engine",
        doors=4,
        multimedia="Basic Multimedia",
        suspension="Standard Suspension",
        electrical_system="Standard Electrical System"
    ):

        self.seats = seats
        self.engine = engine
        self.doors = doors
        self.multimedia = multimedia
        self.suspension = suspension
        self.electrical_system = electrical_system

    #car looks 
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

# Singleton Factory
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
        seats="Fabric Seats",
        engine="1.5L Petrol Engine",
        doors=4,
        multimedia="Basic Multimedia",
        suspension="Standard Suspension",
        electrical_system="Standard Electrical System"
    ):

        car = Car(
            seats,
            engine,
            doors,
            multimedia,
            suspension,
            electrical_system
        )

        self.cars.append(car)

        print("Car Created Successfully!")
        return car

    # Get all cars
    def get_all_cars(self):
        return self.cars

    # Count cars by engine type
    def get_car_counts(self):

        counts = Counter(car.engine for car in self.cars)

        return counts


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
        seats="Leather Seats",
        engine="2.0L Turbo Engine",
        multimedia="12-inch Touch Screen",
        suspension="Sport Suspension",
        electrical_system="Premium Electrical System"
    )

    # Electric Car
    car3 = factory1.create_car(
        seats="Premium Leather",
        engine="Electric Motor",
        multimedia="Tesla Style Display",
        suspension="Adaptive Suspension",
        electrical_system="800V Electrical System"
    )

    print("\n========== Cars Produced ==========\n")

    for i, car in enumerate(factory1.get_all_cars(), start=1):
        print(f"Car {i}")
        print(car)
        print()

    print("========== Production Count ==========")

    counts = factory1.get_car_counts()

    for engine, count in counts.items():
        print(f"{engine}: {count}")
