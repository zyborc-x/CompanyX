from django.db import models

class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    
class Details(models.Model):
    id = models.IntegerField(primary_key=True)
    tech = models.CharField(max_length=100)
    experience = models.IntegerField()
    age = models.IntegerField()


    def __str__(self):
        return f'{self.tech} {self.age} {self.experience}'