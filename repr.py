class Warriors:
   def __init__(self, x, y):
     self.x = x
     self.y = y

   def __repr__(self):
     return f"Warriors({self.x}, {self.y})"

p1 = Warriors("Gohan", "Piccolo")

print(p1)