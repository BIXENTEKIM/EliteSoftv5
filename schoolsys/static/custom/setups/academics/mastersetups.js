
$(document).ready(function () {
    $.ajaxSetup({
        headers: {
            "X-CSRFToken": $('[name=csrfmiddlewaretoken]').val()
        }
    });
    mastersetupsModal();
    getMasterSetups();
    saveMasterSetups();
    editMasterSetups();
    deleteMasterSetups();
//    searchMasterSetups();
})
function mastersetupsModal() {
    $('#open-modal').click(function () {
        clearData()
        $('#mastersetupsModal').modal({backdrop: 'static', keyboard: false})
    })

}
function clearData(){
//      $('#mastersetups-form').empty();
      $('#mastersetups-form')[0].reset();
      $('#ms_code').val('');
}
function deleteMasterSetups() {
    $('#mastersetupsTable').on('click','.btn-deleteMasterSetups',function (s) {
        var data = $(this).closest('tr').find('#delete-mastersetups').val();
        bootbox.confirm("Are you sure want to delete this Setup?", function (result) {
            if (result) {
               $.ajax({
            type: 'GET',
            url: 'deleteMasterSetups/'+data,
            processData: false,
            contentType: false,
        }).done(function (s) {
          bootbox.hideAll()
          getMasterSetups()
          bootbox.alert(s.success)


        }).fail(function (xhr, error) {
        bootbox.alert(xhr.responseText)
        });
            }
        })
    })
}

function getMasterSetups() {
     $.ajax({
        type: 'GET',
        url: 'getMasterSetups',
        processData: false,
        contentType: false,
    }).done(function (s) {
       $('#mastersetupsTable').DataTable().destroy();
       $("#mastersetupsTable tbody").empty();
        if(s.length!==0) {
            $.each(s, function (i, item) {
                $("#mastersetupsTable tbody").append(
                    "<tr scope='col'>"
                    + "<td>" + item.ms_desc + "</td>"
                    + "<td>" + item.ms_type + "</td>"
                    + "<td>" + '<form id="editMasterSetups" method="post" enctype="multipart/form-data"><input type="hidden" id="edit-mastersetups" name="id" value=' + item.ms_code + '></form><button class="btn btn-outline-primary btn-sm btn-editMasterSetups" ><i class="fa fa-edit"></button>'
                    + "</td>"
                    + "<td>" + '<form id="deleteMasterSetups" method="post" enctype="multipart/form-data"><input type="hidden" id="delete-mastersetups" name="id" value=' + item.ms_code + '></form><button class="btn btn-outline-danger btn-sm btn-deleteMasterSetups" ><i class="fa fa-trash-o"></button>'
                    + "</tr>")
            })
        }
        $('#mastersetupsTable').DataTable();
    }).fail(function (xhr, error) {
       bootbox.alert(xhr.responseText);
    });

}

function saveMasterSetups(){
    $('#saveMasterSetups').click(function () {
        var data=$('#mastersetups-form').serialize();
        var url = '';
        if($('#ms_code').val()===''){
          url = 'createMasterSetups'
        }else{
            url = 'updateMasterSetups/'+$('#ms_code').val()
        }
		$.ajax({
			type: 'POST',
			url: url,
            data: data
		}).done(function (s) {
		    getMasterSetups()
            clearData()
            $('#mastersetupsModal').modal('hide')
			bootbox.alert(s.success)

		}).fail(function (xhr, error) {
						bootbox.alert(xhr.responseText)
            // bootbox.alert("Error Occured while saving")
		})


	})
}
function editMasterSetups(){
    $('#mastersetupsTable').on('click','.btn-editMasterSetups',function (s) {
        var data=$(this).closest('tr').find('#edit-mastersetups').val();
        $.ajax({
            type: 'GET',
            url: 'editMasterSetups/'+data,
            processData: false,
            contentType: false,
        }).done(function (s) {
            //alert(val(s.mastersetups-code));
            // alert((s.dormCode));
            $('#ms_code').val(s.ms_code);
            $('#ms_desc').val(s.ms_desc);
            $('#ms_type').val(s.ms_type);



        $('#mastersetupsModal').modal({backdrop: 'static', keyboard: false})
        }).fail(function (xhr, error) {
        bootbox.alert(xhr.responseText)
        });
    });

}

function searchMasterSetups() {
     $('#mastersetups-frm').select2({
           placeholder: 'MasterSetups',
           allowClear: true,
           width: '100%' ,
           ajax: {
             delay: 250,
             url: 'searchMasterSetups',
             data: function (params) {
                 console.log("AA", params);
                 return {
                     query: params.term,
                     gotoPage: params.page
                 }
             },

             processResults: function (data,params) {
                 params.page = params.page || 1;
                 console.log('data: ', data);
                 return {
                   results: data.results
                 };
             }

         }
     })
}

