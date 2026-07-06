# from abc import ABC, abstractmethod
# import xml.etree.ElementTree as ET
# import json


# # -------------------------------------
# # Database Model (Stores XML)
# # -------------------------------------
# class UserModel:
#     def __init__(self, user_id, name_xml):
#         self.user_id = user_id
#         self.name_xml = name_xml


# # -------------------------------------
# # Adapter Interface
# # Defines the contract for converting data to JSON
# # -------------------------------------
# class JSONAdapter(ABC):

#     @abstractmethod
#     def get_json(self):
#         pass


# # -------------------------------------
# # Adapter
# # Converts XML -> JSON
# # -------------------------------------
# class XMLToJSONAdapter(JSONAdapter):

#     def __init__(self, user):
#         self.user = user

#     def get_json(self):
#         root = ET.fromstring(self.user.name_xml)

#         data = {}

#         for child in root:
#             data[child.tag] = child.text

#         return json.dumps(data, indent=4)


# # -------------------------------------
# # Singleton Display Service
# # -------------------------------------
# class DisplayService:

#     _instance = None

#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super(DisplayService, cls).__new__(cls)
#         return cls._instance

#     def display(self, adapter: JSONAdapter):
#         print("Printing Data...\n")
#         print(adapter.get_json())


# # -------------------------------------
# # Driver Code
# # -------------------------------------
# if __name__ == "__main__":

#     xml_data = """
#     <user>
#         <name>Ali</name>
#         <age>22</age>
#         <city>Lahore</city>
#     </user>
#     """

#     user = UserModel(1, xml_data) #store user data as XML in the database

#     adapter = XMLToJSONAdapter(user)

#     display1 = DisplayService()
#     display2 = DisplayService()

#     print("Same Display Service:", display1 is display2)
#     print()

#     display1.display(adapter)


# -------------------------------------
# Q4 - ASIGNMENT
# -------------------------------------
class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# -------------------------------------
# Hash Table
# -------------------------------------
class HashTable:

    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    # Custom Hash Function
    def hash_function(self, key):

        hash_value = 0

        for char in key:
            hash_value += ord(char)

        return hash_value % self.size

    # Insert
    def put(self, key, value):

        index = self.hash_function(key)

        new_node = Node(key, value)

        if self.table[index] is None:
            self.table[index] = new_node
            return

        current = self.table[index]

        while current:

            if current.key == key:
                current.value = value
                return

            if current.next is None:
                break

            current = current.next

        current.next = new_node

    # Search
    def get(self, key):

        index = self.hash_function(key)

        current = self.table[index]

        while current:

            if current.key == key:
                return current.value

            current = current.next

        return None

    # Delete
    def remove(self, key):

        index = self.hash_function(key)

        current = self.table[index]
        previous = None

        while current:

            if current.key == key:

                if previous is None:
                    self.table[index] = current.next
                else:
                    previous.next = current.next

                return True

            previous = current
            current = current.next

        return False

    # Display
    def display(self):

        print("\nHash Table\n")

        for i in range(self.size):

            print(f"Bucket {i}:", end=" ")

            current = self.table[i]

            if current is None:
                print("Empty")
                continue

            while current:
                print(f"[{current.key}:{current.value}]", end=" -> ")
                current = current.next

            print("None")


# -------------------------------------
# Driver Code
# -------------------------------------
if __name__ == "__main__":

    ht = HashTable()

    ht.put("Ali", 90)
    ht.put("Sara", 85)
    ht.put("Ahmed", 88)
    ht.put("Bilal", 91)

    ht.display()

    print("\nSearching")
    print("Ali:", ht.get("Ali"))
    print("Sara:", ht.get("Sara"))

    print("\nRemoving Sara")
    ht.remove("Sara")

    ht.display()    