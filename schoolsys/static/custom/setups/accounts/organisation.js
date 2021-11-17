$(document).ready(function () {
    $.ajaxSetup({
        headers: {
            "X-CSRFToken": $('[name=csrfmiddlewaretoken]').val()
        }
    });
    logoImage("");
    logoImage2("");
    getOrganisations();
    saveOrganisation();
    editOrganisation();
    deleteOrganisation();
    newOrganisation();
    testProc();
})
function newOrganisation() {
   $('#newOrg').click(function () {
       clearData()
       logoImage("");
       logoImage2("");
   })
}
function deleteOrganisation() {
    $('#orgTable').on('click','.btn-deleteOrganisation',function (s) {
        var data = $(this).closest('tr').find('#delete-organisation').val();
        if(data===''){
           bootbox.alert('No Organisation Selected For Deletion')
        }
        else {
            bootbox.confirm("Are you sure want to delete this Organisation?", function (result) {
                if (result) {
                    $.ajax({
                        type: 'GET',
                        url: 'deleteOrganisation/' + data,
                        processData: false,
                        contentType: false,
                    }).done(function (s) {
                        bootbox.hideAll()
                        getOrganisations()
                        bootbox.alert(s.success)


                    }).fail(function (xhr, error) {
                        bootbox.alert(xhr.responseText)
                    });
                }
            })
        }
    })

}

function editOrganisation(){
    $('#orgTable').on('click','.btn-editOrganisation',function (s) {
        var data=$(this).closest('tr').find('#edit-organisation').val();
        $.ajax({
            type: 'GET',
            url: 'editOrganisation/'+data,
            processData: false,
            contentType: false,
        }).done(function (s) {
           $('#org_code').val(s.org_code);
            $('#Org_Name').val(s.Org_Name);
			$('#Org_Physical_Address').val(s.Org_Physical_Address);
			$('#Org_Tel_No').val(s.Org_Tel_No);
			$('#Org_Email').val(s.Org_Email);
			$('#Org_Tag_Line').val(s.Org_Tag_Line);
			$('#Org_Poastal_Address').val(s.Org_Poastal_Address);
			$('#Org_Cell_No').val(s.Org_Cell_No);
			$('#Org_Website').val(s.Org_Website);
			$('#Org_Mission').val(s.Org_Mission);
			$('#Org_Vision').val(s.Org_Vision);
			$('#Org_Pin_No').val(s.Org_Pin_No);
            $('#Org_NHIF_Code').val(s.Org_NHIF_Code);
            $('#Org_NSSF_Code').val(s.Org_NSSF_Code);


			if(s.url) {
                logoImage(s.url)
            }
            else{
			    logoImage("")
            }

            if(s.url2) {
                logoImage2(s.url2)
            }
            else{
			    logoImage2("")
            }

        }).fail(function (xhr, error) {
        bootbox.alert(xhr.responseText)
        });
    });

}

function clearData(){
      $('#org_code').val('');
      $('#org-form')[0].reset();
}
function saveOrganisation(){
    $('#saveOrg').click(function () {
        if($('#Org_Name').val()==='' || $('#Org_Cell_No').val()==='' || $('#Org_Physical_Address').val()===''){
            bootbox.alert('Please Provide data to save !!!')
        }
        else {
            var form = $("#org-form")[0];
            var data = new FormData(form);
            data.append('Org_Logo', $('#logo1-avatar')[0].files[0]);
            data.append('Org_Logo2', $('#logo2-avatar')[0].files[0]);
            var url = '';
            if ($('#org_code').val() === '') {
                url = 'addOrganisation'
            } else {
                url = 'updateOrganisation/' + $('#org_code').val()
            }
            $.ajax({
                type: 'POST',
                url: url,
                data: data,
                processData: false,
                contentType: false
                // data: {
                // 	'firstName':$('#inputFirstname').val(),
                // 	'lastName':$('#inputLastname').val(),
                // 	'age':$('#inputAge').val(),
                // 	'height':$('#inputHeight').val(),
                // 	'country':$('#inputCountry').val(),
                // 	'county':$('#inputCounty').val(),
                // 	'town':$('#inputTown').val(),
                // 	'phone':$('#inputPhone').val(),
                // 	'website':$('#inputWebsite').val(),
                // }
            }).done(function (s) {
                getOrganisations();
                clearData();
                bootbox.alert(s.success)

            }).fail(function (xhr, error) {
                bootbox.alert(xhr.responseText)
                // bootbox.alert("Error Occured while saving")
            })

        }
	})
}
function testProc(){
    $('#testOrg').click(function () {

            var form = $("#org-form")[0];
            var data = new FormData(form);
            data.append('Org_Logo', $('#logo1-avatar')[0].files[0]);
            data.append('Org_Logo2', $('#logo2-avatar')[0].files[0]);
            var url = '';
            url = 'testProc'
            $.ajax({
                type: 'POST',
                url: url,
                data: data,
                processData: false,
                contentType: false

            }).done(function (s) {
                bootbox.alert(s.success)
            }).fail(function (xhr, error) {
                bootbox.alert(xhr.responseText)
                // bootbox.alert("Error Occured while saving")
            })


	})
}
function getOrganisations() {
     $.ajax({
        type: 'GET',
        url: 'getOrganisations',
        processData: false,
        contentType: false,
    }).done(function (s) {
       $('#orgTable').DataTable().destroy();
       $("#orgTable tbody").empty();
        if(s.length!==0) {
            $.each(s, function (i, item) {
                $("#orgTable tbody").append(
                    "<tr scope='col'>"
                    + "<td>" + item.Org_Name + "</td>"
                    + "<td>" + item.Org_Physical_Address + "</td>"
                    + "<td>" + item.Org_Cell_No + "</td>"
                    + "<td>" + item.Org_Email + "</td>"
                    + "<td>" + item.Org_Website + "</td>"
                    + "<td>" + item.Org_Mission + "</td>"
                    + "<td>" + item.Org_Vision + "</td>"
                    + "<td>" + '<form id="editForm" method="post" enctype="multipart/form-data"><input type="hidden" id="edit-organisation" name="id" value=' + item.org_code + '></form><button class="btn btn-outline-primary btn-sm btn-editOrganisation" ><i class="fa fa-edit"></button>'
                    + "</td>"
                    + "<td>" + '<form id="deleteForm" method="post" enctype="multipart/form-data"><input type="hidden" id="delete-organisation" name="id" value=' + item.org_code + '></form><button class="btn btn-outline-danger btn-sm btn-deleteOrganisation" ><i class="fa fa-trash-o"></button>'
                    + "</tr>")
            })
        }
        $('#orgTable').DataTable();
    }).fail(function (xhr, error) {
       bootbox.alert(xhr.responseText);
    });

}

function logoImage(url){
    console.log(url)
        $("#logo1-avatar").fileinput('destroy').fileinput({
            overwriteInitial: true,
            maxFileSize: 1500,
            showClose: false,
            showCaption: false,
            browseLabel: '',
            removeLabel: '',
            browseIcon: '<i class="fa fa-folder-open"></i>',
            removeIcon: '<i class="fa fa-times"></i>',
            removeTitle: 'Cancel or reset changes',
            elErrorContainer: '#kv-avatar-errors',
            msgErrorClass: 'alert alert-block alert-danger',
            defaultPreviewContent: '<img src="' + url + '"  style="height:15em;width:200px">',
            layoutTemplates: {main2: '{preview} ' + ' {remove} {browse}'},
            allowedFileExtensions: ["jpg", "png", "gif"]
        });

}

function logoImage2(url2){
    console.log(url2)
        $("#logo2-avatar").fileinput('destroy').fileinput({
            overwriteInitial: true,
            maxFileSize: 1500,
            showClose: false,
            showCaption: false,
            browseLabel: '',
            removeLabel: '',
            browseIcon: '<i class="fa fa-folder-open"></i>',
            removeIcon: '<i class="fa fa-times"></i>',
            removeTitle: 'Cancel or reset changes',
            elErrorContainer: '#kv-avatar-errors',
            msgErrorClass: 'alert alert-block alert-danger',
            defaultPreviewContent: '<img src="' + url2 + '"  style="height:15em;width:200px">',
            layoutTemplates: {main2: '{preview} ' + ' {remove} {browse}'},
            allowedFileExtensions: ["jpg", "png", "gif"]
        });

}