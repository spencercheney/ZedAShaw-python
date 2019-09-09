# animal is-a object
class Animal(object):
    pass

#Dog is-a animal
class Dog(Animal):

    def __init__(self, name):
        #dog has-a name
        self.name = name

#cat is-a animal
class Cat(Animal):
    
    def __init__(self, name):
        #Cat has-a name
        self.name = name

#person is-a object
class Person(object):
    
    def __init__(self, name):
        #person has-a name
        self.name = name

        #person has-a pet
        self.pet = None

#employee is-a person
class Employee(Person):
    
    def __init__(self, name, salary):
        #I believe this adds the name to person class
        super(Employee, self).__init__(name)
        #employee has-a salary
        self.salary = salary

#fish is-a object
class Fish(object):
    pass

#salmon is-a fish
class Salmon(Fish):
    pass

#halibut is-a fish
class Halibut(Fish):
    pass

#rover is-a dog
rover = Dog("Rover")

#satan is-a cat
satan = Cat("Satan")

#mary is-a person
mary = Person("Mary")

#mary's pet is satan
mary.pet = satan

#frank is-a employee with a $120000 salary
frank = Employee("Frank", 120000)

#frank's pet is rover
frank.pet = rover

#flipper is-a fish
flipper = Fish()

#crouse is-a salmon
crouse = Salmon()

#harry is-a halibut
harry = Halibut()
