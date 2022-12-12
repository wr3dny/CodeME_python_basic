class Student:
    min_avg = 4.5 # jak to działa ? przy 4.5 wyrzuca bład

    def __init__(self, name, last, student_avg, scholarship):
        self.name = name
        self.last = last
        self.student_avg = student_avg
        self.scholarship = scholarship

    def __str__(self):
        return f'{self.name}{self.last} - srednia: {self.student_avg}'

    @property
    def fullname(self):
        return self.name.capitalize() + " " + self.last.capitalize()

    @property
    def email(self):
        return '{}.{}@university.com'.format(self.name.lower(), self.last.lower())

    def grant_scholarship(self):
        if self.student_avg > self.min_avg:
            self.scholarship = True
        else:
            self.scholarship = False


