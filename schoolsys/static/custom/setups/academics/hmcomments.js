
$(document).ready(function () {
    $.ajaxSetup({
        headers: {
            "X-CSRFToken": $('[name=csrfmiddlewaretoken]').val()
        }
    });
    hmModal();
    getHMComments();
    saveHMComments();
    editHMComments();
    deleteHMComments();
})
function hmModal() {
    $('#open-modal').click(function () {
        clearData()
        $('#hmModal').modal({backdrop: 'static', keyboard: false})
    })

}
function clearData(){
      $('#hm-form')[0].reset();
      $('#hm_code').val('');
}
function deleteHMComments() {
    $('#hmTable').on('click','.btn-deleteHMComments',function (s) {
        var data = $(this).closest('tr').find('#delete-hmcomments').val();
        bootbox.confirm("Are you sure want to delete this Comment?", function (result) {
            if (result) {
               $.ajax({
            type: 'GET',
            url: 'deleteHMComments/'+data,
            processData: false,
            contentType: false,
        }).done(function (s) {
          bootbox.hideAll()
          getHMComments()
          bootbox.alert(s.success)


        }).fail(function (xhr, error) {
        bootbox.alert(xhr.responseText)
        });
            }
        })
    })
}

function getHMComments() {
     $.ajax({
        type: 'GET',
        url: 'getHMComments',
        processData: false,
        contentType: false,
    }).done(function (s) {
       $('#hmTable').DataTable().destroy();
       $("#hmTable tbody").empty();
        if(s.length!==0) {
            $.each(s, function (i, item) {
                $("#hmTable tbody").append(
                    "<tr scope='col'>"
                    + "<td>" + item.hm_val1 + "</td>"
                    + "<td>" + item.hm_val2 + "</td>"
                    + "<td>" + item.hm_grade + "</td>"
                    + "<td>" + item.hm_remarks + "</td>"
                    + "<td>" + '<form id="editHMComments" method="post" enctype="multipart/form-data"><input type="hidden" id="edit-hmcomments" name="id" value=' + item.hm_code + '></form><button class="btn btn-outline-primary btn-sm btn-editHMComments" ><i class="fa fa-edit"></button>'
                    + "</td>"
                    + "<td>" + '<form id="deleteHMComments" method="post" enctype="multipart/form-data"><input type="hidden" id="delete-hmcomments" name="id" value=' + item.hm_code + '></form><button class="btn btn-outline-danger btn-sm btn-deleteHMComments" ><i class="fa fa-trash-o"></button>'
                    + "</tr>")
            })
        }
        $('#hmTable').DataTable();
    }).fail(function (xhr, error) {
       bootbox.alert(xhr.responseText);
    });

}

function saveHMComments(){
    $('#saveHMComments').click(function () {
        var data=$('#hm-form').serialize();
        var url = '';
        if($('#hm_code').val()===''){
          url = 'createHMComments'
        }else{
            url = 'updateHMComments/'+$('#hm_code').val()
        }
		$.ajax({
			type: 'POST',
			url: url,
            data: data
		}).done(function (s) {
		    getHMComments()
            clearData()
            $('#hmModal').modal('hide')
			bootbox.alert(s.success)

		}).fail(function (xhr, error) {
						bootbox.alert(xhr.responseText)
            // bootbox.alert("Error Occured while saving")
		})


	})
}
function editHMComments(){
    $('#hmTable').on('click','.btn-editHMComments',function (s) {
        var data=$(this).closest('tr').find('#edit-hmcomments').val();
        $.ajax({
            type: 'GET',
            url: 'editHMComments/'+data,
            processData: false,
            contentType: false,
        }).done(function (s) {
            $('#hm_code').val(s.hm_code);
            $('#hm_val1').val(s.hm_val1);
            $('#hm_val2').val(s.hm_val2);
            $('#hm_grade').val(s.hm_grade);
            $('#hm_remarks').val(s.hm_remarks);



        $('#hmModal').modal({backdrop: 'static', keyboard: false})
        }).fail(function (xhr, error) {
        bootbox.alert(xhr.responseText)
        });
    });

}
