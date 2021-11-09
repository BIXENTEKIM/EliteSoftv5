from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.cache import cache_control

from usertype.usertype.forms import UsertypeForm
from useradmin.users.models import UserType
from students.models import Select2Data
from students.serializers import Select2Serializer

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def usertype(request):
    return render(request, 'usertype/usertype.html')


def createUsertype(request):
    usertype = UsertypeForm(request.POST)
    usertype.save()
    return JsonResponse({'success': 'User Type Saved Successfully'})

def getUsertypes(request):
    listsel = []
    usertypes = UserType.objects.raw(
        "select type_code,type_name,type_desc from  [dbo].[users_usertype]")


    for obj in usertypes:
        if obj.type_code not in listsel:
           response_data = {}
           response_data['type_code'] = obj.type_code


           response_data['type_name'] = obj.type_name
           response_data['type_desc'] = obj.type_desc

           listsel.append(response_data)


    return JsonResponse(listsel, safe=False)


def editUsertype(request,id):
    usertypes = UserType.objects.get(pk=id)
    response_data = {}
    response_data['type_code'] = usertypes.type_code
    response_data['type_name'] = usertypes.type_name
    response_data['type_desc'] = usertypes.type_desc
    return JsonResponse(response_data)


def updateUsertype(request,id):
    usertypes = UserType.objects.get(pk=id)
    form = UsertypeForm(request.POST, instance=usertypes)
    form.save()
    return JsonResponse({'success': 'Usertype Updated Successfully'})


def deleteUsertype(request,id):
    usertypes = UserType.objects.get(pk=id)
    usertypes.delete()
    return JsonResponse({'success': 'User Type Deleted Successfully'})

