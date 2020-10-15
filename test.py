class Programmer:
    passion = 'Programming'

<<<<<<< HEAD
    def __init__(self, name, age, country, role, tech_stack):
=======
    def __init__(self, name, age, country, role, company):
>>>>>>> cbf335ca2f852d0ccfa846302d45fb5a3709c7c8
        self.name = name
        self.age = age
        self.country = country
        self.role = role
<<<<<<< HEAD
        self.tech_stack = tech_stack
=======
        self.company = company
>>>>>>> cbf335ca2f852d0ccfa846302d45fb5a3709c7c8

    def change_role(self, new_role):
        self.role = new_role
        return f'My new role is {self.role}.'
    
    def say_age(self):
        return f'I am {self.age} years old.'

    @classmethod
    def say_passion(cls):
        return f'{cls.passion} is all about passion.'

    @staticmethod
    def greet():
        return f"Hi, I am a programmer."

<<<<<<< HEAD
jose = Programmer("José Gabriel", 16, "Dominican Republic", "Front-end developer", "MEAN")
=======
jose = Programmer("José Gabriel", 16, "Dominican Republic", "Front-end developer", "Google")
>>>>>>> cbf335ca2f852d0ccfa846302d45fb5a3709c7c8
