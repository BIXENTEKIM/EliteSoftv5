from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from setups.academics.hmcomments.forms import HMCommentsForm
from setups.academics.hmcomments.models import HMComments
from students.models import Select2Data
from students.serializers import Select2Serializer


def hmcomments(request):
    return render(request, 'setups/academics/hmcomments.html')


def createHMComments(request):

    hmcomments = HMCommentsForm(request.POST)

    hmcomments.save()
    return JsonResponse({'success': 'Comments Saved Successfully'})

def getHMComments(request):
    listsel = []
    hmcomments  = HMComments.objects.raw(
        "select hm_code,hm_val1,hm_val2,hm_grade,hm_remarks "+
        "from setups_hmcomments g ")


    for obj in hmcomments:
        if obj.hm_code not in listsel:
           response_data = {}
           response_data['hm_code'] = obj.hm_code
           response_data['hm_val1'] = obj.hm_val1
           response_data['hm_val2'] = obj.hm_val2
           response_data['hm_grade'] = obj.hm_grade
           response_data['hm_remarks'] = obj.hm_remarks

           listsel.append(response_data)


    return JsonResponse(listsel, safe=False)


def editHMComments(request,id):
    hmcomments = HMComments.objects.get(pk=id)
    response_data = {}
    response_data['hm_code'] = hmcomments.hm_code
    response_data['hm_val1'] = hmcomments.hm_val1
    response_data['hm_val2'] = hmcomments.hm_val2
    response_data['hm_grade'] = hmcomments.hm_grade
    response_data['hm_remarks'] = hmcomments.hm_remarks
    return JsonResponse(response_data)


def updateHMComments(request,id):
    hmcomments = HMComments.objects.get(pk=id)
    form = HMCommentsForm(request.POST, instance=hmcomments)
    form.save()
    return JsonResponse({'success': 'HM Comments Updated Successfully'})


def deleteHMComments(request,id):
    hmcomments = HMComments.objects.get(pk=id)
    hmcomments.delete()
    return JsonResponse({'success': 'Comments Deleted Successfully'})

