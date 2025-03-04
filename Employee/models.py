from django.db import models

# Create your models here.
class Location(models.Model):
    name=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    country=models.CharField(max_length=200)


class Department(models.Model):
    name=models.CharField(max_length=200)
    location=models.ForeignKey(Location,on_delete=models.CASCADE)


class Employee(models.Model):   
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=254)
    designation=models.CharField(max_length=200)
    salary=models.FloatField()
    experience=models.SmallIntegerField()
    department_id=models.ForeignKey(Department,on_delete=models.CASCADE)
    profile_image=models.TextField(null=True,blank=True)

class Contact(models.Model):
    address=models.TextField()
    number=models.CharField(max_length=12)
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE)




    




