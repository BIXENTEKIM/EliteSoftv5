import math
import os
from io import BytesIO
from math import nan
from urllib.parse import urlsplit, urlparse
import pyodbc as po
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import pandas as pd

# Create your views here.
from django.views.decorators.cache import cache_control
from rest_framework import status

from setups.system.organisation.forms import OrganisationForm
from setups.system.organisation.models import  Organisation
from students.models import Select2Data
from students.serializers import Select2Serializer
from django.conf import Settings, settings


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def organisation(request):
    return render(request,'setups/system/organisation.html')

def addOrganisation(request):


    organisation = OrganisationForm(request.POST,request.FILES)
    # if request.method == 'POST':
    #     if 'parent_photo' in request.FILES:
    #         image = request.FILES.get('parent_photo')
    #         parent.parent_photo = image

    # print(organisation)
    organisation.save()
    return JsonResponse({'success': 'Organisation Saved Successfully'})


def editOrganisation(request,id):
    organisation = Organisation.objects.get(pk=id)
    response_data = {}

    response_data['org_code'] = organisation.org_code
    response_data['Org_Name'] = organisation.Org_Name
    response_data['Org_Physical_Address'] = organisation.Org_Physical_Address
    response_data['Org_Tel_No'] = organisation.Org_Tel_No
    response_data['Org_Email'] = organisation.Org_Email
    response_data['Org_Website'] = organisation.Org_Website
    response_data['Org_Tag_Line'] = organisation.Org_Tag_Line
    response_data['Org_Poastal_Address'] = organisation.Org_Poastal_Address
    response_data['Org_Cell_No'] = organisation.Org_Cell_No
    response_data['Org_Mission'] = organisation.Org_Mission
    # response_data['parentType'] = obj.parent_type
    response_data['Org_Vision'] = organisation.Org_Vision
    response_data['Org_Pin_No'] = organisation.Org_Pin_No
    response_data['Org_NHIF_Code'] = organisation.Org_NHIF_Code
    response_data['Org_NSSF_Code'] = organisation.Org_NSSF_Code
    # if not parent.parent_photo:
    #    print('File Absent')
    # else:
    #    print('File Present')
    # url = request.get_host() + parent.parent_photo.url
    # print(urlsplit(request.build_absolute_uri(None)).scheme)
    if organisation.Org_Logo:
        response_data['url'] = urlsplit(request.build_absolute_uri(None)).scheme + '://' + request.get_host() + organisation.Org_Logo.url
    if organisation.Org_Logo2:
        response_data['url2'] = urlsplit(request.build_absolute_uri(None)).scheme + '://' + request.get_host() + organisation.Org_Logo2.url
    return JsonResponse(response_data)

def testProc(request):
    server = r'DESKTOP-1FPK0DH\\MSSQLSERVER01,1433'
    database = 'TestSchool'
    username = 'admin'
    password = 'P4$$W0RD'
    try:
        # Connection string
        cnxn = po.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                          server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        cursor = cnxn.cursor()

        # Prepare the stored procedure execution script and parameter values
        storedProc = "Exec  [Mtb_GetCustomers] @SearchText = ?, @MaximumRowsToReturn = ?"
        params = ("kim", 10)

        # Execute Stored Procedure With Parameters
        cursor.execute(storedProc, params)

        # Iterate the cursor
        row = cursor.fetchone()
        while row:
            # Print the row
            print(str(row[0]) + " : " + str(row[1] or ''))
            row = cursor.fetchone()

        # Close the cursor and delete it
        cursor.close()
        del cursor

        # Close the database connection
        cnxn.close()
        return JsonResponse({'success': 'Organisation Saved Successfully'})
    except Exception as e:
        print("Error: %s" % e)
        return JsonResponse({'success': "Error: %s" % e})
def updateOrganisation(request,id):
    organisation = Organisation.objects.get(pk=id)

    form = OrganisationForm(request.POST,request.FILES, instance=organisation)

    form.save()
    return JsonResponse({'success': 'Organisation Updated Successfully'})


def deleteOrganisation(request,id):
    organisation = Organisation.objects.get(pk=id)
    organisation.delete()
    return JsonResponse({'success': 'Organisation Deleted Successfully'})


def getOrganisations(request):
    listsel = []
    organisation = Organisation.objects.raw(
        "SELECT org_code,Org_Name,Org_Physical_Address,Org_Tel_No,Org_Email,Org_Tag_Line, " +
        " Org_Poastal_Address,Org_Cell_No,Org_Mission,Org_Vision,Org_Pin_No," +
        "Org_NHIF_Code,Org_Website,Org_NSSF_Code from setups_Organisation")

    for obj in organisation:
        if obj.org_code not in listsel:
            response_data = {}

            response_data['org_code'] = obj.org_code
            response_data['Org_Name'] = obj.Org_Name
            response_data['Org_Website'] = obj.Org_Website
            response_data['Org_Physical_Address'] = obj.Org_Physical_Address
            response_data['Org_Tel_No'] = obj.Org_Tel_No
            response_data['Org_Email'] = obj.Org_Email
            response_data['Org_Tag_Line'] = obj.Org_Tag_Line
            response_data['Org_Poastal_Address'] = obj.Org_Poastal_Address
            response_data['Org_Cell_No'] = obj.Org_Cell_No
            response_data['Org_Mission'] = obj.Org_Mission
            response_data['Org_Vision'] = obj.Org_Vision
            response_data['Org_Pin_No'] = obj.Org_Pin_No
            response_data['Org_NHIF_Code'] = obj.Org_NHIF_Code
            response_data['Org_NSSF_Code'] = obj.Org_NSSF_Code
            listsel.append(response_data)

    return JsonResponse(listsel, safe=False)