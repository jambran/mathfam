class Animal:

    def __init__(self, color, num_legs):
        self.color = color
        self.num_legs = num_legs

    def speak(self):
        print('the animal talks!')

    def how_many_legs(self):
        print(f"I've got {self.num_legs} legs")

class Cat(Animal):

    def speak(self):
        print('Meow!')




if __name__ == '__main__':
    a = Cat(color='blue',
               num_legs=4)
    a.speak()
    a.how_many_legs()
