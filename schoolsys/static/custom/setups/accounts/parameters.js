
$(document).ready(function () {
    $.ajaxSetup({
        headers: {
            "X-CSRFToken": $('[name=csrfmiddlewaretoken]').val()
        }
    });
    paramModal();
    getParameters();
    saveParameter();
    editParameter();
    deleteParameter();
//    searchParameter();
})
function paramModal() {
    $('#open-modal').click(function () {
        clearData()
        $('#paramModal').modal({backdrop: 'static', keyboard: false})
    })

}
function clearData(){
//      $('#dorm-form').empty();
      $('#param-form')[0].reset();
      $('#param_code').val('');
}
function deleteParameter() {
    $('#paramTable').on('click','.btn-deleteParameter',function (s) {
        var data = $(this).closest('tr').find('#delete-parameter').val();
        bootbox.confirm("Are you sure want to delete this Parameter?", function (result) {
            if (result) {
               $.ajax({
            type: 'GET',
            url: 'deleteParameter/'+data,
            processData: false,
            contentType: false,
        }).done(function (s) {
          bootbox.hideAll()
          getParameters()
          bootbox.alert(s.success)


        }).fail(function (xhr, error) {
        bootbox.alert(xhr.responseText)
        });
            }
        })
    })
}

function getParameters() {
     $.ajax({
        type: 'GET',
        url: 'getParameters',
        processData: false,
        contentType: false,
    }).done(function (s) {
       $('#paramTable').DataTable().destroy();
       $("#paramTable tbody").empty();
        if(s.length!==0) {
            $.each(s, function (i, item) {
                $("#paramTable tbody").append(
                    "<tr scope='col'>"
                    + "<td>" + item.param_name + "</td>"
                    + "<td>" + item.param_value + "</td>"
                    + "<td>" + item.param_desc + "</td>"
                    + "<td>" + '<form id="editParameter" method="post" enctype="multipart/form-data"><input type="hidden" id="edit-parameter" name="id" value=' + item.param_code + '></form><button class="btn btn-outline-primary btn-sm btn-editParameter" ><i class="fa fa-edit"></button>'
                    + "</td>"
                    + "<td>" + '<form id="deleteParameter" method="post" enctype="multipart/form-data"><input type="hidden" id="delete-parameter" name="id" value=' + item.param_code + '></form><button class="btn btn-outline-danger btn-sm btn-deleteParameter" ><i class="fa fa-trash-o"></button>'
                    + "</tr>")
            })
        }
        $('#paramTable').DataTable();
    }).fail(function (xhr, error) {
       bootbox.alert(xhr.responseText);
    });

}

function saveParameter(){
    $('#saveParam').click(function () {
        var data=$('#param-form').serialize();
        var url = '';
        if($('#param_code').val()===''){
          url = 'createParameter'
        }else{
            url = 'updateParameter/'+$('#param_code').val()
        }
		$.ajax({
			type: 'POST',
			url: url,
            data: data
		}).done(function (s) {
		    getParameters()
            clearData()
            $('#paramModal').modal('hide')
			bootbox.alert(s.success)

		}).fail(function (xhr, error) {
						bootbox.alert(xhr.responseText)
            // bootbox.alert("Error Occured while saving")
		})


	})
}
function editParameter(){
    $('#paramTable').on('click','.btn-editParameter',function (s) {
        var data=$(this).closest('tr').find('#edit-parameter').val();
        $.ajax({
            type: 'GET',
            url: 'editParameter/'+data,
            processData: false,
            contentType: false,
        }).done(function (s) {
            //alert(val(s.dorm-code));
            // alert((s.dormCode));
            $('#param_code').val(s.param_code);
            $('#param_name').val(s.param_name);
            $('#param_value').val(s.param_value);
            $('#param_desc').val(s.param_desc);



        $('#paramModal').modal({backdrop: 'static', keyboard: false})
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

