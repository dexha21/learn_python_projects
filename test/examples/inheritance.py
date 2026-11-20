class Mammal:
  def walk(self):
    print("walk")


class Dog(Mammal):
  def bark(self):
    print("bark")


class Cat(Mammal):
  def be_cute(self):
    print("^_^")


dog1 = Dog()
dog1.walk()

cat1 = Cat()
cat1.be_cute()