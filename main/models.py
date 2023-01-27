from django.db import models


# Create your models here.
class Message(models.Model):
    name = models.TextField()
    email = models.EmailField()
    subject = models.CharField(max_length=20)
    message = models.TextField()

    date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} : {self.subject}'


categories = (
    ("w", "web"),
    ("a", "application"),
    ("g", "game"),
    ("m", "micro controller"),
    ("e", "else")
)


class Screenshot(models.Model):
    description = models.CharField(max_length=25)
    image = models.ImageField(upload_to="screenshots/")


class Project(models.Model):
    category = models.CharField(max_length=1, choices=categories, default="w")
    name = models.CharField(max_length=20)
    description = models.TextField()
    purpose = models.TextField()
    screenshots = models.ManyToManyField(Screenshot)
    repository = models.CharField(max_length=100)
    date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
