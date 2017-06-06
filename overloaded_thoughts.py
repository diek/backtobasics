'''subclass contains a method that overrides a method of the superclass,
you can also call the superclass method by calling
super(Subclass, self).method instead of self.method '''


class Thought():
    def __init__(self):
        pass

    def message(self):
        print("I feel like I am diagonally parked in a parallel universe.")


class Advice(Thought):
    def __init__(self):
        super(Advice, self).__init__()

    def message(self):
        print("Warning: Dates in a calendar are closer than they appear")

my_advice = Advice()
my_advice.message()
