from rest_framework import serializers
from hpcl.models import CityModel , Account , OutletAssignmentModel , AttendanceModel,FormFieldModel
from django.contrib.auth.hashers import make_password
from accounts.models import Account

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CityModel
        fields ="__all__"
        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
    def create(self, validated_data):
        # Hash the password before saving
        validated_data['password'] = make_password(validated_data['password'])
        
        return super().create(validated_data)
    
class OutletAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutletAssignmentModel
        fields = '__all__'
        
    def validate(self, data):
        outlet = data.get('outlet')
        user = data.get('user')
        status = data.get('status')

        # Check if an active assignment for the outlet already exists
        active_assignment = OutletAssignmentModel.objects.filter(outlet=outlet, status=True).first()

        # Check if an inactive assignment for the user already exists
        inactive_assignment = OutletAssignmentModel.objects.filter(user=user, status=True).first()

        if active_assignment:
            if active_assignment.user == user and status:
                raise serializers.ValidationError('Outlet already assigned to this user.')
            elif status:
                raise serializers.ValidationError('Outlet already assigned to another user.')
            elif not status:
                if active_assignment.user != user or active_assignment.outlet != outlet:
                    raise serializers.ValidationError('Outlet assigned to a different user. Cannot deactivate.')

        if inactive_assignment and not status:
            if inactive_assignment.outlet != outlet:
                raise serializers.ValidationError('User already assigned to a different outlet.')

        return data
    
class AttendenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceModel
        fields = '__all__'
        
class FormFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormFieldModel
        fields ="__all__"