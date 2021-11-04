from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from setups.academics.subjects.forms import SubjectForm
from setups.academics.subjects.models import SchoolSubjects
from setups.academics.departments.models import SchoolDepartments
from students.models import Select2Data
from students.serializers import Select2Serializer


def subjects(request):
    return render(request, 'setups/academics/subjects.html')


def createSubject(request):
    pos = ''
    if request.method == 'POST' and 'subject_include_for_pos' in request.POST:
        val = request.POST['subject_include_for_pos']
        pos = val
    else:
        pos = ''
    schoolSubject = SubjectForm(request.POST)
    # tr = request.POST['class_teacher']
    sd = schoolSubject.data['subject_department']
    # subject_include_for_pos = schoolSubject.data['subject_include_for_pos']

    if sd is not None and sd != '':
        department = SchoolDepartments.objects.get(pk=sd)
        schoolSubject.subject_department=department


    if pos is not None and pos == 'on':
        schoolSubject.subject_include_for_pos = True
    else:
        schoolSubject.subject_include_for_pos = False

    schoolSubject.save()
    return JsonResponse({'success': 'Subject Saved Successfully'})

def getSubjects(request):
    listsel = []
    subjects = SchoolSubjects.objects.raw(
        "select top 100 subject_code,subject_sht_code,subject_name,subject_order,subject_multiply_by,subject_include_for_pos,dp_name from  [dbo].[subjects_schoolsubjects] s, [dbo].[departments_schooldepartments]  d "+
        " where [dp_code] = [subject_department_id]")


    for obj in subjects:
        if obj.subject_code not in listsel:
           response_data = {}
           response_data['subjectCode'] = obj.subject_code
           response_data['subjectShtCode'] = obj.subject_sht_code

           if obj.dp_name is None:
               response_data['subjectDepartment'] = "Not Availed"
           else:
               response_data['subjectDepartment'] = obj.dp_name

           response_data['subjectName'] = obj.subject_name
           response_data['subjectOrder'] = obj.subject_order
           response_data['subjectMultiplyBy'] = obj.subject_multiply_by
           response_data['subjectIncludeForPos'] = obj.subject_include_for_pos

           listsel.append(response_data)


    return JsonResponse(listsel, safe=False)


def editSubject(request,id):
    subjects = SchoolSubjects.objects.get(pk=id)
    response_data = {}

    if subjects.subject_department is not None:
        subjectDepartment = SchoolDepartments.objects.get(pk=subjects.subject_department.pk)
        response_data['subjectDepartmentCode'] = subjectDepartment.dp_code
        response_data['subjectDepartmentName'] = subjectDepartment.dp_name
    response_data['subjectCode'] = subjects.subject_code
    response_data['subjectShtCode'] = subjects.subject_sht_code
    response_data['subjectName'] = subjects.subject_name
    response_data['subjectOrder'] = subjects.subject_order
    response_data['subjectMultiplyBy'] = subjects.subject_multiply_by
    response_data['subjectIncludeForPos'] = subjects.subject_include_for_pos
    return JsonResponse(response_data)


def updateSubject(request,id):
    subjects = SchoolSubjects.objects.get(pk=id)
    form = SubjectForm(request.POST, instance=subjects)
    form.save()
    return JsonResponse({'success': 'Subject Updated Successfully'})


def deleteSubject(request,id):
    subjects = SchoolSubjects.objects.get(pk=id)
    subjects.delete()
    return JsonResponse({'success': 'Subject Deleted Successfully'})


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