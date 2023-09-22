from django import forms
from .models import CityModel , FormFieldModel , OutletModel ,OutletAssignmentModel,AttendanceModel
from accounts.models import Account

from django.core.exceptions import ValidationError

class CityForm(forms.ModelForm):
    class Meta:
        model = CityModel
        fields = ['city', 'status']


class UserForm(forms.ModelForm):
    
    class Meta:
        model = Account
        fields = ['cityName','name' , 'code' , 'mobile' ,'role', 'status' , 'lock' , 'password']
        
        
    def clean(self):
        cleaned_data = super().clean()
       

        code = cleaned_data.get('code')
        mobile = cleaned_data.get('mobile')

        if Account.objects.filter(code=code).exclude(id=self.instance.id).exists():
            self.add_error('code', "Code is already registered.")

        if Account.objects.filter(mobile=mobile).exclude(id=self.instance.id).exists():
            self.add_error('mobile', "Mobile number is already registered.")
        
class FormFieldForm(forms.ModelForm):
    class Meta:
        model = FormFieldModel
        fields = '__all__'
        
class OutletForm(forms.ModelForm):
    class Meta:
        model = OutletModel
        fields = '__all__'
        
    def clean(self):
        cleaned_data = super().clean()
        code = cleaned_data.get('code')
        
        if Account.objects.filter(code=code).exclude(id=self.instance.id).exists():
            self.add_error('code', "Code is already registered.")
            
class OutletAssignForm(forms.ModelForm):

    class Meta:
        model = OutletAssignmentModel
        fields = "__all__"
    
    def clean(self):
        cleaned_data = super().clean()
        outlet = cleaned_data.get('outlet')
        user = cleaned_data.get('user')
        status = cleaned_data.get('status')
        
        
        # active_assignment = OutletAssignmentModel.objects.filter(outlet=outlet).first()
        # if active_assignment:
        #        self.add_error('outlet', "outlet is already registered.")
               
               
        # inactive_assignment = OutletAssignmentModel.objects.filter(user=user, status=True).first()
        # if inactive_assignment and not status:
        #     if inactive_assignment.outlet != outlet:
        #         self.add_error("User already assigned to a different outlet.")
                
        return cleaned_data
                
class AttendenceForm(forms.ModelForm):
    
    class Meta:
        model = AttendanceModel
        fields = "__all__"
        
     