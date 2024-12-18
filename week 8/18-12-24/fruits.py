class fruits:
    def eat(self):
        print("we can eat fruits")
class orange(fruits):
    pass
  # def eat(self)
      # print("orange is a sour fruit")
class apple(fruits):
    def eat(self):
        print("apple is sweet ")
org1=orange()
app1=apple()
org1.eat()
app1.eat()
