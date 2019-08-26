class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
class Student(Person):
    def __init__(self, first_name, last_name, gpa, classes = []):
        super().__init__(first_name, last_name)
        self.gpa = gpa
        self.classes = classes
    
    def update_gpa(self, gpa):
        self.gpa = gpa


class Teacher(Person):
    def __init__(self, first_name, last_name, tenure, subject):
        super().__init__(first_name, last_name)
        self.tenure = tenure
        self.subject = subject
    
    def add_students(self, students):
        self.students = students 

class Food:
    def __init__(self, name, healthy, price):
        self.name = name
        self.healthy = healthy
        self.price = price

class ShoppingList:
    def __init__(self, shopping_list=[]):
        self.shopping_list = shopping_list

    def add_to_list(self, name, healthy, price):
        food = Food(name, healthy, price)
        self.shopping_list = shopping_list.append(food)

    def view_list(self):
        print(self.shopping_list)

# justin = Student('Justin', 'Sarraga', 4.0, ['web development'])
# print(justin.first_name)
# print(justin.gpa)
# justin.update_gpa(2.3)
# print(justin.gpa)

apple = Food('apple',True,1.0)
print(apple.name, apple.healthy, apple.price)
ShoppingList.add_to_list('apple', True, 1.0)
print(ShoppingList.shopping_list)