from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from setups.academics.mastersetups.forms import MasterSetupsForm
from setups.academics.mastersetups.models import MasterSetups
from students.models import Select2Data
from students.serializers import Select2Serializer


def mastersetups(request):
    return render(request, 'setups/academics/mastersetups.html')


def createMasterSetups(request):
    mastersetups = MasterSetupsForm(request.POST)
    # tr = request.POST['class_teacher']
    mastersetups.save()
    return JsonResponse({'success': 'MasterSetups Saved Successfully'})

def getMasterSetups(request):
    listsel = []
    mastersetups = MasterSetups.objects.raw(
        "SELECT DISTINCT v.ms_code,v.ms_desc, v.ms_type   FROM Setups_MasterSetups v")


    for obj in mastersetups:
        if obj.ms_code not in listsel:
           response_data = {}
           response_data['ms_code'] = obj.ms_code


           response_data['ms_desc'] = obj.ms_desc
           response_data['ms_type'] = obj.ms_type

           listsel.append(response_data)


    return JsonResponse(listsel, safe=False)


def editMasterSetups(request,id):
    dorms = MasterSetups.objects.get(pk=id)
    response_data = {}
    response_data['ms_code'] = dorms.ms_code
    response_data['ms_desc'] = dorms.ms_desc
    response_data['ms_type'] = dorms.ms_type
    return JsonResponse(response_data)


def updateMasterSetups(request,id):
    # print('Dorm id is===' + id)
    mastersetups = MasterSetups.objects.get(pk=id)
    form = MasterSetupsForm(request.POST, instance=mastersetups)
    form.save()
    return JsonResponse({'success': 'Setups Updated Successfully'})


def deleteMasterSetups(request,id):
    mastersetups = MasterSetups.objects.get(pk=id)
    mastersetups.delete()
    return JsonResponse({'success': 'Setups Deleted Successfully'})

#
# def searchDorm(request):
#     if request.method == 'GET' and 'query' in request.GET:
#         query = request.GET['query']
#         query = '%' + query + '%'
#     else:
#         query = '%' + '' + '%'
#
#     listsel = []
#     dorms = SchoolDorms.objects.raw(
#         "SELECT top 5 dorm_code,dorm_name FROM dorms_schooldorms v WHERE v.dorm_name like %s or v.dorm_name like %s",
#         tuple([query, query]))
#
#     for obj in dorms:
#         select2 = Select2Data()
#         select2.id = str(obj.dorm_code)
#         select2.text = obj.dorm_name
#         serializer = Select2Serializer(select2)
#
#         listsel.append(serializer.data)
#
#     return JsonResponse({'results': listsel})

