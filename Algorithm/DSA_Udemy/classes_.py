from typing import overload


# MRO (Method Resolution Order)

class Base:
    def greet(self):
        print("Hello from Base")

class Left(Base):
    def greet(self):
        print("Hello from Left")
        super().greet()

class Right(Base):
    def greet(self):
        print("Hello from Right")
        super().greet()

class MROExample(Left, Right):
    def __init__(self, p: int):
        self.p = p
        print("Init Function.")

    def greet(self):
        print("Hello from MROExample")
        super().greet()


# Instantiate and check behavior
obj = MROExample(10)
obj.greet()

# Show MRO order
print("\nMethod Resolution Order:")
for cls in MROExample.__mro__:
    print(cls)
