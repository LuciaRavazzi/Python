# ---------------------
#       CLASS
# ---------------------


# ---- Introduction: class and objects.
# Python is a object oriented program because everything is
# a object, i.e. an instance of an object.
# even the basilar thing are objects.
x = 1  # it's an instance of int class.
print(type(x))


def hello():
    print("hello")


# function type: they are in-built objects.
# print(type(hello))

# A class is something abstract which is istantiated, i.e. an object.
string = "hello"
# a method is defined because the object defined/inheritated it.
# print(string.upper())

# ---- First class.
# A class is made up by interesting methods.
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def bark(self):
        print("bark")


d = Dog("Tim", 12)
d.set_age(24)
print(d.get_age())

# The strenght of a class is its re-usability: \inf number of objects can be istanciaced.


# ---- Communication between classes.
# It is possible to use a class as the input to another one.
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # 0- 100

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        self.is_active = False

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        values = 0
        for student in self.students:
            values += student.get_grade()

        return values / len(self.students)


s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("Jill", 19, 65)

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)
print(course.get_average_grade())


# ---- Inheritance.


class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don' t know")


class Cat(Pet):
    def __init__(self, name, age):
        # super refers to the super class
        # and it is calling the __init__ method.
        super().__init__(name, age)
        # This is done because it is undesired to rewrite the init method.

    def speak(self):
        print("Meow")


class Dog(Pet):
    def speak(self):
        print("Bark")


class Fish(Pet):
    pass


# There is too much redundancy to define Cat and dog separately -> inheritance.

p = Pet("Time", 19)
p.show()

# Child or derive classes: if a method is defined here, it override the one written into the parent class.
c = Cat("Bill", 34)
c.speak()

d = Dog("Billy", 34)
d.speak()

f = Fish("Billy", 34)
f.speak()


#
class Person:
    # it doesn't depend on the class.
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        # Person.number_of_people += 1 # track how many instances are created.
        Person.add_person()  # it is equal to teh previous line.

    # because it acts on something that isn't defined as self.
    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        print("M", cls.number_of_people)
        cls.number_of_people += 1


p1 = Person("Tim")
p2 = Person("Lucy")
# print("Number of people: ", Person.number_of_people)

# I can access to this variable.
# print(p1.number_of_people)
# Person.number_of_people = 8
# print(p2.number_of_people)


# --- Static method
# executed a set of operation but not cange the values of variables.
class Math:
    @staticmethod
    def add5(x):
        return x + 5


print(Math.add5(5))
