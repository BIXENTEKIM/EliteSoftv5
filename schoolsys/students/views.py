import json

from django.core import serializers
from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from students.forms import StudentForm, CountriesForm, CountiesForm
from students.serializers import StudentSerializer, Select2Serializer
from .models import StudentDef, Select2Data, Countries, Counties
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required

# Create your views here.
def home(request):
    return render(request,'home/home.html')
def add(request):
    # firstName = request.POST['firstName']
    # lastName = request.POST['lastName']
    # age = int(request.POST['age'])
    # height = int(request.POST['height'])
    # country = request.POST['country']
    # county = request.POST['county']
    # town = request.POST['town']
    # phone = request.POST['phone']
    # website = request.POST['website']
    # student = StudentDef()
    # student.age = age
    # student.firstName = firstName
    # student.lastName = lastName
    # student.height = height
    # student.country = country
    # student.county = county
    # student.town = town
    # student.phone = phone
    # student.website = website
    # student.save()
    student = StudentForm(request.POST)
    country = Countries.objects.get(pk=student.data['stud_country'])
    county  = Counties.objects.get(pk=student.data['stud_county'])
    student.stud_country=country
    student.stud_county=county
    student.save()
    return JsonResponse({'success': 'Student Saved Successfully'})

def getStudents(request):
    # students = json.loads(serializers.serialize('json', StudentDef.objects.all()))
    # return JsonResponse(students, safe=False)
    listsel = []
    students = StudentDef.objects.raw(
        "SELECT stdCode,concat(firstName,' ',lastName)name,phone,website,age,town,country_name,county_name FROM students_studentdef,students_countries,students_counties" +
        " where stud_country_id=country_id"+
        "  and  stud_county_id=county_id")

    for obj in students:
        response_data = {}
        response_data['stdCode'] = obj.stdCode
        response_data['country_name'] = obj.country_name
        response_data['county_name'] = obj.county_name
        response_data['name'] = obj.name
        response_data['town'] = obj.town
        response_data['phone'] = obj.phone
        response_data['website'] = obj.website
        response_data['age'] = obj.age


        listsel.append(response_data)

    return JsonResponse(listsel, safe=False)

def editStudent(request,id):
    print('This is the Id: '+str(id))
    student = StudentDef.objects.get(pk=id)
    country=Countries.objects.get(pk=student.stud_country.pk)
    county = Counties.objects.get(pk=student.stud_county.pk)
    response_data = {}
    response_data['stdCode'] = student.stdCode
    response_data['country_name'] = country.country_name
    response_data['country_id'] = country.country_id
    response_data['county_name'] = county.county_name
    response_data['county_id'] = country.country_id
    response_data['firstName'] = student.firstName
    response_data['lastName'] = student.lastName
    response_data['town'] = student.town
    response_data['phone'] = student.phone
    response_data['website'] = student.website
    response_data['age'] = student.age
    response_data['height'] = student.height
    return JsonResponse(response_data)

def updateStudent(request,id):

    student = StudentDef.objects.get(pk=id)
    form = StudentForm(request.POST,instance=student)
    form.save()
    return JsonResponse({'success': 'Student Updated Successfully'})

def deleteStudent(request,id):

    student = StudentDef.objects.get(pk=id)
    student.delete()
    return JsonResponse({'success': 'Student Deleted Successfully'})


def searchStudents(request):
    if request.method == 'GET' and 'query' in request.GET:
        query=request.GET['query']
        query='%'+query+'%'
    else:
        query = '%' + '' + '%'

    listsel = []
    students = StudentDef.objects.raw("SELECT  stdCode,firstName,lastName FROM students_studentdef WHERE firstName like %s or lastName like %s",tuple([query,query]))

    for obj in students:
        text = obj.firstName + ' ' + obj.lastName
        select2 = Select2Data()
        select2.id = str(obj.stdCode)
        select2.text = text
        serializer = Select2Serializer(select2)

        listsel.append(serializer.data)


    return JsonResponse({'results':listsel})


def country(request):
    return render(request,'countries.html')


def addcountry(request):
    country = CountriesForm(request.POST)
    country.save()
    return JsonResponse({'success': 'Country Saved Successfully'})

def getcountry(request):
    countries = json.loads(serializers.serialize('json', Countries.objects.all()))
    return JsonResponse(countries, safe=False)

def addcounty(request):
    county = CountiesForm(request.POST)
    print("Name: "+county.data['county_name']+"Code: "+county.data['county_code']+"Country: "+county.data['county_country'])
    country= Countries.objects.get(pk=county.data['county_country'])
    county.county_country = country
    county.save()


    return JsonResponse({'success': 'County Saved Successfully'})


def getcounty(request):
    # counties = json.loads(serializers.serialize('json', Counties.objects.all()))
    # return JsonResponse(counties, safe=False)
    listsel = []
    counties = Counties.objects.raw(
        "SELECT  county_id,county_name,county_code,country_name FROM students_counties,students_countries"+
        " where county_country_id=country_id")

    for obj in counties:
        response_data = {}
        response_data['county_id'] = obj.county_id
        response_data['county_name'] = obj.county_name
        response_data['county_code'] = obj.county_code
        response_data['country_name'] = obj.country_name

        listsel.append(response_data)

    return JsonResponse(listsel,safe=False)

def searchcountries(request):
    if request.method == 'GET' and 'query' in request.GET:
        query = request.GET['query']
        query = '%' + query + '%'
    else:
        query = '%' + '' + '%'

    listsel = []
    students = Countries.objects.raw(
        "SELECT  country_id,country_name FROM students_countries WHERE country_name like %s or country_code like %s",
        tuple([query, query]))

    for obj in students:
        text = obj.country_name
        select2 = Select2Data()
        select2.id = str(obj.country_id)
        select2.text = text
        serializer = Select2Serializer(select2)

        listsel.append(serializer.data)

    return JsonResponse({'results': listsel})


def county(request):
    return render(request,'counties.html')


def searchcounties(request,id):
    print('Id for search is :'+str(id))
    if request.method == 'GET' and 'query' in request.GET:
        query = request.GET['query']
        query = '%' + query + '%'
    else:
        query = '%' + '' + '%'

    listsel = []
    counties = Counties.objects.raw(
        "SELECT  county_id,county_name FROM students_counties WHERE county_country_id = %s and" +
        " (county_name like %s or county_code like %s)",
        [id, query,query])

    for obj in counties:
        text = obj.county_name
        select2 = Select2Data()
        select2.id = str(obj.county_id)
        select2.text = text
        serializer = Select2Serializer(select2)

        listsel.append(serializer.data)

    return JsonResponse({'results': listsel})