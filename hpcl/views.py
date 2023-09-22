from django.shortcuts import render ,HttpResponse , redirect , HttpResponseRedirect , get_object_or_404
from .forms import CityForm , UserForm , FormFieldForm , OutletForm , OutletAssignForm
from .models import CityModel  , FormFieldModel , OutletAssignmentModel , OutletModel,AttendanceModel
from rest_framework.response import Response
from django.db.models import Q
import csv
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.http import StreamingHttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.core.paginator import Paginator
from django.contrib.auth.models import User
import  csv
from django.utils.dateparse import parse_date
from django.contrib.auth.hashers import make_password
from datetime import timedelta
from django.contrib.auth import get_user_model
from accounts.models import Account

user = get_user_model()


# Create your views here.


def login_view(request):
    if request.method == 'POST':
        mobile = request.POST['mobile']
        password = request.POST['password']
        user = authenticate(request, mobile=mobile, password=password)
        if user:
            print("Print authenticated")
        if user is not None:
            login(request, user)
            print("login123434")
            return redirect('dash')  
        else:
            error_message = 'Invalid username or password'  # Customize the error message as needed
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

    
    
# user logout view

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


def dash(request) : 
    usr = Account.objects.all().count
    return render(request , 'dash.html' , {'usr' : usr} )

#USER MANAGEMENT
def userManage(request):
    usr = Account.objects.all()
    city = CityModel.objects.all()
    search = request.GET.get('search')
    cities = request.GET.get('citySearch')

    if search:
        usr = usr.filter(
            Q(name__icontains=search) |
            Q(code__icontains=search)
        )
    elif cities:
        usr = usr.filter(
            Q(cityReg__id__icontains=cities)
        )
    paginator = Paginator(usr, 10)  
    page_number = request.GET.get('page')
    usr = paginator.get_page(page_number)
    
    return render(request, 'usermanager.html', {'usr': usr, 'city': city})




def register(request):
    city = CityModel.objects.all()
    if request.method == 'POST':
        form = UserForm(request.POST)
        password = request.POST.get('password')
        cnfpass = request.POST.get('cnfPass')  # Note the change in name attribute
        
        if form.is_valid() :
            if password == cnfpass:
                hashed_password = make_password(password)
                print(hashed_password)
                form.instance.password = hashed_password
                form.save()
                return redirect('/user')
            else:
                error_message = "Password and Confirm Password do not match."
        else:
            error_message = ""
    else:
        error_message = None
        form = UserForm()

    return render(request, 'register.html', {'form': form, 'city': city, 'error_message': error_message})



def update_user(request, id):
    uid = Account.objects.get(pk=id)
    city = CityModel.objects.all()
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=uid)
        password = request.POST.get('password')
        cnfpass = request.POST.get('cnfPass') 
        if form.is_valid():
            if password == cnfpass:
                hashed_password = make_password(password)
                print(hashed_password)
                form.instance.password = hashed_password
                form.save()
                return redirect('/user')
        
            else:
                error_message = "Password and Confirm Password do not match."
        else:
            error_message = ""
    else:
        error_message = None
        form = UserForm(instance=uid)
    
        
    return render(request, 'updateUser.html', {'form': form , 'city' : city, 'error_message': error_message})


#Outlet Management

def outlet(request):
    city = CityModel.objects.all()
    out = OutletModel.objects.all().order_by('-id')
    search = request.GET.get('search')
    cities = request.GET.get('citySearch')
    usr = Account.objects.all()
    

    if search:
        out = out.filter(
            Q(name__icontains = search)
        )
    elif cities:
        out = out.filter(
            Q(cityReg__id__icontains=cities)
        )
    paginator = Paginator(out, 10)  
    page_number = request.GET.get('page')
    out = paginator.get_page(page_number)
    return render(request , 'outlet.html' , {'out' : out , 'city' : city , 'usr' : usr })





def updateOutlet(request , id):
    city = CityModel.objects.all()
    uid = OutletModel.objects.get(pk=id)
    if request.method == 'POST':
        form = OutletForm(request.POST, instance=uid)
        if form.is_valid():
            form.save()
            return redirect('/outlet')
    else:
        form = OutletForm(instance=uid)
    return render(request, 'updateOutlet.html', {'form': form , 'city' : city})




def assign_outlet_view(request):
    pass


def outReg(request):
    city = CityModel.objects.all()
    if request.method == 'POST':
        form = OutletForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/outlet')
    else:
        form = OutletForm()
    return render(request , 'outReg.html' , {'form': form , 'city' : city})








def assign_outlet(request, id):
    outlet = OutletModel.objects.get(pk=id)

    if request.method == 'POST':
        form = OutletAssignForm(request.POST, initial={'outlet': outlet})
        if form.is_valid():
            outlet = form.cleaned_data['outlet']
            status = form.cleaned_data['status']
            # Check if the outlet is already assigned
            existing_assignment = OutletAssignmentModel.objects.filter(outlet=outlet, status = True).exists()
            if existing_assignment:
                # Get the existing assignment
                existing_assignment = OutletAssignmentModel.objects.get(outlet=outlet)
                
                # Check if the outlet's status is inactive
                if not existing_assignment.status:
                    existing_assignment.delete()  # Delete the existing assignment
                else:
                    error_message = 'Outlet is already assigned.'
                    return render(request, 'assign_outlet.html', {'form': form, 'outlet': outlet, 'error_message': error_message})
            
            form.save()
            return HttpResponse('Success!')
        else:
            print(form.errors)
    else:
        form = OutletAssignForm(initial={'outlet': outlet})
    
    return render(request, 'assign_outlet.html', {'form': form, 'outlet': outlet})


def updateOutlet(request , id):
    city = CityModel.objects.all()
    uid = OutletModel.objects.get(pk=id)
    if request.method == 'POST':
        form = OutletForm(request.POST, instance=uid)
        if form.is_valid():
            form.save()
            return redirect('/outlet')
    else:
        form = OutletForm(instance=uid)
    return render(request, 'updateOutlet.html', {'form': form , 'city' : city})


def outActivity(request):
    user_id = request.user.id
    out = OutletAssignmentModel.objects.all()
    att = AttendanceModel.objects.all()
    return render(request , 'outActivity.html' , {'out' : out , 'att' : att ,'id' : user_id})


def attendence(request):
    att = AttendanceModel.objects.all()
    return render(request , 'attendence.html' , {'att' : att})


def updateActivity(request,id):
    oid = OutletAssignmentModel.objects.get(pk=id)
    if request.method == 'POST':
        form = OutletAssignForm(request.POST, instance=oid)
        if form.is_valid():
            form.save()
            return redirect('/outActivity')
    else:
        form = OutletAssignForm(instance=oid)
    return render(request , 'updateActivity.html' , { 'form' : form  })

#CITY 

def city(request):
    city = CityModel.objects.all()
    return render(request, 'city.html', {'city' : city})

def add_city(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('/city')
        
    else:
        form = CityForm()
    return render(request, 'cityReg.html', {'form': form})


def update_city(request, id):
    uid = CityModel.objects.get(pk=id)
    
    if request.method == 'POST':
        form = CityForm(request.POST, instance=uid)
        if form.is_valid():
            form.save()
            return redirect('/city')
    else:
        form = CityForm(instance=uid)
    return render(request, 'updateCity.html', {'form': form})



def area(request) :
    out = OutletModel.objects.all()
    return render(request , 'area.html' , {'out' : out})

def areaReg(request) :
    out = OutletModel.objects.all()
    return render(request , 'areaReg.html' , {'out' : out})







def fields(request):
    data = FormFieldModel.objects.all().order_by('-id')
    return render(request , 'fields.html' , {'data' : data})

def fieldsReg(request):
    if request.method == 'POST':
        form = FormFieldForm(request.POST, request.FILES) 
        print(form.errors)
        if form.is_valid():
            field = form.save(commit=False)
            field.save()  

            # Process and save the options as a comma-separated string
            options = request.POST.getlist('options[]')
            options_str = ', '.join(options)
            field.options = options_str
            field.save()

            return redirect('/fields')  # Replace 'success_page' with the appropriate URL name
    else:
        form = FormFieldForm()
    return render(request, 'fieldsReg.html', {'form': form})


def updateFields(request,id):
    oid = FormFieldModel.objects.get(pk=id)
    if request.method == 'POST':
        form = FormFieldForm(request.POST, instance=oid)
        if form.is_valid():
            form.save()
            return redirect('/fields')
        else:
            print(form.errors)
    else:
        form = FormFieldForm(instance=oid)
    return render(request , 'updateFields.html' , { 'form' : form  })

    

def raw(request):
    return render(request , 'raw.html')




class Echo:
    """An object that implements just the write method of the file-like
    interface.
    """

    def write(self, value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value

@login_required
def export_data(request):
    data = Account.objects.all()
    model_fields = Account._meta.fields
    excluded_fields = ['password']
    field_names = [field.name for field in model_fields if field.name not in excluded_fields]

    rows = ([getattr(row, field_name) for field_name in field_names] for row in data)
    rows = list(rows)  # Convert generator object to a list

    pseudo_buffer = Echo()
    writer = csv.writer(pseudo_buffer)

    response = StreamingHttpResponse(
        (writer.writerow(row) for row in [field_names] + rows),  
        content_type="text/csv"
    )
    response['Content-Disposition'] = 'attachment; filename="data.csv"'

    return response


def import_page(request):
    return render(request , 'import.html')


def import_data(request):
    if request.method == 'POST' and 'import' in request.FILES:
        csvfile = request.FILES['import']
        decoded_file = csvfile.read().decode('utf-8').splitlines()

        reader = csv.DictReader(decoded_file)
        c= 1
        rows = ""
        error_message = None
        
        
        for row in reader:
            c +=1
            cityReg = row['cityReg']
            name = row['name']
            
            
            code = row['code']
            if Account.objects.filter(code=code).exists():
                error_message = "Code already exists." 
                rows = "Error at row : " + str(c)
                
                
            mobile = row['mobile']
            if Account.objects.filter(mobile=mobile).exists():
                error_message = "Mobile number already exists."
                rows = "Error at row : " + str(c)
                
           
            password = row['password']

            try:
                city_instance = CityModel.objects.get(city=cityReg)
            except CityModel.DoesNotExist:
                # City doesn't exist, create a new CityModel instance
                city_instance = CityModel(city=cityReg)
                city_instance.save()
                
            if error_message:
                return render(request, 'import.html', {'error_message': error_message , 'rows' : rows}) 
            Account.objects.create(cityReg=city_instance, name=name, code=code, mobile=mobile,  password=password)
        return redirect('/user')
    
    return HttpResponse("Invalid request")




from django.shortcuts import get_object_or_404

from django.db.models import Q

def upbeatPlan(request):
    if request.method == 'POST' and 'import' in request.FILES:
        csvfile = request.FILES['import']
        decoded_file = csvfile.read().decode('utf-8').splitlines()

        reader = csv.DictReader(decoded_file)
        
        def parse_date(date_str):
            if date_str:
                date_obj = datetime.strptime(date_str, '%m/%d/%Y')
                return date_obj.strftime('%Y-%m-%d')
            return None
        
        c = 1
        rows = ""
        error_message = None
        
        for row in reader:
            c += 1
            outlet_name = row['outlet']
            outlets = OutletModel.objects.filter(Q(name__iexact=outlet_name)).all()
            if not outlets.exists():
                error_message = f'User with name "{outlet_name}" not found'
                rows = f"Error at row: {c}"
                return render(request, 'import.html', {'error_message': error_message, 'rows': rows})
            
            outlet = outlets.first()
            
            user_name = row['user']
            users = Account.objects.filter(Q(name__iexact=user_name)).all()
            
            if not users.exists():
                error_message = f'User with name "{user_name}" not found'
                rows = f"Error at row: {c}"
                return render(request, 'import.html', {'error_message': error_message, 'rows': rows})
            
            user = users.first()
            
            
            assignment_start = parse_date(row['assignment_start']) if row['assignment_start'] else None
           
            if error_message:
                return render(request, 'import.html', {'error_message': error_message, 'rows': rows}) 
            
            OutletAssignmentModel.objects.create(outlet=outlet, user=user, assignment_start=assignment_start)
        
        return redirect('/outActivity')
    
    return render(request, 'upbeatPlan.html')



def delete_data(request,id):
    if request.method=='POST':
        pi = OutletAssignmentModel.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/outActivity')
