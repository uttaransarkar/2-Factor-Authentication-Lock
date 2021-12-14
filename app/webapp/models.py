from django.db import models

# Create your models here.
class UserRegister(models.Model):
    CAT = (
			('Master','Master'),
			('Known','Known'),
			)
    name = models.CharField(max_length=50,primary_key=True)
    category = models.CharField(max_length=10,choices=CAT)

    def __str__(self):
	    return self.name

class UserImages(models.Model):
    name = models.ForeignKey(UserRegister, on_delete=models.CASCADE)
    imagelinklist = models.ImageField()