from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .models import Doctor,Patient,Appointment,ContactForm
from .forms import MyContactForm

# Create your views here.
def Home(request):
    return render(request,'index.html')

def Contact(request):
    data ={}
    form = MyContactForm()
    data['form']=form
    if request.method=="POST":
        form = MyContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'contact.html',data)

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
    data = {}
    mypati = Patient.objects.all()
    data['p']=len(mypati)
    mydoc = Doctor.objects.all()
    data['d']=len(mydoc)
    myapp = Appointment.objects.all()
    data['a']=len(myapp)
    return render(request,'admindash.html',data)

@login_required(login_url="adlogin")
def adlogout(request):
    logout(request)
    return redirect('home')

@login_required(login_url="adlogin")
def viewdoctor(request):
    mydoc=Doctor.objects.all()
    return render(request,'viewdoctor.html',{'doctors':mydoc})

@login_required(login_url="adlogin")
def viewpatient(request):
    mypatient = Patient.objects.all()
    return render(request,'viewpatient.html',{'patients':mypatient})

@login_required(login_url="adlogin")
def viewappoint(request):
    myapp = Appointment.objects.all()
    return render(request,'viewappoint.html',{'apps':myapp})

@login_required(login_url="adlogin")
def adddoctor(request):
    if request.method=="POST":
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        spec = request.POST.get('spec')

        mydoc = Doctor.objects.create(Doctor_name=name,Contact_no=contact,Speciality=spec)

    return render(request,'adddoctor.html')

@login_required(login_url="adlogin")
def addpatient(request):
    data={}
    mypati = Patient.Gender_Choices
    data['gender']=mypati
    # print(mypati)
    if request.method=="POST":
        name=request.POST.get('name')
        address=request.POST.get('address')
        gender=request.POST.get('gender')
        print(gender)
        
        mypatient = Patient.objects.create(Patient_name=name,Address=address,Gender=gender)

    return render(request,'addpatient.html',data)

@login_required(login_url="adlogin")
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

@login_required(login_url="adlogin")
def editdoctor(request,did):
    if request.method == "POST":
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        spec = request.POST.get('spec')
        mydoc = Doctor.objects.get(id=did)
        mydoc.Doctor_name=name
        mydoc.Contact_no=contact
        mydoc.Speciality=spec
        mydoc.save()
    mydoc = Doctor.objects.get(id=did)
    name = mydoc.Doctor_name
    contact = mydoc.Contact_no
    spec = mydoc.Speciality
    data={'name':name,"contact":contact,"speciality":spec}
    return render(request,'editdoctor.html',data)

@login_required(login_url="adlogin")
def deldoctor(request,did):
    mydoc = Doctor.objects.get(id=did)
    mydoc.delete()
    return redirect('viewdoctor')

@login_required(login_url="adlogin")
def editappoint(request,aid):
    if request.method=="POST":
        doc = request.POST.get('doctor')
        pati = request.POST.get('patient')
        date = request.POST.get('bookdate')
        time = request.POST.get('booktime')
        myapp = Appointment.objects.get(id=aid)
        myapp.Doctor.Doctor_name=doc
        myapp.Patient.Patient_name=pati
        myapp.Book_date=date
        myapp.Book_time=time
        myapp.save()
    data={}
    myapp = Appointment.objects.get(id=aid)
    mydoc = Doctor.objects.all()
    mypatient = Patient.objects.all()
    dname=myapp.Doctor.Doctor_name
    pname = myapp.Patient.Patient_name
    bdate = myapp.Book_date
    btime=myapp.Book_time
    data['dname']=dname
    data['pname']=pname
    data['bdate']=bdate.isoformat()
    data['btime']=btime.strftime('%H:%M')
    data['mydoc']=mydoc
    data['mypatient']=mypatient

    return render(request,'editappoint.html',data)

@login_required(login_url="adlogin")
def delappoint(request,aid):
    myapp = Appointment.objects.get(id=aid)
    myapp.delete()
    return redirect('viewappoint')

@login_required(login_url="adlogin")
def editpatient(request,pid):
    if request.method=="POST":
        name = request.POST.get('name')
        address=request.POST.get('address')
        gender=request.POST.get('gender')
        mypati = Patient.objects.get(id=pid)
        mypati.Patient_name=name
        mypati.Address=address
        mypati.Gender=gender
        mypati.save()
    data={}
    mypati = Patient.objects.get(id=pid)
    name = mypati.Patient_name
    add = mypati.Address
    gender= mypati.Gender
    data['name']=name
    data['add']=add
    data['gender']=gender
    return render(request,'editpatient.html',data)

@login_required(login_url="adlogin")
def delpatient(request,pid):
    mypati = Patient.objects.get(id=pid)
    mypati.delete()
    return redirect('viewpatient')

@login_required(login_url='adlogin')
def viewmsg(request):
    data={}
    mymsg = ContactForm.objects.all()
    data['msg']=mymsg
    return render(request,'viewmsg.html',data)


@login_required(login_url='adlogin')
def msgdetail(request,mid):
    data = {}
    mymsg = ContactForm.objects.get(id=mid)
    data['mymsg']=mymsg
    return render(request,'msgdetail.html',data)