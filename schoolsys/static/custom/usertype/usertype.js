
$(document).ready(function () {
    $.ajaxSetup({
        headers: {
            "X-CSRFToken": $('[name=csrfmiddlewaretoken]').val()
        }
    });
    usertypeModal();
    getUsertypes();
    saveUsertype();
    editUsertype();
    deleteUsertype();
//    searchDorm();
})
function usertypeModal() {
    $('#open-modal').click(function () {
        clearData()
        $('#usertypeModal').modal({backdrop: 'static', keyboard: false})
    })

}
function clearData(){
//      $('#dorm-form').empty();
      $('#usertype-form')[0].reset();
      $('#type_code').val('');
}
function deleteUsertype() {
    $('#usertypeTable').on('click','.btn-deleteUsertype',function (s) {
        var data = $(this).closest('tr').find('#delete-usertype').val();
        bootbox.confirm("Are you sure want to delete this User Type?", function (result) {
            if (result) {
               $.ajax({
            type: 'GET',
            url: 'deleteUsertype/'+data,
            processData: false,
            contentType: false,
        }).done(function (s) {
          bootbox.hideAll()
          getUsertypes()
          bootbox.alert(s.success)


        }).fail(function (xhr, error) {
        bootbox.alert(xhr.responseText)
        });
            }
        })
    })
}

function getUsertypes() {
     $.ajax({
        type: 'GET',
        url: 'getUsertypes',
        processData: false,
        contentType: false,
    }).done(function (s) {
       $('#usertypeTable').DataTable().destroy();
       $("#usertypeTable tbody").empty();
        if(s.length!==0) {
            $.each(s, function (i, item) {
                $("#usertypeTable tbody").append(
                    "<tr scope='col'>"
                    + "<td>" + item.type_name + "</td>"
                    + "<td>" + item.type_desc + "</td>"
//                    + "<td>" + '<form id="editUsertype" method="post" enctype="multipart/form-data"><input type="hidden" id="edit-usertype" name="id" value=' + item.type_code + '></form><button class="btn btn-outline-primary btn-sm btn-editUsertype" ><i class="fa fa-edit"></button>'
//                    + "</td>"
//                    + "<td>" + '<form id="deleteUsertype" method="post" enctype="multipart/form-data"><input type="hidden" id="delete-usertype" name="id" value=' + item.type_code + '></form><button class="btn btn-outline-danger btn-sm btn-deleteUsertype" ><i class="fa fa-trash-o"></button>'
                    + "</tr>")
            })
        }
        $('#usertypeTable').DataTable();
    }).fail(function (xhr, error) {
       bootbox.alert(xhr.responseText);
    });

}

function saveUsertype(){
    $('#saveUsertype').click(function () {
        var data=$('#usertype-form').serialize();
        var url = '';
        if($('#type_code').val()===''){
          url = 'createUsertype'
        }else{
            url = 'updateUsertype/'+$('#type_code').val()
        }
		$.ajax({
			type: 'POST',
			url: url,
            data: data
		}).done(function (s) {
		    getUsertypes()
            clearData()
            $('#usertypeModal').modal('hide')
			bootbox.alert(s.success)

		}).fail(function (xhr, error) {
						bootbox.alert(xhr.responseText)
            // bootbox.alert("Error Occured while saving")
		})


	})
}
function editUsertype(){
    $('#usertypeTable').on('click','.btn-editUsertype',function (s) {
        var data=$(this).closest('tr').find('#edit-usertype').val();
        $.ajax({
            type: 'GET',
            url: 'editUsertype/'+data,
            processData: false,
            contentType: false,
        }).done(function (s) {
            $('#type_code').val(s.type_code);
            $('#type_name').val(s.type_name);
            $('#type_desc').val(s.type_desc);



        $('#usertypeModal').modal({backdrop: 'static', keyboard: false})
        }).fail(function (xhr, error) {
        bootbox.alert(xhr.responseText)
        });
    });

}
