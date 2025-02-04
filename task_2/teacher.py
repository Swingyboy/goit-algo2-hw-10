class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = can_teach_subjects
        self.assigned_subjects = set()

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age}, email: {self.email}\n   Викладає предмети: {', '.join(self.assigned_subjects)}\n"
    
    def __repr__(self):
        return f"Teacher({self.first_name}, {self.last_name}, {self.age}, {self.email}, {self.can_teach_subjects})"

    @classmethod
    def from_dict(cls, data):
        try:
            return cls(data["first_name"], data["last_name"], data["age"], data["email"], data["can_teach_subjects"])
        except KeyError:
            raise ValueError("Invalid data")

    @classmethod
    def from_tuple(cls, data):
        try:
            return cls(data[0], data[1], data[2], data[3], data[4])
        except IndexError:
            raise ValueError("Invalid data")