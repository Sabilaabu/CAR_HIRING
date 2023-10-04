from django.db import models

class CAR(models.Model):
    TRANSMISSION_OPTIONS = [
        ('A', 'AUTOMATIC'),
        ('M', 'MANUAL'),
    ]
    STATUS_OPTIONS = [
        ('A', 'AVAILABLE'),
        ('T', 'TAKEN'),
    ]
    
    Plate_number = models.CharField(max_length=10)
    Make = models.CharField(max_length=15)
    Model = models.CharField(max_length=15)
    Capacity = models.CharField(max_length=100)
    Transmission = models.CharField(max_length=2, choices=TRANSMISSION_OPTIONS)
    Price_per_day = models.CharField(max_length=4)
    Status = models.CharField(max_length=2, choices=STATUS_OPTIONS)
    Driver = models.CharField(max_length=20)




class DRIVER(models.Model):
    GENDER_OPTIONS = [
        ('M', 'MALE'),
        ('F', 'FEMALE'),
    ]
   
    Name = models.CharField(max_length=20)
    Gender = models.CharField(max_length=2, choices= GENDER_OPTIONS)
    License_number = models.CharField(max_length=60)
    Contact = models.CharField(max_length=20)
    Address = models.CharField(max_length=30)

class HIRING(models.Model):
    SERVICE_TYPE_OPTIONS = [
        ('S', 'SELF DRIVE'),
        ('D', 'DRIVEN'),
    ]
    Hire_date = models.DateField(auto_now=False, auto_now_add=False)
    Customer = models.CharField(max_length=20)
    Car = models.CharField(max_length=20)
    Service_type = models.CharField(max_length=2, choices=SERVICE_TYPE_OPTIONS)
    Number_of_days = models.IntegerField()
    Amount_paid = models.IntegerField()

class PAYMENT(models.Model):
    Payment_date = models.DateField(auto_now=False, auto_now_add=False)
    Hire = models.CharField(max_length=20)
    Amount_paid = models.IntegerField()   