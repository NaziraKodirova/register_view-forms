from django.db import models

class Address(models.Model):
   name = models.CharField(max_length=50)

   def __str__(self):
      return self.name
   

class Role(models.TextChoices):
   BAKALAVR = ('bakalavr', ('Bakalavr'))  
   MAGISTER = ('magister', ('Magister'))
   ASPIRANT = ('aspirant', ('Aspirant'))
   PROFESSOR = ('professor', ('Professor'))



class Student(models.Model):
   firts_name = models.CharField(max_length=50)
   last_name = models.CharField(max_length=50)
   age = models.PositiveBigIntegerField(null=True, blank=True)
   status = models.CharField(max_length=20, choices=Role.choices)
   address = models.ForeignKey(Address, on_delete=models.CASCADE)

   def __str__(self):
      return f"{self.firts_name} {self.last_name}"
