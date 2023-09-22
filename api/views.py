from hpcl.models import CityModel , OutletAssignmentModel ,OutletModel , AttendanceModel , FormFieldModel
from rest_framework import viewsets
from .serializers import CitySerializer , UserSerializer ,OutletAssignmentSerializer,AttendenceSerializer,FormFieldSerializer
from rest_framework.response import Response
from accounts.models import Account

class CityViewSet(viewsets.ModelViewSet):
    queryset = CityModel.objects.all()
    serializer_class = CitySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = UserSerializer
    
    
class OutletAssignmentViewSet(viewsets.ModelViewSet):
    queryset = OutletAssignmentModel.objects.all()
    serializer_class = OutletAssignmentSerializer
    

    
class AttendenceViewSet(viewsets.ModelViewSet):
    queryset = AttendanceModel.objects.all()
    serializer_class = AttendenceSerializer
    
class FormFieldViewSet(viewsets.ModelViewSet):
    queryset = FormFieldModel.objects.all()
    serializer_class = FormFieldSerializer