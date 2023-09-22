from django.db import models
from datetime import datetime, timedelta
from accounts.models import Account
from django.utils import timezone


class CityModel(models.Model):
    city = models.CharField(max_length=100 , unique=True)
    status = models.CharField(max_length=10, choices=[('Active', 'Active'), ('Inactive', 'Inactive')])

    def __str__(self):
        return self.city


field_choices = [('Text' , 'Text') ,
                 ('Dropdown' , 'Dropdown'),
                 ('Radio' , 'Radio'),
                 ('Checkbox' , 'Checkbox'),
                 ('File' , 'File') , 
                 ('Number' , 'Number')]

class FormFieldModel(models.Model):
    form_type = models.CharField(max_length=100 , blank=True , null= True)
    label = models.CharField(max_length=100, blank=True , null=True)
    field_type = models.CharField(max_length=100, blank=True , null=True , choices=field_choices)
    options = models.CharField(max_length=100, blank=True , null=True)
    num_images = models.CharField(max_length=10, choices=[('1', '1'), ('2', '2'),('3', '3'), ('4', '4'),('5', '5')] , blank=True , null=True)
    priority = models.IntegerField(blank=True , null=True)
    req = models.CharField(max_length=10, choices=[('Yes', 'Yes'), ('No', 'No')])
    status = models.CharField(max_length=10, choices=[('Active', 'Active'), ('Inactive', 'Inactive')])
    
    def __str__(self):
        return self.label

    

class OutletModel(models.Model):
    
    cityReg = models.ForeignKey(CityModel , on_delete=models.CASCADE , default='')
    name = models.CharField(max_length=100 , blank=True , null=True )
    code = models.CharField(max_length=100 , blank=True , null=True ,unique=True)
    address = models.CharField(max_length=100 , blank=True , null=True )
    lat = models.CharField(max_length=100 , blank=True , null=True  )
    long = models.CharField(max_length=100 , blank=True , null=True  )
    status = models.CharField(max_length=10, choices=[('Active', 'Active'), ('Inactive', 'Inactive')])
    
    
    def __str__(self):
        return self.name
    

class AreaModel(models.Model):
    name = models.CharField(max_length=300 , blank=True , null=True)
    code = models.CharField(max_length=100 , blank=True , null=True)
    outlet = models.ForeignKey(OutletModel , on_delete=models.CASCADE , default='')
    address = models.CharField(max_length=300 , blank=True , null=True)
    lat = models.CharField(max_length=100 , blank=True , null=True  )
    long = models.CharField(max_length=100 , blank=True , null=True  )
    
    def __str__(self):
        return self.name
    
    
class OutletAssignmentModel(models.Model):
    
    outlet = models.ForeignKey(OutletModel, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    assignment_start = models.DateTimeField(default=timezone.now())
    assignment_end = models.DateTimeField(default=timezone.now() + timedelta(hours=24) , blank=True )
    status = models.CharField(max_length=10, choices=[('Active', 'Active'), ('Inactive', 'Inactive')] ,default='Active')
    


    def __str__(self):
        return str(self.outlet)
    
    def is_assignment_active(self):
        now = datetime.now()
        return self.assignment_start <= now <= self.assignment_end and self.status
    
    

class AttendanceModel(models.Model):
  
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    checkin = models.DateTimeField()
    checkin_image = models.ImageField(upload_to='checkin/',null=True, default="",blank=True)
    checkout = models.DateTimeField(blank=True , null=True) 
    checkout_image = models.ImageField(upload_to='checkout/',null=True, default="",blank=True)
    lat = models.CharField(max_length=100 , blank=True , null=True,default=0.0  )
    long = models.CharField(max_length=100 , blank=True , null=True ,default=0.0)
    lat1 = models.CharField(max_length=100 , blank=True , null=True,default=0.0  )
    long2 = models.CharField(max_length=100 , blank=True , null=True ,default=0.0)
    status = models.CharField(max_length=10, choices=[('Active', 'Active'), ('Inactive', 'Inactive')])
    
    
    def __str__(self):
        return f"{self.user.name} - {self.checkin}"
    
    
    
