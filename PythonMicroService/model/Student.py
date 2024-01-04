from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()

    def __dict__(self):
        return {'name': self.name, 'date': self.age}

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id