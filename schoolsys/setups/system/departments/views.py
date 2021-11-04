from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from setups.academics.departments.forms import DepartmentForm
from setups.academics.departments.models import SchoolDepartments
from students.models import Select2Data
from students.serializers import Select2Serializer


def departments(request):
    return render(request, 'setups/academics/departments.html')


def createDepartment(request):
    schoolDepartment = DepartmentForm(request.POST)
    # tr = request.POST['class_teacher']
    schoolDepartment.save()
    return JsonResponse({'success': 'Department Saved Successfully'})

def getDepartments(request):
    listsel = []
    departments = SchoolDepartments.objects.raw(
        "SELECT DISTINCT v.dp_code,v.dp_sht_name, v.dp_name,v.dp_sequence  FROM   departments_schooldepartments  v")


    for obj in departments:
        if obj.dp_code not in listsel:
           response_data = {}
           response_data['dpCode'] = obj.dp_code
           response_data['dpShtName'] = obj.dp_sht_name
           response_data['dpName'] = obj.dp_name
           response_data['dpSequence'] = obj.dp_sequence

           listsel.append(response_data)


    return JsonResponse(listsel, safe=False)


def editDepartment(request,id):
    departments = SchoolDepartments.objects.get(pk=id)
    response_data = {}
    response_data['dpCode'] = departments.dp_code
    response_data['dpShtName'] = departments.dp_sht_name
    response_data['dpName'] = departments.dp_name
    response_data['dpSequence'] = departments.dp_sequence
    return JsonResponse(response_data)


def updateDepartment(request,id):
    departments = SchoolDepartments.objects.get(pk=id)
    form = DepartmentForm(request.POST, instance=departments)
    form.save()
    return JsonResponse({'success': 'Department Updated Successfully'})


def deleteDepartment(request,id):
    departments = SchoolDepartments.objects.get(pk=id)
    departments.delete()
    return JsonResponse({'success': 'Department Deleted Successfully'})


def searchDepartment(request):
    if request.method == 'GET' and 'query' in request.GET:
        query = request.GET['query']
        query = '%' + query + '%'
    else:
        query = '%' + '' + '%'

    listsel = []
    departments = SchoolDepartments.objects.raw(
        "SELECT top 5 dp_code,dp_name FROM departments_schooldepartments v WHERE v.dp_name like %s or v.dp_name like %s",
        tuple([query, query]))

    for obj in departments:
        select2 = Select2Data()
        select2.id = str(obj.dp_code)
        select2.text = obj.dp_name
        serializer = Select2Serializer(select2)

        listsel.append(serializer.data)

    return JsonResponse({'results': listsel})

