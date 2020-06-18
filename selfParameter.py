class State(object):
    def __init__(self):
        self.field = 5.0
 
    def add(self, x):
        self.field += x
 
    def mul(self, x):
        self.field *= x
 
    def div(self, x):
        self.field /= x
 
    def sub(self, x):
        self.field -= x
 
 
s = State()
print(s.field)
 
s.add(2)         # Self is implicitly passed.
print(s.field)
 
s.mul(2)         # Self is implicitly passed.
print(s.field)
 
s.div(2)         # Self is implicitly passed.
print(s.field)
 
s.sub(2)         # Self is implicitly passed.
print(s.field)