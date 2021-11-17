import pdb

from django.http import JsonResponse
from django.shortcuts import render
import pyodbc as po
from datetime import datetime
# Create your views here.
from setups.accounts.accountmaster.forms import AccountMasterForm
from setups.accounts.accountmaster.models import AccountMaster
from setups.accounts.accountmaster.models import AccountGroups
from setups.accounts.accountmaster.forms import AccountGroupsForm
from setups.accounts.accountmaster.models import AccountMain
from setups.accounts.accountmaster.forms import AccountMainForm
from students.models import Select2Data
from students.serializers import Select2Serializer


def accountmaster(request):
    return render(request, 'setups/accounts/accountmaster.html')

def generateAccountNo(numbertype):
    server = r'DESKTOP-1FPK0DH\\MSSQLSERVER01,1433'
    database = 'TestSchool'
    username = 'admin'
    password = 'P4$$W0RD'
    try:
        # Connection string
        cnxn = po.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                          server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password, autocommit=True)

        cursor = cnxn.cursor()
        # Prepare the stored procedure execution script and parameter values
        # storedProc = "Exec  account_number_sequences_proc 100"
        # storedProc = "Exec  account_number_sequences_proc @numbertype = ?"
        # params = (numbertype)
        # cursor.execute(storedProc,params)

        sql = """\
                DECLARE @out nvarchar(max);
                DECLARE @rv varchar(100);
                Exec  @rv = account_number_sequences_proc @numbertype = ?, @param_out = @out OUTPUT;
                SELECT @rv AS return_value;
                """
        params = (numbertype,)
        cursor.execute(sql, params)

        return_value = cursor.fetchval()
        cnxn.commit
        # rows = cursor.fetchall()
        # while rows:
        #     print(rows)
        #     if cursor.nextset():
        #         rows = cursor.fetchall()
        #         accountNo = rows[0]
        #     else:
        #         rows = None


        print("return_value NOOOOOO===="+str(return_value))
        # Iterate the cursor
        # row = cursor.fetchone()
        # print("row is====="+ str(row[0]))
        # while row:
        #     accountNo= row[0]
        #     row = cursor.fetchone()

        # Close the cursor and delete it

        cursor.close()
        del cursor

        # Close the database connection

        cnxn.close()
        return  return_value
    except Exception as e:
        print("Error: %s" % e)
        return JsonResponse({'success': "Error: %s" % e})

def createAccountmaster(request):
    pos = ''
    if request.method == 'POST' and 'am_cb' in request.POST:
        val = request.POST['am_cb']
        pos = val
    else:
        pos = ''

    pos2 = ''
    if request.method == 'POST' and 'am_bs' in request.POST:
        val = request.POST['am_bs']
        pos2 = val
    else:
        pos2 = ''

    pos3 = ''
    if request.method == 'POST' and 'am_pl' in request.POST:
        val = request.POST['am_pl']
        pos3 = val
    else:
        pos3 = ''

    pos4 = ''
    if request.method == 'POST' and 'am_pc' in request.POST:
        val = request.POST['am_pc']
        pos4 = val
    else:
        pos4 = ''

    accountmaster = AccountMasterForm(request.POST)


    # tr = request.POST['class_teacher']
    sd = accountmaster.data['am_AccountGroups']

    if sd is not None and sd != '':
        accountgroup = AccountGroups.objects.get(pk=sd)
        accountmaster.am_AccountGroups=accountgroup
        print(accountgroup)

    sd2 = accountmaster.data['am_AccountMain']
    print("sd2===" +str(sd2))
    if sd2 is not None and sd2 != '':
        accountmain = AccountMain.objects.get(pk=sd2)
        accountmaster.am_AccountMain = accountmain
        print("account main ======" +str(accountmain))

    if pos is not None and pos == 'on':
        accountmaster.am_cb = True
    else:
        accountmaster.am_cb = False

    if pos2 is not None and pos2 == 'on':
        accountmaster.am_bs = True
    else:
        accountmaster.am_bs = False

    if pos3 is not None and pos3 == 'on':
        accountmaster.am_pl = True
    else:
        accountmaster.am_pl = False

    if pos4 is not None and pos4 == 'on':
        accountmaster.am_pc = True
    else:
        accountmaster.am_pc = False

    amaccountgroups = AccountGroups.objects.get(pk=accountmaster.am_AccountGroups.pk)
    print("prefix is " + amaccountgroups.ag_prefix)

    try:
        if accountmaster.is_valid():
            inst=accountmaster.save()
            accmast = AccountMaster.objects.get(pk=inst.pk)
            accmast.am_created_by = 'KIM'
            accmast.am_created_on = datetime.today()
            v_accno = generateAccountNo(amaccountgroups.ag_prefix)
            print('generated account no is '+ str(v_accno))
            accmast.am_account_no=v_accno
            accmast.save()
            return JsonResponse({'success': 'Account Saved Successfully'})
        else:
            print(accountmaster.errors)
            return JsonResponse({'success': "Error saving account master"} )

    except Exception as e:
        return JsonResponse({'success': "Error: %s" % e})


def getAccountmaster(request):
    listsel = []
    accountmaster = AccountMaster.objects.raw(
        "select ag_desc,ama_desc,[am_code],[am_desc],[am_status] ,[am_account_no] ,"+
        "[am_cb],[am_bs],[am_pl],[am_pc],[am_order] "+
        "from account_master am,account_groups , account_main "+
        "where ag_code=am_AccountGroups_id "+
        "and am_AccountMain_id =ama_code")


    for obj in accountmaster:
        if obj.am_code not in listsel:
           response_data = {}
           response_data['am_code'] = obj.am_code
           response_data['am_desc'] = obj.am_desc
           response_data['am_status'] = obj.am_status
           response_data['am_account_no'] = obj.am_account_no
           response_data['am_order'] = obj.am_order

           if obj.ag_desc is None:
               response_data['am_AccountGroups'] = "Not Availed"
           else:
               response_data['am_AccountGroups'] = obj.ag_desc

           if obj.ama_desc is None:
               response_data['am_AccountMain'] = "Not Availed"
           else:
               response_data['am_AccountMain'] = obj.ama_desc

           response_data['am_cb'] = obj.am_cb
           response_data['am_pl'] = obj.am_pl
           response_data['am_pc'] = obj.am_pc
           response_data['am_bs'] = obj.am_bs

           listsel.append(response_data)


    return JsonResponse(listsel, safe=False)


def editAccountmaster(request,id):
    accountmaster = AccountMaster.objects.get(pk=id)
    response_data = {}

    if accountmaster.am_AccountGroups  is not None:
        amaccountgroups = AccountGroups.objects.get(pk=accountmaster.am_AccountGroups.pk)
        response_data['accountGroupCode'] = amaccountgroups.ag_code
        response_data['accountGroupName'] = amaccountgroups.ag_desc

    if accountmaster.am_AccountMain  is not None:
        amaaccountmain = AccountMain.objects.get(pk=accountmaster.am_AccountMain.pk)
        print ("ama is********" + str(amaaccountmain))
        response_data['accountMainCode'] = amaaccountmain.ama_code
        response_data['accountMainName'] = amaaccountmain.ama_desc


    response_data['am_code'] = accountmaster.am_code
    response_data['am_desc'] = accountmaster.am_desc
    response_data['am_status'] = accountmaster.am_status
   # // v_accno = generateAccountNo(amaccountgroups.ag_prefix)
    # //print("account is ==== "+v_accno)
    response_data['am_account_no'] =accountmaster.am_account_no
        # accountmaster.am_account_no

    response_data['am_order'] = accountmaster.am_order
    response_data['am_cb'] = accountmaster.am_cb
    response_data['am_pl'] = accountmaster.am_pl
    response_data['am_pc'] = accountmaster.am_pc
    response_data['am_bs'] = accountmaster.am_pc
    return JsonResponse(response_data)


def updateAccountmaster(request,id):
    accountmaster = AccountMaster.objects.get(pk=id)
    form = AccountMasterForm(request.POST, instance=accountmaster)
    if form.is_valid():
        form.save()
        return JsonResponse({'success': 'Account Master Updated Successfully'})
    else:
        print(form.errors)
        return JsonResponse({'success': "Error saving account master"})


def deleteAccountmaster(request,id):
    accountmaster = AccountMaster.objects.get(pk=id)
    accountmaster.delete()
    return JsonResponse({'success': 'Account Master Deleted Successfully'})


def searchAccountGroup(request):
    if request.method == 'GET' and 'query' in request.GET:
        query = request.GET['query']
        query = '%' + query + '%'
    else:
        query = '%' + '' + '%'

    listsel = []
    accountgroups = AccountGroups.objects.raw(
        "select ag_code,ag_desc from account_groups WHERE ag_desc like %s or ag_desc like %s",
        # "SELECT top 5 dp_code,dp_name FROM departments_schooldepartments ",
        tuple([query, query]))
    print('accountgroups is *********** ' )
    for obj in accountgroups:
        print ('Department is  ' + obj.ag_desc)
        select2 = Select2Data()
        select2.id = str(obj.ag_code)
        select2.text = obj.ag_desc
        serializer = Select2Serializer(select2)

        listsel.append(serializer.data)

    return JsonResponse({'results': listsel})


def searchAccountMain(request):
    if request.method == 'GET' and 'query' in request.GET:
        query = request.GET['query']
        query = '%' + query + '%'
    else:
        query = '%' + '' + '%'

    listsel = []
    accountmain = AccountMain.objects.raw(
        "select ama_code,ama_desc from account_main WHERE ama_desc like %s or ama_desc like %s",
         tuple([query, query]))
    print('accountmain is *********** ')
    for obj in accountmain:
        print('accountmain is  ' + obj.ama_desc)
        select2 = Select2Data()
        select2.id = str(obj.ama_code)
        select2.text = obj.ama_desc
        serializer = Select2Serializer(select2)

        listsel.append(serializer.data)

    return JsonResponse({'results': listsel})

