# polymorphism allows different classes to use the same method name but performs different actions
# when child class has the same method name, python calls the child's method first.

class Employee:
    def work(self):
        print("Employee is working")

class Developer(Employee):
    def execute(self):
        super().work()

    def work(self):
        print("Develper writes the code")

class Tester(Employee):
    def validate(self):
        super().work()

    def work(self):
        print("Tester tests the app")


d = Developer()
d.execute()

print("\n")

t = Tester()
t.validate()

