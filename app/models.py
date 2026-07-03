from django.db import models

# Create your models here.
class doctor(models.Model):
    doctor_name=models.CharField(max_length=100)
    doctor_fees=models.IntegerField()
    doctor_email=models.EmailField()
    doctor_number=models.BigIntegerField()
    doctor_image=models.ImageField()
    doctor_dept=models.CharField(max_length=200)
    

    def __str__(self):
        return self.doctor_name