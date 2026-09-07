# Inheritence allows a child class to use the properties and methods of a parent class
# It helps in code reuse and reduces duplicates code.
# It makes programms organized and esay to maintain


# without inheritence(Code Duplication)
# Developer -> work(), code()
# Tester    -> work(), test()
# work() method is repeated in both classes


class Employee:
    def work(self):
        print("Employee is working")


class Developer(Employee):
    def coder(self):
        print("developer is coding")

class Tester(Employee):
    def test(self):
        print("Tester is testing the app")

d = Developer()
d.work()
d.coder()

print("\n")
t = Tester()
t.work()
t.test()