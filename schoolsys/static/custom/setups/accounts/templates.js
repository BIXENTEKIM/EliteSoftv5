
$(document).ready(function () {
    $.ajaxSetup({
        headers: {
            "X-CSRFToken": $('[name=csrfmiddlewaretoken]').val()
        }
    });
    tempModal();
    getTemplates();
    saveTemplate();
    editTemplate();
    deleteTemplate();
//    searchParameter();
})
function tempModal() {
    $('#open-modal').click(function () {
        clearData()
        $('#tempModal').modal({backdrop: 'static', keyboard: false})
    })

}
function clearData(){
//      $('#dorm-form').empty();
      $('#temp-form')[0].reset();
      $('#temp_code').val('');
}
function deleteTemplate() {
    $('#tempTable').on('click','.btn-deleteTemplate',function (s) {
        var data = $(this).closest('tr').find('#delete-template').val();
        bootbox.confirm("Are you sure want to delete this Template?", function (result) {
            if (result) {
               $.ajax({
            type: 'GET',
            url: 'deleteTemplate/'+data,
            processData: false,
            contentType: false,
        }).done(function (s) {
          bootbox.hideAll()
          getTemplates()
          bootbox.alert(s.success)


        }).fail(function (xhr, error) {
        bootbox.alert(xhr.responseText)
        });
            }
        })
    })
}

function getTemplates() {
     $.ajax({
        type: 'GET',
        url: 'getTemplates',
        processData: false,
        contentType: false,
    }).done(function (s) {
       $('#tempTable').DataTable().destroy();
       $("#tempTable tbody").empty();
        if(s.length!==0) {
            $.each(s, function (i, item) {
                $("#tempTable tbody").append(
                    "<tr scope='col'>"
                    + "<td>" + item.temp_module + "</td>"
                    + "<td>" + item.temp_name + "</td>"
                    + "<td>" + item.temp_desc + "</td>"
                    + "<td>" + '<form id="editTemplate" method="post" enctype="multipart/form-data"><input type="hidden" id="edit-template" name="id" value=' + item.temp_code + '></form><button class="btn btn-outline-primary btn-sm btn-editTemplate" ><i class="fa fa-edit"></button>'
                    + "</td>"
                    + "<td>" + '<form id="deleteTemplate" method="post" enctype="multipart/form-data"><input type="hidden" id="delete-template" name="id" value=' + item.temp_code + '></form><button class="btn btn-outline-danger btn-sm btn-deleteTemplate" ><i class="fa fa-trash-o"></button>'
                    + "</tr>")
            })
        }
        $('#tempTable').DataTable();
    }).fail(function (xhr, error) {
       bootbox.alert(xhr.responseText);
    });

}

function saveTemplate(){
    $('#saveTemp').click(function () {
        var data=$('#temp-form').serialize();
        var url = '';
        if($('#temp_code').val()===''){
          url = 'createTemplate'
        }else{
            url = 'updateTemplate/'+$('#temp_code').val()
        }
		$.ajax({
			type: 'POST',
			url: url,
            data: data
		}).done(function (s) {
		    getTemplates()
            clearData()
            $('#tempModal').modal('hide')
			bootbox.alert(s.success)

		}).fail(function (xhr, error) {
						bootbox.alert(xhr.responseText)
            // bootbox.alert("Error Occured while saving")
		})


	})
}
function editTemplate(){
    $('#tempTable').on('click','.btn-editTemplate',function (s) {
        var data=$(this).closest('tr').find('#edit-template').val();
        $.ajax({
            type: 'GET',
            url: 'editTemplate/'+data,
            processData: false,
            contentType: false,
        }).done(function (s) {
            //alert(val(s.dorm-code));
            // alert((s.dormCode));
            $('#temp_code').val(s.temp_code);
            $('#temp_module').val(s.temp_module);
            $('#temp_name').val(s.temp_name);
            $('#temp_desc').val(s.temp_desc);



        $('#tempModal').modal({backdrop: 'static', keyboard: false})
        }).fail(function (xhr, error) {
        bootbox.alert(xhr.responseText)
        });
    });

}
//
//function searchParameter() {
//     $('#param-frm').select2({
//           placeholder: 'Parameters',
//           allowClear: true,
//           width: '100%' ,
//           ajax: {
//             delay: 250,
//             url: 'searchParameter',
//             data: function (params) {
//                 console.log("AA", params);
//                 return {
//                     query: params.term,
//                     gotoPage: params.page
//                 }
//             },
//
//             processResults: function (data,params) {
//                 params.page = params.page || 1;
//                 console.log('data: ', data);
//                 return {
//                   results: data.results
//                 };
//             }
//
//         }
//     })
//}

