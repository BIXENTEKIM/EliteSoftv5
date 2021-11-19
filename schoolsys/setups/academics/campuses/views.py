from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from setups.academics.campuses.forms import CampusForm
from setups.academics.campuses.models import  Campuses
from localities.models import Counties
from students.models import Select2Data
from students.serializers import Select2Serializer


def campuses(request):
    return render(request, 'setups/academics/campuses.html')


def createCampus(request):

    schoolCampus = CampusForm(request.POST)
    # tr = request.POST['class_teacher']
    sd = schoolCampus.data['campus_county']

    if sd is not None and sd != '':
        county = Counties.objects.get(pk=sd)
        schoolCampus.campus_county=county
    if schoolCampus.is_valid():
        schoolCampus.save()
        return JsonResponse({'success': 'Campus Saved Successfully'})
    else:
        print(schoolCampus.errors)
        return JsonResponse({'success': 'Failed '})


def getCampuses(request):
    listsel = []
    campuses =  Campuses.objects.raw(
        "select campus_code,campus_name,campus_location,campus_incharge, campus_incharge_contacts,"+
        "county_name from campuses_campuses sc ,localities_counties c where sc.campus_county_id= c.county_id")

    for obj in campuses:
        if obj.campus_code not in listsel:
           response_data = {}
           response_data['campus_code'] = obj.campus_code
           response_data['campus_name'] = obj.campus_name

           if obj.county_name is None:
               response_data['campusCounty'] = "Not Availed"
           else:
               response_data['campusCounty'] = obj.county_name

           response_data['campus_location'] = obj.campus_location
           response_data['campus_incharge'] = obj.campus_incharge
           response_data['campus_incharge_contacts'] = obj.campus_incharge_contacts

           listsel.append(response_data)


    return JsonResponse(listsel, safe=False)


def editCampus(request,id):
    campuses = Campuses.objects.get(pk=id)
    response_data = {}

    if campuses.campus_county is not None:
        campusCounty = Counties.objects.get(pk=campuses.campus_county.pk)
        response_data['campusCountyCode'] = campusCounty.county_id
        response_data['campusCountyName'] = campusCounty.county_name
    response_data['campus_code'] = campuses.campus_code
    response_data['campus_name'] = campuses.campus_name
    response_data['campus_location'] = campuses.campus_location
    response_data['campus_incharge'] = campuses.campus_incharge
    response_data['campus_incharge_contacts'] = campuses.campus_incharge_contacts
    return JsonResponse(response_data)


def updateCampus(request,id):
    campuses =  Campuses.objects.get(pk=id)
    form = CampusForm(request.POST, instance=campuses)
    form.save()
    return JsonResponse({'success': 'Campus Updated Successfully'})


def deleteCampus(request,id):
    campuses =  Campuses.objects.get(pk=id)
    campuses.delete()
    return JsonResponse({'success': 'Campus Deleted Successfully'})


def searchCounty(request):
    if request.method == 'GET' and 'query' in request.GET:
        query = request.GET['query']
        query = '%' + query + '%'
    else:
        query = '%' + '' + '%'

    listsel = []
    counties = Counties.objects.raw(
        "SELECT top 5 county_id,county_name FROM localities_counties WHERE county_name like %s or county_name like %s",
        tuple([query, query]))
    for obj in counties:
        print ('County is  ' + obj.county_name)
        select2 = Select2Data()
        select2.id = str(obj.county_id)
        select2.text = obj.county_name
        serializer = Select2Serializer(select2)

        listsel.append(serializer.data)

    return JsonResponse({'results': listsel})
