#Single Inheritance
# class Car:
#     def steering(self):
#         print("Comfortable to ride")
# class Bike(Car):
#     def Gear(self):
#         print("^ six Speed Gear Box")
# c=Bike()
# c.steering() 
# c.Gear()  

# multiple inheritance
# class Travels:
#     def busname(self):
#         print("Swamy Ayyappa")
# class Travels1:
#     def bustype(self):
#         print("VOlvo 9600 SLX")

# class main_class(Travels,Travels1):
#     def Price(self):
#         print("3500RS")
# M=main_class()
# M.busname()
# M.bustype()
# M.Price()

# multilevel inheritance
# class Car:
#     def Wheel(self):
#         print("ALLOY WHEEELS")
# class Benz(Car):
#     def Luxury(self):
#         print("Its a Costlier car ")
# class BYD(Benz):
#     def Comfort(self):
#         print("BYD Compare to Benz")
# b=BYD()
# b.Wheel()
# b.Comfort()
# b.Luxury()

# encapsulation
# class Mobile:
#     __model=""   #private
#     __price=0.0
#     __ram=0
#     __internal=0
#     def setModel(self,mod=""):
#         self.__model=mod
#     def getModel(self):
#         return self.__model
#     def setPrice(self,pri=""):
#         self.__Price=pri
#     def getPrice(self):
#         return self.__Price
#     def setRam(self,ra=""):
#         self.__ram=ra
#     def getRam(self):
#         return self.__ram
#     def setInternal(self,inte=""):
#         self.__internal=inte
#     def getInternal(self):
#         return self.__internal                
# M=Mobile()
# M.setModel("Iphone")
# M.setPrice(690000.0)
# M.setRam(128)
# M.setInternal(128)
# print(M.getModel(),M.getPrice(),M.getRam(),M.getInternal())

# abstraction
# from abc import ABC
# class bus(ABC):
#     def volvo(self):
#         print("Luxury Bus")
# class Lorry(bus):
#     def volvo(self):
#         print("Happy")
# class Car(bus):
#     def volvo(self):
#         print("COstlier car")
# A=bus()
# A.volvo()                
# l=Lorry()
# l.volvo()
# c=Car()
# c.volvo()

# polymorphism overriding
# class Animal:
#     def speak(self):
#         print("Animal sound is louder")
# class Cat(Animal):
#     def speak(self):
#         print("meaow")
# class Dog(Animal):
#     def speak(self):
#         print("Dogs")
# C=Cat()
# D=Dog()
# C.speak()
# D.speak()


# polymorphisim overloading
# class sam:
#     def Add(self,a):
#         print(a)
#     def Add(self,a,b):
#         print(a+b)
#     def Add(self,a,b,c):
#         print(a+b+c)
# s=sam()
# # s.Add(10)
# # s.Add(10,20)
# s.Add(10,20,30)

# class Load:
#     def loading(self,a=None,b=None,c=None):
#         if a!=None and b!=None and c!=None:
#             return a+b+c
#         elif a!=None and b!=None:
#             return a+b
#         else:
#             return a
# l=Load()
# print("Add",l.loading(125))
# print("Add",l.loading(125,125))
# print("Add",l.loading(125,125,125))