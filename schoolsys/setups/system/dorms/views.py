from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from setups.academics.dorms.forms import DormForm
from setups.academics.dorms.models import SchoolDorms
from students.models import Select2Data
from students.serializers import Select2Serializer


def dorms(request):
    return render(request, 'setups/academics/dorms.html')


def createDorm(request):
    schoolDorm = DormForm(request.POST)
    # tr = request.POST['class_teacher']
    schoolDorm.save()
    return JsonResponse({'success': 'Dorm Saved Successfully'})

def getDorms(request):
    listsel = []
    dorms = SchoolDorms.objects.raw(
        "SELECT DISTINCT v.dorm_code,v.dorm_name, v.max_capacity,v.current_capacity  FROM dorms_schooldorms v")


    for obj in dorms:
        if obj.dorm_code not in listsel:
           response_data = {}
           response_data['dormCode'] = obj.dorm_code


           response_data['dormname'] = obj.dorm_name
           response_data['maxCapacity'] = obj.max_capacity
           response_data['currentCapacity'] = '0'

           listsel.append(response_data)


    return JsonResponse(listsel, safe=False)


def editDorm(request,id):
    dorms = SchoolDorms.objects.get(pk=id)
    response_data = {}
    response_data['dormCode'] = dorms.dorm_code
    response_data['dormname'] = dorms.dorm_name
    response_data['maxCapacity'] = dorms.max_capacity
    response_data['currentCapacity'] = '0'
    return JsonResponse(response_data)


def updateDorm(request,id):
    # print('Dorm id is===' + id)
    dorms = SchoolDorms.objects.get(pk=id)
    form = DormForm(request.POST, instance=dorms)
    form.save()
    return JsonResponse({'success': 'Dorm Updated Successfully'})


def deleteDorm(request,id):
    dorms = SchoolDorms.objects.get(pk=id)
    dorms.delete()
    return JsonResponse({'success': 'Dorm Deleted Successfully'})


def searchDorm(request):
    if request.method == 'GET' and 'query' in request.GET:
        query = request.GET['query']
        query = '%' + query + '%'
    else:
        query = '%' + '' + '%'

    listsel = []
    dorms = SchoolDorms.objects.raw(
        "SELECT top 5 dorm_code,dorm_name FROM dorms_schooldorms v WHERE v.dorm_name like %s or v.dorm_name like %s",
        tuple([query, query]))

    for obj in dorms:
        select2 = Select2Data()
        select2.id = str(obj.dorm_code)
        select2.text = obj.dorm_name
        serializer = Select2Serializer(select2)

        listsel.append(serializer.data)

    return JsonResponse({'results': listsel})

