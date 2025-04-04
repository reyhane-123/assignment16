from django.db import models
from django.urls import reverse
# Create your models here.
class Users(models.Model):
    name=models.CharField(max_length=50)
    family=models.CharField(max_length=50)
    phone=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=50 , null=True)
    status=models.BooleanField(default=True)
    is_deleted=models.BooleanField(default=False)
    password=models.CharField(max_length=15)
    created_add=models.DateField(auto_now_add=True,null=True)
    update=models.DateField(auto_now=True,null=True)
    class Meta:
        db_table='users'

class Course(models.Model):
    course_name=models.CharField(max_length=50)
    teacher=models.CharField(max_length=50)
    status=models.BooleanField(default=1)
    is_deleted=models.BooleanField(default=False)
    created_add=models.DateField(auto_now_add=True,null=True)
    update=models.DateField(auto_now=True,null=True)

    def get_course_detail(self):
        return reverse('detail_1',args=[self.id])

    class Meta:
        db_table='course'