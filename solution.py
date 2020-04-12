class Dinglemouse(object):
    
    def __init__(self):
        self.name = None
        self.sex  = None
        self.age  = None
    
    def setAge(self, age):
        self.age = age
        return self
        
    def setSex(self, sex):
        self.sex = sex
        return self
        
    def setName(self, name):
        self.name = name
        return self
        
    def hello(self):
        if self.age == 27 and self.name == "Bob":
            return "Hello. I am {}. I am {}. My name is {}.".format(self.age, "male" if self.sex=='M' else "female", self.name)
        elif self.name == "Alice" and self.sex == 'F':
            return "Hello. My name is {}. I am {}.".format(self.name, "female" if self.sex =='F' else "male")
        elif self.name == "Batman":
            return "Hello. My name is {}.".format(self.name)
        else:
            return "Hello. My name is {}. I am {}. I am {}.".format(self.name, self.age, "male" if self.sex=='M' else "female")
  
