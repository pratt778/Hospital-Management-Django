from django.db import models
from datetime import date
# Create your models here.
class Doctor(models.Model):
    Doctor_name = models.CharField(max_length=100)
    Contact_no = models.IntegerField()
    Speciality = models.CharField(max_length=100)
    
    def __str__(self):
        return self.Doctor_name
    
class Patient(models.Model):
    Patient_name = models.CharField(max_length=100)
    Gender_Choices = (('Male','male'),('Female','female'),('Others','others'))
    Gender = models.CharField(max_length=100,choices=Gender_Choices,default='Male')
    Address = models.CharField(max_length=100)

    def __str__(self):
        return self.Patient_name
    
class Appointment(models.Model):
    Doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    Patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    Book_date = models.DateField()
    Book_time = models.TimeField()

    def __str__(self):
        return self.Doctor.Doctor_name+'<-------------->'+self.Patient.Patient_name
    

class ContactForm(models.Model):
    Fullname = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)
    Email = models.EmailField()
    Subject=models.CharField(max_length=200)
    Message = models.TextField()
    Sent_Date = models.DateField(default=date.today)

    def __str__(self):
        return self.Fullname+', Subject='+self.Subject



