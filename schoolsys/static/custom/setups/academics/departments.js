
$(document).ready(function () {
    $.ajaxSetup({
        headers: {
            "X-CSRFToken": $('[name=csrfmiddlewaretoken]').val()
        }
    });
    departmentModal();
    getDepartments();
    saveDepartment();
    editDepartment();
    deleteDepartment();
    searchDepartment();
})
function departmentModal() {
    $('#open-modal').click(function () {
        clearData()
        $('#departmentModal').modal({backdrop: 'static', keyboard: false})
    })

}
function clearData(){
//      $('#dorm-form').empty();
      $('#department-form')[0].reset();
      $('#dpCode').val('');
}
function deleteDepartment() {
    $('#departmentTable').on('click','.btn-deleteDepartment',function (s) {
        var data = $(this).closest('tr').find('#delete-department').val();
        bootbox.confirm("Are you sure want to delete this department?", function (result) {
            if (result) {
               $.ajax({
            type: 'GET',
            url: 'deleteDepartment/'+data,
            processData: false,
            contentType: false,
        }).done(function (s) {
          bootbox.hideAll()
          getDepartments()
          bootbox.alert(s.success)


        }).fail(function (xhr, error) {
        bootbox.alert(xhr.responseText)
        });
            }
        })
    })
}

function getDepartments() {
     $.ajax({
        type: 'GET',
        url: 'getDepartments',
        processData: false,
        contentType: false,
    }).done(function (s) {
       $('#departmentTable').DataTable().destroy();
       $("#departmentTable tbody").empty();
        if(s.length!==0) {
            $.each(s, function (i, item) {
                $("#departmentTable tbody").append(
                    "<tr scope='col'>"
                    + "<td>" + item.dpShtName + "</td>"
                    + "<td>" + item.dpName + "</td>"
                    + "<td>" + item.dpSequence + "</td>"
                    + "<td>" + '<form id="editDepartment" method="post" enctype="multipart/form-data"><input type="hidden" id="edit-department" name="id" value=' + item.dpCode + '></form><button class="btn btn-outline-primary btn-sm btn-editDepartment" ><i class="fa fa-edit"></button>'
                    + "</td>"
                    + "<td>" + '<form id="deleteDepartment" method="post" enctype="multipart/form-data"><input type="hidden" id="delete-department" name="id" value=' + item.dpCode + '></form><button class="btn btn-outline-danger btn-sm btn-deleteDepartment" ><i class="fa fa-trash-o"></button>'
                    + "</tr>")
            })
        }
        $('#departmentTable').DataTable();
    }).fail(function (xhr, error) {
       bootbox.alert(xhr.responseText);
    });

}

function saveDepartment(){
    $('#saveDepartment').click(function () {
        var data=$('#department-form').serialize();
        var url = '';
        if($('#dpCode').val()===''){
          url = 'createDepartment'
        }else{
            url = 'updateDepartment/'+$('#dpCode').val()
        }
		$.ajax({
			type: 'POST',
			url: url,
            data: data
		}).done(function (s) {
		    getDepartments()
            clearData()
            $('#departmentModal').modal('hide')
			bootbox.alert(s.success)

		}).fail(function (xhr, error) {
						bootbox.alert(xhr.responseText)
            // bootbox.alert("Error Occured while saving")
		})


	})
}
function editDepartment(){
    $('#departmentTable').on('click','.btn-editDepartment',function (s) {
        var data=$(this).closest('tr').find('#edit-department').val();
        $.ajax({
            type: 'GET',
            url: 'editDepartment/'+data,
            processData: false,
            contentType: false,
        }).done(function (s) {
            //alert(val(s.dorm-code));
            // alert((s.dormCode));
            $('#dpCode').val(s.dpCode);
            $('#dpShtName').val(s.dpShtName);
            $('#dpName').val(s.dpName);
            $('#dpSequence').val(s.dpSequence);



        $('#departmentModal').modal({backdrop: 'static', keyboard: false})
        }).fail(function (xhr, error) {
        bootbox.alert(xhr.responseText)
        });
    });

}

function searchDepartment() {
     $('#department-frm').select2({
           placeholder: 'Departments',
           allowClear: true,
           width: '100%' ,
           ajax: {
             delay: 250,
             url: 'searchDepartment',
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

