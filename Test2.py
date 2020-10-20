class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()


class Photography:
    def __init__(self, camera, shots):
        self.camera = camera
        self.shots = shots

    def myfunc(self):
        print("My camera is a " + self.camera)
        
p1 = Photography("Nikon", 52)
p1.myfunc()
#"Test page"