class Student:

  def show_class_name(self):
      print(self.__class__)

a = Student()
a.show_class_name()

class Student:
  def show_class_name(self):
      print(self.__class__.__name__)

a = Student()
a.show_class_name()

class Alien:
  def show_class_name(self):
      print(self.__class__.__name__, 'believes in extraterrestrials!')

class Student(Alien):
    pass

class Human(Alien):
    pass

s = Student()
s.show_class_name()

h = Human()
h.show_class_name()