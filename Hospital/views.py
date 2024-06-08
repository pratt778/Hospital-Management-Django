from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .models import Doctor,Patient,Appointment

# Create your views here.
def Home(request):
    return render(request,'index.html')

def Contact(request):
    return render(request,'contact.html')

def About(request):
    return render(request,'about.html')

def adminLogin(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        passw = request.POST.get('password')
        print(uname,passw)
        myuser = authenticate(username=uname,password=passw)
        if myuser is not None:
            login(request,myuser)
            return redirect('admindash')
    return render(request,'adminlogin.html')

@login_required(login_url="adlogin")
def admindash(request):
    return render(request,'admindash.html')

def adlogout(request):
    logout(request)
    return redirect('home')

def viewdoctor(request):
    mydoc=Doctor.objects.all()
    return render(request,'viewdoctor.html',{'doctors':mydoc})

def viewpatient(request):
    mypatient = Patient.objects.all()
    return render(request,'viewpatient.html',{'patients':mypatient})

def viewappoint(request):
    myapp = Appointment.objects.all()
    return render(request,'viewappoint.html',{'apps':myapp})

def adddoctor(request):
    if request.method=="POST":
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        spec = request.POST.get('spec')

        mydoc = Doctor.objects.create(Doctor_name=name,Contact_no=contact,Speciality=spec)

    return render(request,'adddoctor.html')

def addpatient(request):
    if request.method=="POST":
        name=request.POST.get('name')
        address=request.POST.get('address')
        gender=request.POST.get('gender')
        
        mypatient = Patient.objects.create(Patient_name=name,Address=address,Gender=gender)
    return render(request,'addpatient.html')


def addappoint(request):
    if request.method=="POST":
        doc = request.POST.get('doctor')
        pati = request.POST.get('patient')
        date = request.POST.get('bookdate')
        time = request.POST.get('booktime')
        doctor = Doctor.objects.get(Doctor_name=doc)
        patient=Patient.objects.get(Patient_name=pati)
        myapp = Appointment.objects.create(Doctor=doctor,Patient=patient,Book_date=date,Book_time=time)
    mydoc = Doctor.objects.all()
    mypatient = Patient.objects.all()
    return render(request,'addappoint.html',{'mydoc':mydoc,'mypatient':mypatient})