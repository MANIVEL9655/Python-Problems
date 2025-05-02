class Car:    
    def method1(self,color, weight): 
        print("able to access object's attribute to method", color) 
        print("Weight of the car is ", weight)
obj1=Car()
obj1.method1("Green",4.4444)
print(type(obj1))
obj1.color="White"
obj1.weight=444
obj1.method1(obj1.color,obj1.weight)