class Programmer:
    passion = 'Programming'

    def __init__(self, name, age, country, role, company, tech_stack):
        self.name = name
        self.age = age
        self.country = country
        self.role = role
        self.tech_stack = tech_stack
        self.company = company

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


jose = Programmer("José Gabriel", 16, "Dominican Republic",
                  "Front-end developer", "Google", "MEAN")
