from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from setups.system.parameters.forms import ParametersForm
from setups.system.parameters.models import Parameters
from students.models import Select2Data
from students.serializers import Select2Serializer


def parameters(request):
    return render(request, 'setups/system/parameters.html')


def createParameter(request):
    parameter = ParametersForm(request.POST)
    # tr = request.POST['class_teacher']
    parameter.save()
    return JsonResponse({'success': 'Parameter Saved Successfully'})

def getParameters(request):
    listsel = []
    parameter = Parameters.objects.raw(
        "SELECT   v.param_code,v.param_name, v.param_value,v.param_desc  FROM Setups_Parameters v")


    for obj in parameter:
        if obj.param_code not in listsel:
           response_data = {}
           response_data['param_code'] = obj.param_code
           response_data['param_name'] = obj.param_name
           response_data['param_value'] = obj.param_value
           response_data['param_desc'] = obj.param_desc

           listsel.append(response_data)


    return JsonResponse(listsel, safe=False)


def editParameter(request,id):
    parameters = Parameters.objects.get(pk=id)
    response_data = {}
    response_data['param_code'] = parameters.param_code
    response_data['param_name'] = parameters.param_name
    response_data['param_value'] = parameters.param_value
    response_data['param_desc'] =parameters.param_desc
    return JsonResponse(response_data)


def updateParameter(request,id):
    # print('Dorm id is===' + id)
    parameters = Parameters.objects.get(pk=id)
    form = ParametersForm(request.POST, instance=parameters)
    form.save()
    return JsonResponse({'success': 'Paramater Updated Successfully'})


def deleteParameter(request,id):
    parameters = Parameters.objects.get(pk=id)
    parameters.delete()
    return JsonResponse({'success': 'Parameter Deleted Successfully'})

#
# def searchparameter(request):
#     if request.method == 'GET' and 'query' in request.GET:
#         query = request.GET['query']
#         query = '%' + query + '%'
#     else:
#         query = '%' + '' + '%'
#
#     listsel = []
#     dorms = Parameters.objects.raw(
#         "SELECT top 5 param_code,dorm_name FROM dorms_schooldorms v WHERE v.dorm_name like %s or v.dorm_name like %s",
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

