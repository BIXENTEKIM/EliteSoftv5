
$(document).ready(function () {
    $.ajaxSetup({
        headers: {
            "X-CSRFToken": $('[name=csrfmiddlewaretoken]').val()
        }
    });
    dormModal();
    getDorms();
    saveDorm();
    editDorm();
    deleteDorm();
    searchDorm();
})
function dormModal() {
    $('#open-modal').click(function () {
        clearData()
        $('#dormModal').modal({backdrop: 'static', keyboard: false})
    })

}
function clearData(){
      $('#dorm-form').empty();
      $('#dorm-form')[0].reset();
      $('#dormCode').val('');
}
function deleteDorm() {
    $('#dormTable').on('click','.btn-deleteDorm',function (s) {
        var data = $(this).closest('tr').find('#delete-dorm').val();
        bootbox.confirm("Are you sure want to delete this Dorm?", function (result) {
            if (result) {
               $.ajax({
            type: 'GET',
            url: 'deleteDorm/'+data,
            processData: false,
            contentType: false,
        }).done(function (s) {
          bootbox.hideAll()
          getDorms()
          bootbox.alert(s.success)


        }).fail(function (xhr, error) {
        bootbox.alert(xhr.responseText)
        });
            }
        })
    })
}

function getDorms() {
     $.ajax({
        type: 'GET',
        url: 'getDorms',
        processData: false,
        contentType: false,
    }).done(function (s) {
       $('#dormTable').DataTable().destroy();
       $("#dormTable tbody").empty();
        if(s.length!==0) {
            $.each(s, function (i, item) {
                $("#dormTable tbody").append(
                    "<tr scope='col'>"
                    + "<td>" + item.dormname + "</td>"
                    + "<td>" + item.maxCapacity + "</td>"
                    + "<td>" + item.currentCapacity + "</td>"
                    + "<td>" + '<form id="editDorm" method="post" enctype="multipart/form-data"><input type="hidden" id="edit-dorm" name="id" value=' + item.dormCode + '></form><button class="btn btn-outline-primary btn-sm btn-editDorm" ><i class="fa fa-edit"></button>'
                    + "</td>"
                    + "<td>" + '<form id="deleteDorm" method="post" enctype="multipart/form-data"><input type="hidden" id="delete-dorm" name="id" value=' + item.dormCode + '></form><button class="btn btn-outline-danger btn-sm btn-deleteDorm" ><i class="fa fa-trash-o"></button>'
                    + "</tr>")
            })
        }
        $('#dormTable').DataTable();
    }).fail(function (xhr, error) {
       bootbox.alert(xhr.responseText);
    });

}

function saveDorm(){
    $('#saveDorm').click(function () {
        var data=$('#dorm-form').serialize();
        var url = '';
        if($('#dormCode').val()===''){
          url = 'createDorm'
        }else{
            url = 'updateDorm/'+$('#dormCode').val()
        }
		$.ajax({
			type: 'POST',
			url: url,
            data: data
		}).done(function (s) {
		    getDorms()
            clearData()
            $('#dormModal').modal('hide')
			bootbox.alert(s.success)

		}).fail(function (xhr, error) {
						bootbox.alert(xhr.responseText)
            // bootbox.alert("Error Occured while saving")
		})


	})
}
function editDorm(){
    $('#dormTable').on('click','.btn-editDorm',function (s) {
        var data=$(this).closest('tr').find('#edit-dorm').val();
        $.ajax({
            type: 'GET',
            url: 'editDorm/'+data,
            processData: false,
            contentType: false,
        }).done(function (s) {
            $('#dormCode').val(s.dormCode);
            $('#dormname').val(s.dormname);
            $('#maxCapacity').val(s.maxCapacity);
            $('#currentCapacity').val(s.currentCapacity);



        $('#dormModal').modal({backdrop: 'static', keyboard: false})
        }).fail(function (xhr, error) {
        bootbox.alert(xhr.responseText)
        });
    });

}

function searchDorm() {
     $('#dorm-frm').select2({
           placeholder: 'Dorms',
           allowClear: true,
           width: '100%' ,
           ajax: {
             delay: 250,
             url: 'searchDorm',
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

