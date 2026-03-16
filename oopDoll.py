#21/11/25

class Doll:

    def __init__(self,name,greeting="Hello"):
        self.name = name
        self.greeting = greeting

    def say_hello(self):
        print(self.greeting,"I am",self.name)

callum = Doll("Callum")
david = Doll("David",greeting = "I'm hella friggin tuff cuz")
carmichael = Doll("Carmichael",greeting = "Skibidi hawk tuah gyat rizz baby gronk")

callum.say_hello()
david.say_hello()
carmichael.say_hello()