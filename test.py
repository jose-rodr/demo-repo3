class Programmer:
    passion = 'Programming'

    def __init__(self, name, age, country, role):
        self.name = name
        self.age = age
        self.country = country
        self.role = role

    @classmethod
    def say_passion(cls):
        return f'My passion is {cls.passion}'

    @staticmethod
    def greet():
        return f"Hi, I am a programmer."
