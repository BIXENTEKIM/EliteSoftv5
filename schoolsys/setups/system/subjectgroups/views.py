from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from setups.academics.subjectgroups.forms import SubjectGroupsForm
from setups.academics.subjectgroups.models import SubjectGroups
from setups.academics.subjects.models import SchoolSubjects
from students.models import Select2Data
from students.serializers import Select2Serializer


def subjectgroups(request):
    return render(request, 'setups/academics/subjectgroups.html')


def createSubjectGroup(request):
    pos = ''
    if request.method == 'POST' and 'sg_compulsory_f12' in request.POST:
        val = request.POST['sg_compulsory_f12']
        pos = val
    else:
        pos = ''

    pos2 = ''
    if request.method == 'POST' and 'sg_compulsory_school' in request.POST:
        val = request.POST['sg_compulsory_school']
        pos2 = val
    else:
        pos2 = ''

    subjectgroup = SubjectGroupsForm(request.POST)
    # tr = request.POST['class_teacher']
    sd = subjectgroup.data['subjectgroups_subject']

    if sd is not None and sd != '':
        subject = SchoolSubjects.objects.get(pk=sd)
        subjectgroup.subjectgroups_subject=subject


    if pos is not None and pos == 'on':
        subjectgroup.sg_compulsory_f12 = True
    else:
        subjectgroup.sg_compulsory_f12 = False

    if pos2 is not None and pos2 == 'on':
        subjectgroup.sg_compulsory_school = True
    else:
        subjectgroup.sg_compulsory_school = False

    subjectgroup.save()
    return JsonResponse({'success': 'Subject Group Saved Successfully'})

def getSubjectGroups(request):
    listsel = []
    subjectgroups = SubjectGroups.objects.raw(
        "select sg_code,sg_group,sg_compulsory_f12,sg_compulsory_school,subject_name " +
        " from setups_subjectgroups sg,subjects_schoolsubjects s " +
        " where subject_code=subjectgroups_subject_id")


    for obj in subjectgroups:
        if obj.sg_code not in listsel:
           response_data = {}
           response_data['sg_code'] = obj.sg_code
           response_data['sg_group'] = obj.sg_group

           if obj.subject_name is None:
               response_data['subjectgroupSubject'] = "Not Availed"
           else:
               response_data['subjectgroupSubject'] = obj.subject_name

           response_data['sg_compulsory_f12'] = obj.sg_compulsory_f12
           response_data['sg_compulsory_school'] = obj.sg_compulsory_school

           listsel.append(response_data)


    return JsonResponse(listsel, safe=False)


def editSubjectGroup(request,id):
    subjectgroups = SubjectGroups.objects.get(pk=id)
    response_data = {}

    if subjectgroups.subjectgroups_subject  is not None:
        subjectGroupSubject = SchoolSubjects.objects.get(pk=subjectgroups.subjectgroups_subject.pk)
        response_data['subjectGroupSubjectCode'] = subjectGroupSubject.subject_code
        response_data['subjectGroupSubjectName'] = subjectGroupSubject.subject_name
    response_data['sg_code'] = subjectgroups.sg_code
    response_data['sg_group'] = subjectgroups.sg_group
    response_data['sg_compulsory_f12'] = subjectgroups.sg_compulsory_f12
    response_data['sg_compulsory_school'] = subjectgroups.sg_compulsory_school
    return JsonResponse(response_data)


def updateSubjectGroup(request,id):
    subjectgroups = SubjectGroups.objects.get(pk=id)
    form = SubjectGroupsForm(request.POST, instance=subjectgroups)
    form.save()
    return JsonResponse({'success': 'Subject Group Updated Successfully'})


def deleteSubjectGroup(request,id):
    subjectgroups = SubjectGroups.objects.get(pk=id)
    subjectgroups.delete()
    return JsonResponse({'success': 'Subject Group Deleted Successfully'})


def searchSubject(request):
    if request.method == 'GET' and 'query' in request.GET:
        query = request.GET['query']
        query = '%' + query + '%'
    else:
        query = '%' + '' + '%'

    listsel = []
    subjects = SchoolSubjects.objects.raw(
        "SELECT top 5 subject_code,subject_name FROM subjects_schoolsubjects WHERE subject_name like %s or subject_name like %s",
        # "SELECT top 5 dp_code,dp_name FROM departments_schooldepartments ",
        tuple([query, query]))
    print('Department is *********** ' )
    for obj in subjects:
        print ('Department is  ' + obj.subject_name)
        select2 = Select2Data()
        select2.id = str(obj.subject_code)
        select2.text = obj.subject_name
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