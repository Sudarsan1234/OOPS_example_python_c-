class Employee(object):
    def __init__(self, **kwargs):
        for key in kwargs:
            setattr(self, key, kwargs[key])
 
 
emp = Employee(age=25, name="John Doe")
print(emp.age)
print(emp.name)

emp.salary = 1000   #added new property
emp.blood = "O+"
emp.city = "Delhi"

print(emp.city)

temp = vars(emp)
for item in temp:
    print(item, ':', temp[item])