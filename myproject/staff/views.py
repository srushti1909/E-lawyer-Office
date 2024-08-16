from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
# from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from adminlawyer.models import *
import os
# import mysql.connector


def layout(request):
    context = {}
    return render(request,'staff/layout.html',context)

def profile(request):
    context = {}
    return render(request,'staff/profile.html',context)

def header(request):
    context = {}
    return render(request,'staff/header.html',context)

def sidebar(request):
    context = {}
    return render(request,'staff/sidebar.html',context)

def footer(request):
    context = {}
    return render(request,'staff/footer.html',context)

def dashboard(request):
    case  = Cases.objects.all().count()
    client = Client.objects.all().count()
    lawyer = Lawyer.objects.all().count()
    doc    = Documents.objects.all().count()
    app    = Appointment.objects.all().count()
    context = {'case':case,'client':client,'lawyer':lawyer,'doc':doc,'app':app}
    return render(request,'staff/dashboard.html',context)

def table(request):
    context = {}
    return render(request,'staff/table.html',context)

def form(request):
    context = {}
    return render(request,'staff/form.html',context)

def calendar(request):
    context = {}
    return render(request,'staff/calendar.html',context)

def accept_appointment(request,id):
    data = {
                'status' : "Approved",
           }
    Appointment.objects.update_or_create(pk=id, defaults=data)
    return redirect('/staff/view_appointment')

def reject_appointment(request,id):
    data = {
                'status' : "Rejected",
           }
    Appointment.objects.update_or_create(pk=id, defaults=data)
    return redirect('/staff/view_appointment')

def add_case(request):
    result = Client.objects.all()
    context = {'result':result}
    return render(request,'staff/add_case.html',context)

def add_client(request):
    context = {}
    return render(request,'staff/add_client.html',context)

def add_doc(request,id):
    result  = Cases.objects.get(pk=id)
    context = {'result':result}
    return render(request,'staff/add_doc.html',context)

def add_date(request,id):
    result  = Cases.objects.get(pk=id)
    context = {'result':result}
    return render(request,'staff/add_date.html',context)

def view_doc(request):
    result = Documents.objects.all()
    context = {'result':result}
    return render(request, 'staff/view_doc.html',context)

def add_member(request):
    context = {}
    return render(request,'staff/add_member.html',context)

def view_cases(request):
    id = request.user.id
    user = User.objects.get(pk=id)
    cases = Cases.objects.filter(status="Running")
    lawyer = Lawyer.objects.all()
    context = {'cases':cases,'user':user,'lawyer':lawyer}
    return render(request,'staff/view_cases.html',context)


def all_cases(request,id):
    result  = Cases.objects.get(pk=id)
    context = {'result':result}
    return render(request, 'staff/all_cases.html',context)


def view_client(request):
    result = Client.objects.all()
    context = {'result':result}
    return render(request, 'staff/view_client.html',context)

def view_doc(request):
    result = Documents.objects.all()
    context = {'result':result}
    return render(request,'staff/view_doc.html',context)

def view_date(request):
    result = Schedule.objects.all()
    context = {'result':result}
    return render(request,'staff/view_date.html',context)


def view_all_date(request):
    result = Schedule.objects.all()
    context = {'result':result}
    return render(request,'staff/view_all_date.html',context)


def view_member(request):
    result = Lawyer.objects.all()
    context = {'result':result}
    return render(request,'staff/view_member.html',context)

def view_feedback(request):
    result = Feedback.objects.all().order_by('date')
    context = {'result':result}
    return render(request,'staff/view_feedback.html',context)

def view_appointment(request):
    result = Appointment.objects.filter(status="Pending")
    approved = Appointment.objects.filter(status="Approved").order_by('date')
    context = {'result':result,'approved':approved}
    return render(request,'staff/view_appointment.html',context)
    
def login(request):
    context = {}
    return render(request,'staff/login.html',context)


def logout(request):
    auth.logout(request)
    return redirect('/staff/login')


def lawyer_store(request):
    username    = request.POST['username']
    email = request.POST['email']
    lawyer_name = request.POST['lawyer_name']
    password = request.POST['password']
    dob = request.POST['dob']
    age = 20
    gender = request.POST['gender']
    contact = request.POST['contact']
    qualification = request.POST['qualification']
    experience = request.POST['experience']
    registration_date = request.POST['registration_date']
    address = request.POST['address']
    city = request.POST['city']
    state = request.POST['state']
    zipcode = request.POST['zipcode']
    photo = request.FILES['photo']
    mylocation = os.path.join(settings.MEDIA_ROOT, 'staff')
    obj = FileSystemStorage(location=mylocation)
    obj.save(photo.name, photo)

    result = User.objects.create_user(email=email,username=username,password=password)
    Lawyer.objects.create(qualification = qualification, experience = experience, registration_date = registration_date, photo = photo.name, username = username, lawyer_name = lawyer_name, email = email, address = address, contact = contact, password = password, dob = dob, age = age, gender = gender, city_id = city, state_id = state, zipcode = zipcode,user_id=result.id)
    return redirect('/staff/add_member')



def login_check(request):
    username = request.POST['username']
    password = request.POST['password']

    result = auth.authenticate(request, username=username, password=password)

    if result is None:
        print('Invalid Username Or Password')
        return redirect('/staff/login')
    else:
        auth.login(request, result)
        return redirect('/staff/dashboard')



def client_store(request):
    username    = request.POST['username']
    email = request.POST['email']
    client_name = request.POST['client_name']
    password = request.POST['password']
    dob = request.POST['dob']
    age = 20
    gender = request.POST['gender']
    contact = request.POST['contact']
    address = request.POST['address']
    city = request.POST['city']
    state = request.POST['state']
    zipcode = request.POST['zipcode']
    photo = request.FILES['photo']
    mylocation = os.path.join(settings.MEDIA_ROOT, 'client')
    obj = FileSystemStorage(location=mylocation)
    obj.save(photo.name, photo)

    result = User.objects.create_user(email=email,username=username,password=password)
    Client.objects.create(photo = photo.name, username = username, client_name = client_name, email = email, address = address, contact = contact, password = password, dob = dob, age = age, gender = gender, city_id = city, state_id = state, zipcode = zipcode,user_id=result.id)
    return redirect('/staff/add_client')


def client_update(request,id):
    photo = request.FILES['p']
    mylocation = os.path.join(settings.MEDIA_ROOT, 'client')
    obj = FileSystemStorage(location=mylocation)
    obj.save(photo.name, photo)

    data = {
                'photo' : photo.name,
                'client_name'        : request.POST['client_name'],
                'username'        : request.POST['username'],
                'email'       : request.POST['email'],
                'password'       : request.POST['password'],
                'dob'       : request.POST['dob'],
                'age' : 20,
                'gender'       : request.POST['gender'],
                'address'      : request.POST['address'],
                'contact' : request.POST['contact'],
                'city_id'     : request.POST['city'],
                'state_id'         : request.POST['state'],
                'zipcode'     : request.POST['zipcode'],
                
           }
    Client.objects.update_or_create(pk=id, defaults=data)
    return redirect('/staff/view_client')


def lawyer_update(request,id):
    photo = request.FILES['photo']
    mylocation = os.path.join(settings.MEDIA_ROOT, 'client')
    obj = FileSystemStorage(location=mylocation)
    obj.save(photo.name, photo)

    data = {
                'photo' : photo.name,
                'lawyer_name'        : request.POST['lawyer_name'],
                'username'        : request.POST['username'],
                'email'       : request.POST['email'],
                'password'       : request.POST['password'],
                'dob'       : request.POST['dob'],
                'age' : 20,
                'gender'       : request.POST['gender'],
                'qualification'       : request.POST['qualification'],
                'experience'       : request.POST['experience'],
                'registration_date'       : request.POST['registration_date'],
                'address'      : request.POST['address'],
                'contact' : request.POST['contact'],
                'city_id'     : request.POST['city'],
                'state_id'         : request.POST['state'],
                'zipcode'     : request.POST['zipcode'],
                
           }
    Lawyer.objects.update_or_create(pk=id, defaults=data)
    return redirect('/staff/view_member')


def case_store(request):
    title    = request.POST['title']
    description = request.POST['description']
    police_station = request.POST['police_station']
    case_type = request.POST['case_type']
    case_reg_date = request.POST['case_reg_date']
    court = request.POST['court']
    judge = request.POST['judge']
    status = request.POST['status']
    city = request.POST['city']
    state = request.POST['state']
    client = request.POST['client']
    lawyer = request.POST['lawyer']
    fir_copy = request.FILES['fir_copy']
    mylocation = os.path.join(settings.MEDIA_ROOT, 'client')
    obj = FileSystemStorage(location=mylocation)
    obj.save(fir_copy.name, fir_copy)

    Cases.objects.create(fir_copy = fir_copy.name, title = title, description = description, police_station = police_station, case_type = case_type, case_reg_date = case_reg_date, court = court, judge = judge, status = status, client_id = client, lawyer_id = lawyer, city_id = city, state_id = state)
    return redirect('/staff/add_case')


def case_update(request,id):
    fir_copy = request.FILES['fir_copy']
    mylocation = os.path.join(settings.MEDIA_ROOT, 'client')
    obj = FileSystemStorage(location=mylocation)
    obj.save(fir_copy.name, fir_copy)

    data = {
                'title'        : request.POST['title'],
                'description'       : request.POST['description'],
                'police_station'      : request.POST['police_station'],
                'case_type' : request.POST['case_type'],
                'case_reg_date'     : request.POST['case_reg_date'],
                'court'            : request.POST['court'],
                'judge'     : request.POST['judge'],
                'status'     : request.POST['status'],
                'city_id'     : request.POST['city'],
                'state_id'     : request.POST['state'],
                'client_id'     : request.POST['client'],
                'lawyer_id'     : request.POST['lawyer'],
                'fir_copy'     : fir_copy.name,
           }
    Cases.objects.update_or_create(pk=id, defaults=data)
    return redirect('/staff/view_cases')


def doc_store(request):
    title    = request.POST['title']
    description = request.POST['description']
    client = request.POST['client']
    cases = request.POST['cases']
    document = request.FILES['document']
    mylocation = os.path.join(settings.MEDIA_ROOT, 'document')
    obj = FileSystemStorage(location=mylocation)
    obj.save(document.name, document)

    Documents.objects.create(document = document.name, title = title, description = description, client_id = client, cases_id = cases)
    return redirect('/staff/view_cases')


def date_store(request):
    remarks    = request.POST['remarks']
    description = request.POST['description']
    cases = request.POST['cases']
    next_hearing_date = request.POST['date']
    status = "Pending"

    Schedule.objects.create(next_hearing_date = next_hearing_date, remarks = remarks, description = description, status = status, cases_id = cases)
    return redirect('/staff/view_cases')


def doc_update(request,id):
    document = request.FILES['document']
    mylocation = os.path.join(settings.MEDIA_ROOT, 'client')
    obj = FileSystemStorage(location=mylocation)
    obj.save(document.name, document)

    data = {
                'title'        : request.POST['title'],
                'description'       : request.POST['description'],
                'client_id'     : request.POST['client'],
                'cases_id'     : request.POST['cases'],
                'document'     : document.name,
           }
    Documents.objects.update_or_create(pk=id, defaults=data)
    return redirect('/staff/view_doc')


def view(request):
    pass


def client_delete(request,id):
    result = Client.objects.get(pk=id)
    result.delete()
    return redirect('/staff/view_client')


def lawyer_delete(request,id):
    result = Lawyer.objects.get(pk=id)
    result.delete()
    return redirect('/staff/view_member')


def case_delete(request,id):
    result = Cases.objects.get(pk=id)
    result.delete()
    return redirect('/staff/view_cases')


def doc_delete(request,id):
    result = Documents.objects.get(pk=id)
    result.delete()
    return redirect('/staff/view_doc')


def client_edit(request,id):
    result  = Client.objects.get(pk=id)
    city = City.objects.all()
    state = State.objects.all()
    context = {'result':result,'city':city,'state':state}
    return render(request, 'staff/update_client.html',context)


def doc_edit(request,id):
    result  = Documents.objects.get(pk=id)
    client = Client.objects.all()
    cases = Cases.objects.all()
    context = {'result':result,'client':client,'cases':cases}
    return render(request, 'staff/update_doc.html',context)


def lawyer_edit(request,id):
    result  = Lawyer.objects.get(pk=id)
    city = City.objects.all()
    state = State.objects.all()
    context = {'result':result,'city':city,'state':state}
    return render(request, 'staff/update_member.html',context)


def case_edit(request,id):
    result  = Cases.objects.get(pk=id)
    lawyer = Lawyer.objects.all()
    client = Client.objects.all()
    city = City.objects.all()
    state = State.objects.all()
    context = {'result':result,'city':city,'state':state,'lawyer':lawyer,'client':client}
    return render(request, 'staff/update_case.html',context)













# connector

    # try:
    #     connection = mysql.connector.connect(host='localhost',
    #                                          database='lawyeroffice',
    #                                          user='root',
    #                                          password='')

    #     sql_select_Query = "select * from client where id=3"
    #     cursor = connection.cursor()
    #     cursor.execute(sql_select_Query)
    #     # get all records
    #     records = cursor.fetchall()
    #     print("Total number of rows in table: ", cursor.rowcount)

    #     # print("\nPrinting each row")
    #     for row in records:
    #         print("Id = ", row[0], )
    #         print("Name = ", row[1])
    #         # print("Price  = ", row[2])
    #         # print("Purchase date  = ", row[3], "\n")

    # except mysql.connector.Error as e:
    #     print("Error reading data from MySQL table", e)
    # finally:
    #     if connection.is_connected():
    #         connection.close()
    #         cursor.close()
    #         print("MySQL connection is closed")