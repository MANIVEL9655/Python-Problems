class parent:
    def method(self):
        print("This is class")
  
class child(parent):
    def __init__(self):
        print("This is sub class")
obj1=parent()
obj1.method()
# obj2=child()
# obj2.method2()