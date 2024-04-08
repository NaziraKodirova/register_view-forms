from django.db import models
from student.models import Student

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Comments(models.Model):
    text = models.TextField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    publication_date = models.DateField()
    price = models.FloatField()
    count = models.IntegerField(default=1)
    comments = models.ManyToManyField(Comments)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} {self.price}"


class Booking(models.Model):
    book = models.ManyToManyField(Book)
    student = models.ManyToManyField(Student)
    take_date = models.DateTimeField(auto_now_add=True)
    returned_date = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.student} {self.book}"
