class User():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        print(f'The user is {self.name} and they are {self.age} years old')

    @property
    def get_name(self):
        return self.name
    
    @property
    def get_age(self):
        return self.age
    
    @get_name.setter
    def set_name(self, new_name):
        if new_name.isalpha():
            self.name = new_name
        else:
            print("Name must only contain letters")

    @get_age.setter
    def set_age(self, new_age):
        if type(new_age) == int and new_age > 0:
            self.age = new_age
        else: 
            print("Your age must be real")

user1 = User("Bob", 30)
print(user1.get_name)
user1.set_name = "Lar6"


