from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from setups.academics.gradesgrid.forms import GradesGridForm
from setups.academics.gradesgrid.models import GradesGrid
from setups.academics.departments.models import SchoolDepartments
from students.models import Select2Data
from students.serializers import Select2Serializer


def gradesgrid(request):
    return render(request, 'setups/academics/gradesgrid.html')


def createGradesgrid(request):

    gradesgrid = GradesGridForm(request.POST)
    sd = gradesgrid.data['grades_department']

    if sd is not None and sd != '':
        department = SchoolDepartments.objects.get(pk=sd)
        gradesgrid.grades_department = department
        print(department)
    gradesgrid.save()
    return JsonResponse({'success': 'Grades Saved Successfully'})

def getGradesgrids(request):
    listsel = []
    gradesgrid = GradesGrid.objects.raw(
        "select grades_code,grades_val1,grades_val2,grades_grade,grades_remarks,grades_option,dp_name "+
        "from gradesgrid_gradesgrid g, departments_schooldepartments d "+
        "where g.grades_department_id= d.dp_code")


    for obj in gradesgrid:
        if obj.grades_code not in listsel:
           response_data = {}
           response_data['grades_code'] = obj.grades_code
           response_data['grades_val1'] = obj.grades_val1

           if obj.dp_name is None:
               response_data['gradesgridDepartment'] = "Not Availed"
           else:
               response_data['gradesgridDepartment'] = obj.dp_name

           response_data['grades_val2'] = obj.grades_val2
           response_data['grades_grade'] = obj.grades_grade
           response_data['grades_remarks'] = obj.grades_remarks
           response_data['grades_option'] = obj.grades_option

           listsel.append(response_data)


    return JsonResponse(listsel, safe=False)


def editGradesgrid(request,id):
    gradesgrid = GradesGrid.objects.get(pk=id)
    response_data = {}

    if gradesgrid.grades_department is not None:
        gradesgridDepartment = SchoolDepartments.objects.get(pk=gradesgrid.grades_department.pk)
        response_data['gradesgridDepartmentCode'] = gradesgridDepartment.dp_code
        response_data['gradesgridDepartmentName'] = gradesgridDepartment.dp_name
    response_data['grades_code'] = gradesgrid.grades_code
    response_data['grades_val1'] = gradesgrid.grades_val1
    response_data['grades_val2'] = gradesgrid.grades_val2
    response_data['grades_grade'] = gradesgrid.grades_grade
    response_data['grades_remarks'] = gradesgrid.grades_remarks
    response_data['grades_option'] = gradesgrid.grades_option
    return JsonResponse(response_data)


def updateGradesgrid(request,id):
    gradesgrid = GradesGrid.objects.get(pk=id)
    form = GradesGridForm(request.POST, instance=gradesgrid)
    form.save()
    return JsonResponse({'success': 'Grades Grid Updated Successfully'})


def deleteGradesgrid(request,id):
    gradesgrid = GradesGrid.objects.get(pk=id)
    gradesgrid.delete()
    return JsonResponse({'success': 'Grades Deleted Successfully'})


def searchDepartment(request):
    if request.method == 'GET' and 'query' in request.GET:
        query = request.GET['query']
        query = '%' + query + '%'
    else:
        query = '%' + '' + '%'

    listsel = []
    departments = SchoolDepartments.objects.raw(
        "SELECT top 5 dp_code,dp_name FROM departments_schooldepartments WHERE dp_name like %s or dp_name like %s",
        # "SELECT top 5 dp_code,dp_name FROM departments_schooldepartments ",
        tuple([query, query]))
    print('Department is *********** ' )
    for obj in departments:
        print ('Department is  ' + obj.dp_name)
        select2 = Select2Data()
        select2.id = str(obj.dp_code)
        select2.text = obj.dp_name
        serializer = Select2Serializer(select2)

        listsel.append(serializer.data)

    return JsonResponse({'results': listsel})

#
# def searchclasses(request):
#     if request.method == 'GET' and 'query' in request.GET:
#         query = request.GET['query']
#         query = '%' + query + '%'
#     else:
#         query = '%' + '' + '%'
#
#     listsel = []
#     classes = SchoolClasses.objects.raw(
#         "SELECT top 5 class_code,class_name FROM classes_schoolclasses WHERE classes_schoolclasses.class_name like %s or classes_schoolclasses.form like %s",
#         tuple([query, query]))
#
#     for obj in classes:
#         select2 = Select2Data()
#         select2.id = str(obj.class_code)
#         select2.text = obj.class_name
#         serializer = Select2Serializer(select2)
#
#         listsel.append(serializer.data)
#
#     return JsonResponse({'results': listsel})