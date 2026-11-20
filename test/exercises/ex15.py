class Person_:
  def __init__(self, name, word):
    self.name = name
    self.word = word
  
  def talk(self):
    print(self.word)
    
    
me = Person_("John Smith", "Hello World")

me.talk()



#Mosh
class Person:
  def __init__(self, name):
    self.name = name
  
  def talk(self):
    print(f"Hi,I am {self.name}")


john = Person("John Smith")
john.talk()
