from django.db import models

# Create your models here.
class Books(models.Model):
    name=models.CharField(max_length=200,unique=True)
    author=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    publisher=models.CharField(max_length=200)
    publish_date=models.DateField(null=True)


    def __str__(self) :
        return self.name

