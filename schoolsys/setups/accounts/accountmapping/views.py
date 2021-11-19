import pdb

from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

from django.http import JsonResponse
from django.shortcuts import render
import pyodbc as po
from datetime import datetime
# Create your views here.
from setups.accounts.accountmaster.forms import AccountMasterForm
from setups.accounts.accountmaster.models import AccountMaster
from setups.accounts.accountmapping.models import AccountMapping
from setups.accounts.accountmapping.forms import AccountMappingForm
from students.models import Select2Data
from students.serializers import Select2Serializer

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def accountmapping(request):
    return render(request, 'setups/accounts/accountmapping.html')

def createAccountmapping(request):

    accountmapping = AccountMappingForm(request.POST)

    print('88888888888')
    sd = accountmapping.data['acm_AccountMaster']
    if sd is not None and sd != '':
        accountmaster = AccountMaster.objects.get(pk=sd)
        accountmapping.acm_AccountMaster=accountmaster
        print('99999999')

    sd2 = accountmapping.data['acm_contra_AccountMaster']
    if sd2 is not None and sd2 != '':
        accountmaster2 = AccountMaster.objects.get(pk=sd2)
        accountmapping.acm_contra_AccountMaster = accountmaster2

    print('7777777')
    try:
        if accountmapping.is_valid():
            accountmapping.save()
            return JsonResponse({'success': 'Account Mapping Saved Successfully'})
        else:
            print(accountmapping.errors)
            return JsonResponse({'success': "Error saving account mapping"} )

    except Exception as e:
        return JsonResponse({'success': "Error: %s" % e})


def getAccountmapping(request):
    listsel = []
    accountmapping = AccountMapping.objects.raw(
        "select acm_code, acm_type ,am1.am_desc mainaccount ,am2.am_desc contraaccount, acm_desc  "+
        "from account_mapping am, account_master am1,account_master am2 "+
        "where   acm_AccountMaster_id  = am1.am_code "+
        "and  acm_contra_AccountMaster_id  =am2.am_code")


    for obj in accountmapping:
        if obj.acm_code not in listsel:
           response_data = {}
           response_data['acm_code'] = obj.acm_code
           response_data['acm_desc'] = obj.acm_desc
           response_data['acm_type'] = obj.acm_type

           if obj.mainaccount is None:
               response_data['acm_AccountMaster'] = "Not Availed"
           else:
               response_data['acm_AccountMaster'] = obj.mainaccount

           if obj.contraaccount is None:
               response_data['acm_contra_AccountMaster'] = "Not Availed"
           else:
               response_data['acm_contra_AccountMaster'] = obj.contraaccount

           listsel.append(response_data)


    return JsonResponse(listsel, safe=False)


def editAccountmapping(request,id):
    accountmapping = AccountMapping.objects.get(pk=id)
    response_data = {}

    if accountmapping.acm_AccountMaster  is not None:
        accountmaster1 = AccountMaster.objects.get(pk=accountmapping.acm_AccountMaster.pk)
        response_data['accountMasterCode'] = accountmaster1.am_code
        response_data['accountMasterName'] = accountmaster1.am_desc

    if accountmapping.acm_contra_AccountMaster is not None:
        accountmaster2 = AccountMaster.objects.get(pk=accountmapping.acm_contra_AccountMaster.pk)
        response_data['accountMasterCode2'] = accountmaster2.am_code
        response_data['accountMasterName2'] = accountmaster2.am_desc


    response_data['acm_code'] = accountmapping.acm_code
    response_data['acm_desc'] = accountmapping.acm_desc
    response_data['acm_type'] = accountmapping.acm_type

    return JsonResponse(response_data)


def updateAccountmapping(request,id):
    accountmapping = AccountMapping.objects.get(pk=id)
    form = AccountMappingForm(request.POST, instance=accountmapping)
    if form.is_valid():
        form.save()
        return JsonResponse({'success': 'Account Master Updated Successfully'})
    else:
        print(form.errors)
        return JsonResponse({'success': "Error saving account master"})


def deleteAccountmapping(request,id):
    accountmapping = AccountMapping.objects.get(pk=id)
    accountmapping.delete()
    return JsonResponse({'success': 'Account Mapping Deleted Successfully'})


def searchAccountMaster(request):
    if request.method == 'GET' and 'query' in request.GET:
        query = request.GET['query']
        query = '%' + query + '%'
    else:
        query = '%' + '' + '%'

    listsel = []
    accountmaster = AccountMaster.objects.raw(
        "select am_code,am_desc from account_master WHERE am_desc like %s or am_desc like %s",
        # "SELECT top 5 dp_code,dp_name FROM departments_schooldepartments ",
        tuple([query, query]))
    print('accountgroups is *********** ' )
    for obj in accountmaster:
        print ('Department is  ' + obj.am_desc)
        select2 = Select2Data()
        select2.id = str(obj.am_code)
        select2.text = obj.am_desc
        serializer = Select2Serializer(select2)

        listsel.append(serializer.data)

    return JsonResponse({'results': listsel})



def searchAccountMaster2(request):
    if request.method == 'GET' and 'query' in request.GET:
        query = request.GET['query']
        query = '%' + query + '%'
    else:
        query = '%' + '' + '%'

    listsel = []
    accountmaster = AccountMaster.objects.raw(
        "select am_code,am_desc from account_master WHERE am_desc like %s or am_desc like %s",
        # "SELECT top 5 dp_code,dp_name FROM departments_schooldepartments ",
        tuple([query, query]))
    print('accountgroups is *********** ' )
    for obj in accountmaster:
        print ('Department is  ' + obj.am_desc)
        select2 = Select2Data()
        select2.id = str(obj.am_code)
        select2.text = obj.am_desc
        serializer = Select2Serializer(select2)

        listsel.append(serializer.data)

    return JsonResponse({'results': listsel})
