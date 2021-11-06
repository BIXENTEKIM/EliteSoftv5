from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from setups.system.templates.forms import TemplatesForm
from setups.system.templates.models import Templates
from students.models import Select2Data
from students.serializers import Select2Serializer


def templates(request):
    return render(request, 'setups/system/templates.html')


def createTemplate(request):
    templates = TemplatesForm(request.POST)
    # tr = request.POST['class_teacher']
    templates.save()
    return JsonResponse({'success': 'Template Saved Successfully'})

def getTemplates(request):
    listsel = []
    templates = Templates.objects.raw(
        "Select temp_code,temp_module,temp_name,temp_desc from setups_Templates")


    for obj in templates:
        if obj.temp_code not in listsel:
           response_data = {}
           response_data['temp_code'] = obj.temp_code
           response_data['temp_module'] = obj.temp_module
           response_data['temp_name'] = obj.temp_name
           response_data['temp_desc'] = obj.temp_desc

           listsel.append(response_data)


    return JsonResponse(listsel, safe=False)


def editTemplate(request,id):
    templates = Templates.objects.get(pk=id)
    response_data = {}
    response_data['temp_code'] = templates.temp_code
    response_data['temp_module'] = templates.temp_module
    response_data['temp_name'] = templates.temp_name
    response_data['temp_desc'] =templates.temp_desc
    return JsonResponse(response_data)


def updateTemplate(request,id):
    # print('Dorm id is===' + id)
    templates = Templates.objects.get(pk=id)
    form = TemplatesForm(request.POST, instance=templates)
    form.save()
    return JsonResponse({'success': 'Template Updated Successfully'})


def deleteTemplate(request,id):
    templates = Templates.objects.get(pk=id)
    templates.delete()
    return JsonResponse({'success': 'Template Deleted Successfully'})

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

